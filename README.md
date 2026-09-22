# PySentinel: Automated Web Intelligence & System Monitor

PySentinel is a Python-based automation engine designed to monitor web services and perform web intelligence tasks asynchronously.

## Week 1 - Task 1

The first task implements an asynchronous service health monitoring daemon.

### Features

- Monitor multiple web services
- Read target URLs from a YAML configuration file
- Asynchronous HTTP requests using asyncio and httpx
- Display HTTP status codes
- Measure response latency
- Continuously monitor services at a 10-second interval
- Display UP/DOWN service status in the terminal

## Technologies Used

- Python
- asyncio
- httpx
- PyYAML
- YAML

## How to Run

python monitor.py

Press Ctrl+C to stop the monitor.

## Current Status

Week 1 - Task 1: Completed
