from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
import time


def scroll_and_click(driver):
    scroll_pause_time = 3
    last_height = driver.execute_script("return document.body.scrollHeight")
    retry_count = 0

    while True:
        # Scroll down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)

        # Try to click "Load more results" button
        try:
            button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[.//span[text()='Load more results']]")
                )
            )
            if button.is_displayed():
                driver.execute_script("arguments[0].click();", button)
                print(" Clicked 'Load more results'")
                time.sleep(scroll_pause_time)
        except:
            retry_count += 1
            print(" No 'Load more results' button or already clicked.")
            if retry_count >= 3:
                break

        # Check scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def web_scrapper(link, file_name):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(
        ""
    )

    driver = webdriver.Chrome(options=options)
    driver.get(link)

    print(" Scrolling page and loading more hotels ...")
    scroll_and_click(driver)

    print(" Finished scrolling. Parsing data ...")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    hotel_divs = soup.find_all("div", {"data-testid": "property-card"})
    print(f" Hotels found: {len(hotel_divs)}")

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

                price_tag = hotel_div.find(
                    "span", class_="b87c397a13 f2f358d1de ab607752a2"
                )
                price = (
                    price_tag.text.replace("EGP\xa0", "").strip() if price_tag else ""
                )

                rating_tag = hotel_div.find(
                    "div", class_="f63b14ab7a f546354b44 becbee2f63"
                )
                rating = rating_tag.text.strip() if rating_tag else ""

                score_tag = hotel_div.find("div", class_="f63b14ab7a dff2e52086")
                score = score_tag.text.strip() if score_tag else ""

                review_tag = hotel_div.find(
                    "div", class_="fff1944c52 fb14de7f14 eaa8455879"
                )
                review = review_tag.text.strip() if review_tag else ""

                link_tag = hotel_div.find("a", href=True)
                link = link_tag["href"] if link_tag else ""

                writer.writerow(
                    [hotel_name, address, price, rating, score, review, link]
                )

            except Exception as e:
                print(f" Error in hotel parsing: {e}")


if __name__ == "__main__":
    url = input("Enter Booking URL: ").strip()
    fn = input("CSV file name: ").strip()
    web_scrapper(url, fn)

