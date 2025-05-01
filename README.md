Booking.com Hotel Scraper 🏨

Overview

This Python script scrapes 5-star hotels in Cairo from Booking.com. It grabs details like hotel name, location, price, rating, reviews, and link, then saves them to a CSV file.

What It Does





Takes a Booking.com URL and CSV file name as input.



Scrolls the page to load all hotels.



Extracts hotel data and saves it to a CSV.

How I Built It





Used Selenium to handle scrolling and load more results in headless mode.



Used BeautifulSoup to parse HTML and extract hotel info.



Saved data to CSV with columns: Hotel Name, Locality, Price, Rating, Review, Link.

Requirements





Python 3.x



Install: pip install selenium bs4



Chrome WebDriver (add to PATH)

Usage





Clone repo: git clone <repo-url>



Run: python script.py



Enter Booking URL and CSV file name.



Check the CSV file in your directory.

Notes





Update the file path in the script.



Booking.com classes may change; update if needed.
