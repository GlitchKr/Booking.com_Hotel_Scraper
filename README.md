# Booking.com Hotel Scraper 🏨

## Overview
A Python script that automatically scrapes 5-star hotels in Cairo from Booking.com, including:
- Hotel name
- Location
- Price
- Rating
- Review count
- Booking link

Saves all data to a CSV file with automatic pagination handling.

## Key Features
✨ **Automatic Pagination Handling**  
- Automatically detects and clicks "Load more results" button
- Scrolls to the bottom of the page to trigger lazy-loaded content
- Stops when no more hotels are loading

⚡ **Headless Browser**  
- Runs in background without GUI (configurable)
- Simulates real user behavior

📊 **Structured Output**  
- Clean CSV format with proper columns
- Handles missing data gracefully

## How It Works
1. **Initialization**:
   - Launches headless Chrome browser
   - Navigates to provided Booking.com URL

2. **Content Loading**:
   - Scrolls to page bottom repeatedly
   - Clicks "Load more results" when available
   - Waits between actions to prevent blocking

3. **Data Extraction**:
   - Parses loaded HTML with BeautifulSoup
   - Extracts hotel details from property cards
   - Handles missing data fields gracefully

4. **Output**:
   - Saves all data to CSV
   - Preserves special characters with UTF-8 encoding

## Requirements
```bash
pip install selenium bs4
