# Booking.com_scraping_using_BeautifulSoup
Web Scraping 5-Star Hotels in Cairo 🏨
This project is a Python script that scrapes data about 5-star hotels in Cairo from Booking.com. It uses Selenium for dynamic page interaction and BeautifulSoup for HTML parsing, then saves the extracted data into a CSV file for further analysis.
📜 Project Overview
The script automates the process of collecting hotel data by:

Navigating to a Booking.com URL provided by the user.
Scrolling the page and clicking "Load more results" to fetch all hotels.
Extracting details like hotel name, location, price, rating, reviews, and booking link.
Saving the data into a CSV file in a structured format.

🛠️ Features

Dynamic Scrolling: Handles infinite scrolling on Booking.com using Selenium to load all hotels.
Headless Browser: Runs Chrome in headless mode (no visible browser window) for efficiency.
Error Handling: Includes try-except blocks to manage parsing errors gracefully.
Structured Output: Saves data in a CSV file with columns: Hotel Name, Locality, Price, Rating, Review, and Link.

📋 Requirements
To run this script, you need to install the following Python libraries and dependencies:

Python 3.x
Selenium: For browser automation.
BeautifulSoup (bs4): For HTML parsing.
Chrome WebDriver: Required for Selenium to control Chrome.
csv: Built-in Python module for CSV file handling.
time: Built-in Python module for adding delays.

Install the required libraries using pip:
pip install selenium bs4

Chrome WebDriver Setup

Download the Chrome WebDriver compatible with your Chrome browser version from here.
Place the chromedriver executable in your system PATH or in the same directory as your script.

🚀 How It Works
1. Imports and Setup
The script starts by importing necessary libraries:

selenium for browser automation.
BeautifulSoup from bs4 for parsing HTML.
csv for saving data to a CSV file.
time for adding delays during scrolling.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
import time

2. Scrolling Function (scroll_and_click)
This function handles dynamic scrolling and clicking the "Load more results" button on Booking.com:

Scrolls the page to the bottom using JavaScript (window.scrollTo).
Waits for the "Load more results" button using WebDriverWait.
Clicks the button if found, or retries up to 3 times before breaking.
Compares the page height to detect if all content is loaded.

def scroll_and_click(driver):
    scroll_pause_time = 3
    last_height = driver.execute_script("return document.body.scrollHeight")
    retry_count = 0

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)

        try:
            button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[.//span[text()='Load more results']]")
                )
            )
            if button.is_displayed():
                driver.execute_script("arguments[0].click();", button)
                print("🔘 Clicked 'Load more results'")
                time.sleep(scroll_pause_time)
        except:
            retry_count += 1
            print("❌ No 'Load more results' button or already clicked.")
            if retry_count >= 3:
                break

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

3. Main Scraping Function (web_scrapper)
This function orchestrates the scraping process:

Sets up Chrome in headless mode with specific options (e.g., --no-sandbox, custom user-agent).
Navigates to the provided Booking.com URL.
Calls scroll_and_click to load all hotels.
Uses BeautifulSoup to parse the page source and extract hotel data.
Saves the data to a CSV file.

Extracted Data:

Hotel Name
Locality (Address)
Price (in EGP, cleaned from extra characters)
Rating
Review Score
Review Text
Booking Link

def web_scrapper(link, file_name):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=options)
    driver.get(link)

    print("🌀 Scrolling page and loading more hotels ...")
    scroll_and_click(driver)

    print("✅ Finished scrolling. Parsing data ...")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    hotel_divs = soup.find_all("div", {"data-testid": "property-card"})
    print(f"🏨 Hotels found: {len(hotel_divs)}")

    with open(
        f"D:\Projects_DS\Cv_Projects\project_2_webscraping(Booking)\{file_name}.csv",
        mode="w",
        encoding="utf-8-sig",
        newline="",
    ) as file:
        writer = csv.writer(file)
        writer.writerow(["Hotel Name", "Locality", "Price", "Rating", "Review", "Link"])

        for hotel_div in hotel_divs:
            try:
                hotel_name_tag = hotel_div.find("div", class_="b87c397a13 a3e0b4ffd1")
                hotel_name = hotel_name_tag.text.strip() if hotel_name_tag else ""

                address_tag = hotel_div.find("span", class_="d823fbbeed f9b3563dd4")
                address = address_tag.text.strip() if address_tag else ""

                price_tag = hotel_div.find("span", class_="b87c397a13 f2f358d1de ab607752a2")
                price = price_tag.text.replace("EGP\xa0", "").strip() if price_tag else ""

                rating_tag = hotel_div.find("div", class_="f63b14ab7a f546354b44 becbee2f63")
                rating = rating_tag.text.strip() if rating_tag else ""

                score_tag = hotel_div.find("div", class_="f63b14ab7a dff2e52086")
                score = score_tag.text.strip() if score_tag else ""

                review_tag = hotel_div.find("div", class_="fff1944c52 fb14de7f14 eaa8455879")
                review = review_tag.text.strip() if review_tag else ""

                link_tag = hotel_div.find("a", href=True)
                link = link_tag["href"] if link_tag else ""

                writer.writerow([hotel_name, address, price, rating, score, review, link])
            except Exception as e:
                print(f"⚠️ Error in hotel parsing: {e}")

4. Main Execution
The script prompts the user for the Booking.com URL and the desired CSV file name, then calls the web_scrapper function.
if __name__ == "__main__":
    url = input("Enter Booking URL: ").strip()
    fn = input("CSV file name: ").strip()
    web_scrapper(url, fn)

📦 Usage

Clone the repository:
git clone <repository-url>
cd <repository-name>


Install dependencies:
pip install -r requirements.txt


Run the script:
python web_scraper.py


Provide inputs:

Enter the Booking.com URL (e.g., a search page for 5-star hotels in Cairo).
Enter the desired CSV file name (e.g., cairo_hotels).


Output:

The script will save the scraped data into a CSV file at the specified path (e.g., D:\Projects_DS\Cv_Projects\project_2_webscraping(Booking)\cairo_hotels.csv).



📝 Notes

File Path: Update the file path in the web_scrapper function (D:\Projects_DS\...) to match your local directory.
Dynamic Classes: Booking.com may change HTML class names over time. If the script fails, inspect the page and update the class names in the find methods.
Rate Limiting: Be cautious of Booking.com’s scraping policies to avoid being blocked. Adding delays (time.sleep) can help.

📈 Potential Improvements

Add support for scraping additional hotel details (e.g., amenities, distance from landmarks).
Implement multi-threading for faster scraping of multiple pages.
Add a configuration file for customizable scraping options (e.g., output path, scroll delay).

🤝 Contributing
Feel free to fork this repository, make improvements, and submit a pull request! If you encounter any issues, please open an issue on GitHub.
📧 Contact
For questions or feedback, reach out via GitHub Issues.

Happy Scraping! 🚀
