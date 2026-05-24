# Satellite Telemetry Pipeline

A live ETL pipeline that pulls orbital tracking data from the U.S. Space Force
Space-Track.org API, processes Two-Line Element (TLE) data, and stores it for
visualization and analysis.

## Project Status
🔧 In active development — Phase 2: API integration and data ingestion

## What It Does
- Authenticates with the Space-Track.org API
- Pulls live TLE orbital data for tracked satellites (currently: ISS, NORAD ID 25544)
- Parses and stores raw JSON responses locally
- Future: AWS S3 storage, Grafana dashboard visualization

## Tech Stack
- Python 3
- requests, python-dotenv
- AWS S3 (coming Phase 2)
- Grafana (coming Phase 3)

## Setup
1. Clone the repo
2. Install dependencies: `pip3 install requests python-dotenv`
3. Copy `.env.example` to `.env` and add your Space-Track credentials
4. Run: `python3 src/fetch_tle.py`

## Author
Rob Casey — Software Development Engineer Intern
