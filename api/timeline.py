"""
Timeline Analyzer Module
Creates a chronological timeline of digital footprint from collected OSINT data
"""

import json
from datetime import datetime
from collections import defaultdict
from core import color, symbol

class TimelineEvent:
    """Represents a single event in the timeline"""
    def __init__(self, date, platform, event_type, details, url=None):
        self.date = date
        self.platform = platform
        self.event_type = event_type
        self.details = details
        self.url = url
    
    def to_dict(self):
        return {
            "date": self.date,
            "platform": self.platform,
            "type": self.event_type,
            "details": self.details,
            "url": self.url
        }

class Timeline:
    """Manages timeline events and provides analysis"""
    
    def __init__(self, target):
        self.target = target
        self.events = []
        self.platforms_found = set()
        self.earliest_activity = None
        self.latest_activity = None
    
    def add_event(self, date, platform, event_type, details, url=None):
        """Add a new event to the timeline"""
        event = TimelineEvent(date, platform, event_type, details, url)
        self.events.append(event)
        self.platforms_found.add(platform)
        
        # Track earliest and latest activity
        if date:
            if not self.earliest_activity or date < self.earliest_activity:
                self.earliest_activity = date
            if not self.latest_activity or date > self.latest_activity:
                self.latest_activity = date
    
    def add_profile_found(self, platform, url):
        """Add profile discovery event"""
        self.add_event(
            datetime.now().strftime("%Y-%m-%d"),
            platform,
            "profile_found",
            f"Profile discovered on {platform}",
            url
        )
    
    def add_leak_event(self, leak_name, leak_date):
        """Add data leak event"""
        self.add_event(
            leak_date,
            "leak",
            "data_breach",
            f"Found in {leak_name} breach",
            None
        )
    
    def add_paste_event(self, paste_id, paste_url):
        """Add pastebin discovery event"""
        self.add_event(
            datetime.now().strftime("%Y-%m-%d"),
            "pastebin",
            "paste_found",
            f"Mentioned in paste {paste_id}",
            paste_url
        )
    
    def add_github_event(self, commit_id, commit_url, title):
        """Add GitHub commit event"""
        self.add_event(
            datetime.now().strftime("%Y-%m-%d"),
            "github",
            "commit_found",
            f"Found in commit: {title}",
            commit_url
        )
    
    def sort_events(self):
        """Sort events chronologically"""
        self.events.sort(key=lambda x: x.date if x.date else "9999-99-99", reverse=True)
    
    def get_activity_summary(self):
        """Generate activity summary"""
        summary = {
            "target": self.target,
            "total_events": len(self.events),
            "platforms_count": len(self.platforms_found),
            "platforms": list(self.platforms_found),
            "earliest_activity": self.earliest_activity,
            "latest_activity": self.latest_activity
        }
        return summary
    
    def display_timeline(self):
        """Display formatted timeline to console"""
        self.sort_events()
        
        print(f"\n{color.redbg}{color.bold} TIMELINE ANALYZER {color.reset}")
        print(f"{symbol.log} Target: {color.orange}{color.bold}{self.target}{color.reset}")
        print(f"{symbol.log} Total Events: {color.green}{color.bold}{len(self.events)}{color.reset}")
        print(f"{symbol.log} Platforms Found: {color.cyan}{color.bold}{len(self.platforms_found)}{color.reset}")
        
        if self.earliest_activity and self.latest_activity:
            print(f"{symbol.log} Activity Range: {color.yellow}{self.earliest_activity}{color.reset} to {color.yellow}{self.latest_activity}{color.reset}")
        
        print(f"\n{color.bold}{'='*70}{color.reset}")
        print(f"{color.bold}CHRONOLOGICAL TIMELINE{color.reset}")
        print(f"{color.bold}{'='*70}{color.reset}\n")
        
        # Group events by date
        events_by_date = defaultdict(list)
        for event in self.events:
            events_by_date[event.date].append(event)
        
        for date in sorted(events_by_date.keys(), reverse=True):
            print(f"\n{color.bluebg}{color.bold} {date} {color.reset}")
            for event in events_by_date[date]:
                icon = self._get_event_icon(event.event_type)
                platform_color = self._get_platform_color(event.platform)
                
                print(f"  {icon} [{platform_color}{event.platform.upper()}{color.reset}] {event.details}")
                if event.url:
                    print(f"      {color.gray}↳ {color.underline}{event.url}{color.reset}")
        
        print(f"\n{color.bold}{'='*70}{color.reset}\n")
    
    def _get_event_icon(self, event_type):
        """Get appropriate icon for event type"""
        icons = {
            "profile_found": f"{color.green}✓{color.reset}",
            "data_breach": f"{color.red}⚠{color.reset}",
            "paste_found": f"{color.yellow}📋{color.reset}",
            "commit_found": f"{color.cyan}⚡{color.reset}",
        }
        return icons.get(event_type, "•")
    
    def _get_platform_color(self, platform):
        """Get color for platform"""
        colors = {
            "leak": color.red,
            "pastebin": color.yellow,
            "github": color.cyan,
        }
        return colors.get(platform, color.green)
    
    def export_json(self, filename=None):
        """Export timeline to JSON file"""
        if not filename:
            filename = f"timeline_{self.target}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        timeline_data = {
            "summary": self.get_activity_summary(),
            "events": [event.to_dict() for event in self.events]
        }
        
        with open(filename, 'w') as f:
            json.dump(timeline_data, f, indent=2)
        
        print(f"{symbol.info} Timeline exported to: {color.green}{filename}{color.reset}")
        return filename
    
    def export_html(self, filename=None):
        """Export timeline to HTML file with visual representation"""
        if not filename:
            filename = f"timeline_{self.target}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        
        self.sort_events()
        
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Timeline - {self.target}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
            color: #333;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            padding: 30px;
        }}
        h1 {{
            color: #667eea;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
            margin-bottom: 30px;
        }}
        .summary {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 30px;
            border-left: 5px solid #667eea;
        }}
        .summary-item {{
            margin: 10px 0;
            font-size: 16px;
        }}
        .summary-item strong {{
            color: #667eea;
        }}
        .timeline {{
            position: relative;
            padding-left: 50px;
        }}
        .timeline::before {{
            content: '';
            position: absolute;
            left: 20px;
            top: 0;
            bottom: 0;
            width: 3px;
            background: linear-gradient(to bottom, #667eea, #764ba2);
        }}
        .timeline-date {{
            background: #667eea;
            color: white;
            padding: 10px 20px;
            border-radius: 20px;
            display: inline-block;
            margin: 20px 0 10px 0;
            font-weight: bold;
            box-shadow: 0 3px 10px rgba(102, 126, 234, 0.3);
        }}
        .timeline-event {{
            position: relative;
            margin-bottom: 20px;
            background: white;
            padding: 15px;
            border-radius: 10px;
            border: 1px solid #e9ecef;
            margin-left: 20px;
            transition: all 0.3s;
        }}
        .timeline-event:hover {{
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            transform: translateX(5px);
        }}
        .timeline-event::before {{
            content: '';
            position: absolute;
            left: -28px;
            top: 20px;
            width: 15px;
            height: 15px;
            border-radius: 50%;
            background: white;
            border: 3px solid #667eea;
        }}
        .event-platform {{
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 5px 15px;
            border-radius: 15px;
            font-size: 12px;
            font-weight: bold;
            margin-bottom: 10px;
        }}
        .event-platform.leak {{ background: #dc3545; }}
        .event-platform.pastebin {{ background: #ffc107; color: #333; }}
        .event-platform.github {{ background: #28a745; }}
        .event-details {{
            margin: 10px 0;
            color: #555;
        }}
        .event-url {{
            color: #667eea;
            text-decoration: none;
            font-size: 14px;
            word-break: break-all;
        }}
        .event-url:hover {{
            text-decoration: underline;
        }}
        .platforms-list {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 10px;
        }}
        .platform-tag {{
            background: #e9ecef;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 14px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🔍 Digital Footprint Timeline: {self.target}</h1>
        
        <div class="summary">
            <div class="summary-item"><strong>Total Events:</strong> {len(self.events)}</div>
            <div class="summary-item"><strong>Platforms Found:</strong> {len(self.platforms_found)}</div>
            <div class="summary-item">
                <strong>Platforms:</strong>
                <div class="platforms-list">
                    {''.join(f'<span class="platform-tag">{p}</span>' for p in sorted(self.platforms_found))}
                </div>
            </div>
            {f'<div class="summary-item"><strong>Activity Range:</strong> {self.earliest_activity} to {self.latest_activity}</div>' if self.earliest_activity else ''}
        </div>
        
        <div class="timeline">
"""
        
        # Group events by date
        events_by_date = defaultdict(list)
        for event in self.events:
            events_by_date[event.date].append(event)
        
        for date in sorted(events_by_date.keys(), reverse=True):
            html_content += f'            <div class="timeline-date">{date}</div>\n'
            for event in events_by_date[date]:
                html_content += f"""            <div class="timeline-event">
                <span class="event-platform {event.platform.lower()}">{event.platform.upper()}</span>
                <div class="event-details">{event.details}</div>
                {f'<a href="{event.url}" target="_blank" class="event-url">🔗 {event.url}</a>' if event.url else ''}
            </div>
"""
        
        html_content += """        </div>
    </div>
</body>
</html>"""
        
        with open(filename, 'w') as f:
            f.write(html_content)
        
        print(f"{symbol.info} HTML timeline exported to: {color.green}{filename}{color.reset}")
        return filename


# Global timeline instance
_timeline = None

def get_timeline(target):
    """Get or create timeline instance"""
    global _timeline
    if _timeline is None or _timeline.target != target:
        _timeline = Timeline(target)
    return _timeline

def finalize_timeline():
    """Display and export the timeline"""
    global _timeline
    if _timeline and len(_timeline.events) > 0:
        _timeline.display_timeline()
        _timeline.export_json()
        _timeline.export_html()
        print(f"\n{symbol.log} {color.green}Timeline analysis complete!{color.reset}\n")
