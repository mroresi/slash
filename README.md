# [Slash](https://github.com/theahmadov/slash)

Slash is **Automated Osint Tool** that allows you to **OSINT** people by their username.

### Slash OSINT Modules :
```python
|__Checker                                                    |
|  |                                                          |
|  |__Social Media Profile Check (+187)                       |
|  |__Forums Profile Check (+30)                              |
|  |__Leak Check (Username,Email-Adress)                      |
|                                                             |
|__Search                                                     |
|  |                                                          |
|  |__Pastebin Paste Search                                   |
|  |__Github Commit Search                                    |
|                                                             |
|__Extract Scrape                                             |
|  |                                                          |
|  |__Phone Number Extract      (From Bios,Raw Texts)         |
|  |__Mail Extractor            (From Bios,Raw Texts)         |
|  |__Bio Scraper               (Social Media)                |
|  |__Name Scraper              (Social Media)                |
|  |__Location Scraper          (Social Media)                |
|  |__Education Info Scraper    (Social Media)                |
|  |__Personal Website Scraper  (Social Media)                |
|                                                             |
|__Timeline Analyzer              ⭐ NEW FEATURE              |
|  |                                                          |
|  |__Chronological Activity Timeline                         |
|  |__Digital Footprint Visualization                         |
|  |__JSON Export                                             |
|  |__HTML Interactive Report                                 |
|__|__________________________________________________________|
```

## 🆕 Timeline Analyzer Feature

The **Timeline Analyzer** is an innovative feature that automatically aggregates all discovered OSINT data and creates a comprehensive chronological timeline of a target's digital footprint. This powerful visualization tool helps investigators understand the temporal aspects of online presence and activities.

### What it does:
- 📊 **Aggregates Data**: Automatically collects timestamps from all OSINT modules
- 🗓️ **Timeline View**: Displays all discoveries in chronological order
- 🎯 **Activity Summary**: Shows total events, platforms found, and activity range
- 💾 **JSON Export**: Exports structured timeline data for further analysis
- 🌐 **HTML Report**: Generates beautiful interactive HTML visualization
- 🎨 **Visual Timeline**: Color-coded events with icons for easy understanding

### Timeline Events Include:
- ✓ Social media profile discoveries
- ⚠ Data breach/leak findings with dates
- 📋 Pastebin mentions
- ⚡ GitHub commit references

The timeline is automatically generated at the end of each search and exported to both JSON and HTML formats for easy sharing and analysis.

### Visual Timeline Report

<p align="center">
  <img src="https://github.com/user-attachments/assets/394b44ac-d1f5-4b1c-b497-768c34b53b49" alt="Timeline Analyzer Screenshot" />
</p>

**[See detailed documentation →](TIMELINE_FEATURE.md)**

## Installation

```
git clone https://github.com/theahmadov/slash
cd slash
pip install -r requirements.txt
python slash.py help
```

## Usage & Syntax

* Username Syntax : **python slash.py username**
* Mail Adress Syntax : **python slash.py mail_adress**

* Example : 
```
python slash.py theahmadov
```
<h1 align="center">
  <img src="https://raw.githubusercontent.com/theahmadov/slash/main/images/1.png">
</h1>
<h1 align="center">
  <img src="https://github.com/theahmadov/slash/blob/main/images/2.png?raw=true">
</h1>

### Credits
Links of social.json : [sherlock-project](https://github.com/sherlock-project/sherlock/)


![](https://visitor-badge.glitch.me/badge?page_id=thesaderror.slash)
