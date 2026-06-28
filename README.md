# Medical Telegram Data Warehouse

## Project Overview

This project builds an end-to-end ELT pipeline for Ethiopian medical Telegram channels. The pipeline extracts messages and images from public Telegram channels, stores raw data in JSON format, performs object detection using YOLOv8, and exposes the data through a FastAPI service.

---

## Project Structure

```
medical-telegram-warehouse/
│
├── api/
├── data/
│   ├── raw/
│   ├── processed/
│
├── src/
├── tests/
├── logs/
├── notebooks/
└── README.md
```

---

## Technologies Used

- Python
- Telethon
- FastAPI
- YOLOv8 (Ultralytics)
- SQLAlchemy
- PostgreSQL (loader prepared)
- Docker (configuration prepared)

---

## Features

- Scrape multiple Telegram medical channels
- Store raw JSON messages
- Download media/images
- YOLO object detection
- REST API for accessing scraped data

---

## API Endpoints

- `/`
- `/docs`
- `/messages/{channel}`

---

## Sample Channels

- CheMed123
- lobeliacosmetics
- TIKVAHh

---

## Running the Project

```bash
pip install -r requirements.txt

python src/scraper.py

python src/yolo_detect.py

uvicorn api.main:app --reload
```

---

## Results

- Successfully scraped Telegram messages.
- Saved structured JSON files.
- Downloaded channel images.
- Performed object detection using YOLOv8.
- Exposed data through FastAPI.

---

## Future Improvements

- PostgreSQL integration
- dbt transformations
- Dagster orchestration
- Docker deployment