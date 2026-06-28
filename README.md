# 🏥 Medical Telegram Data Warehouse

An end-to-end ELT pipeline for collecting, processing, and serving data from Ethiopian medical Telegram channels.

---

# Project Overview

This project extracts messages and images from public Ethiopian medical Telegram channels, stores them in a structured data lake, performs image object detection using YOLOv8, and exposes the processed data through a FastAPI REST API.

The project demonstrates modern Data Engineering concepts including data ingestion, storage, image processing, API development, and pipeline preparation for analytics.

---

# Objectives

- Scrape public Telegram medical channels
- Store raw messages as JSON
- Download images from Telegram posts
- Detect medical objects using YOLOv8
- Provide data access through FastAPI
- Prepare data for loading into PostgreSQL and analytics workflows

---

# Project Structure

```
medical-telegram-warehouse/
│
├── api/
│   └── main.py
│
├── data/
│   ├── raw/
│   │   ├── telegram_messages/
│   │   └── images/
│   │
│   └── processed/
│       └── yolo_results/
│
├── notebooks/
│
├── src/
│   ├── config.py
│   ├── loader.py
│   ├── scraper.py
│   ├── utils.py
│   └── yolo_detect.py
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---
## dbt Transformation Layer

A dbt project has been added under `medical_warehouse/` to model the raw Telegram data into a star schema.

Implemented dbt components:

- `stg_telegram_messages`: cleans raw Telegram message records
- `dim_channels`: channel-level dimension table
- `dim_dates`: date dimension for trend analysis
- `fct_messages`: analytical fact table
- `schema.yml`: dbt documentation and tests
- `assert_no_future_messages.sql`: custom data quality test

The intended warehouse flow is:

Raw Telegram JSON → PostgreSQL raw schema → dbt staging → dbt marts/star schema

# Technologies Used

- Python 3
- Telethon
- FastAPI
- YOLOv8 (Ultralytics)
- SQLAlchemy
- Pandas
- Docker (configuration)
- PostgreSQL (loader prepared)

---

# Data Pipeline

```
Telegram Channels
        │
        ▼
Telegram Scraper
        │
        ▼
Raw JSON Data Lake
        │
        ▼
Image Downloader
        │
        ▼
YOLO Object Detection
        │
        ▼
FastAPI Service
```

---

# Telegram Channels

The project currently collects data from:

- CheMed123
- Lobelia Cosmetics
- TIKVAH Pharmacy and Health Care

---

# Features

✅ Multi-channel Telegram scraping

✅ Raw JSON data storage

✅ Automatic image downloading

✅ YOLOv8 object detection

✅ FastAPI REST API

✅ Modular Python project structure

---

# API Endpoints

### Home

```
GET /
```

Returns API status.

---

### Swagger Documentation

```
GET /docs
```

Interactive API documentation.

---

### Retrieve Messages

```
GET /messages/{channel}
```

Example:

```
GET /messages/CheMed123
```

Returns scraped messages for the requested channel.

---

# Installation

Clone the repository

```bash
git clone https://github.com/Viv-la/medical-telegram-warehouse.git
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

### Scrape Telegram Channels

```bash
python src/scraper.py
```

---

### Run YOLO Detection

```bash
python src/yolo_detect.py
```

---

### Start FastAPI

```bash
uvicorn api.main:app --reload
```

Visit

```
http://127.0.0.1:8000/docs
```

---

# Sample Output

The scraper stores messages as JSON:

```json
{
    "message_id": 97,
    "channel_name": "CheMed123",
    "message_text": "...",
    "message_date": "...",
    "views": 1412,
    "forwards": 2
}
```

YOLO detection outputs processed images with detected objects.

---

# Future Improvements

- PostgreSQL database integration
- dbt transformation models
- Dagster orchestration
- Docker deployment
- Automated scheduling
- Data warehouse star schema

---

# Challenges Encountered

- Docker was unavailable on the development environment.
- PostgreSQL server was not installed locally during implementation.
- Telegram channel availability varied, requiring validation of public channel usernames.

Despite these limitations, the complete scraping pipeline, image processing, and API services were successfully implemented.

---

# Author

**Frida N.**

10 Academy — Week 8 Data Engineering Challenge

GitHub Repository:

https://github.com/Viv-la/medical-telegram-warehouse