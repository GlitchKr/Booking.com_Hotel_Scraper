# Booking.com Hotel Scraper 🏨

## Overview
A Python script to scrape 5-star hotels in Cairo from Booking.com, extracting details like hotel name, location, price, rating, reviews, and link, then saving them to a CSV file.

## Functionality
- Takes a Booking.com URL and CSV file name as input
- Scrolls the page to load all hotels
- Extracts hotel data and saves it to a CSV with columns: 
  - Hotel Name
  - Locality
  - Price
  - Rating
  - Review
  - Link

## How It Works
- **Selenium**: Handles scrolling and loading more results in headless mode
- **BeautifulSoup**: Parses HTML to extract hotel info
- **CSV**: Saves the data in a structured format

## Requirements
- Python 3.x
- Install dependencies: 
  ```bash
  pip install selenium bs4
