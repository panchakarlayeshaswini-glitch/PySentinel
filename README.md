# \# PySentinel: Automated Web Intelligence \& System Monitor

# 

# PySentinel is a Python-based automation engine designed to monitor web services and perform web intelligence tasks asynchronously.

# 

# \## Week 1 - Task 1

# \### Async HTTP Engine \& Service Health Monitor

# 

# Features:

# \- Monitor multiple web services

# \- Read target URLs from YAML

# \- Asynchronous HTTP requests using asyncio and httpx

# \- Display HTTP status codes

# \- Measure response latency

# \- Continuous service monitoring

# 

# \## Week 2 - Task 2

# \### Web Content Scraping \& Keyword Alert Engine

# 

# Features:

# \- Fetch webpage content asynchronously using HTTPX

# \- Extract webpage text using BeautifulSoup

# \- Load configurable keywords from YAML

# \- Detect matching keywords

# \- Store detected keywords in SQLite

# \- Prevent duplicate alerts using database constraints

# \- Generate alerts for newly detected keywords

# 

# \## Technologies Used

# 

# \- Python

# \- asyncio

# \- HTTPX

# \- BeautifulSoup

# \- PyYAML

# \- SQLite

# \- aiosqlite

# 

# \## Project Structure

# 

# ```text

# PySentinel/

# ├── config/

# │   └── targets.yaml

# ├── monitor.py

# ├── scraper.py

# ├── database.py

# ├── keywords.yaml

# ├── README.md

# ├── requirements.txt

# └── .gitignore

