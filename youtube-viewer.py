import time
import random
import logging
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent

# Logging
log_dir = "./logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Full video URL
video_urls = []

random.shuffle(video_urls)
ua = UserAgent()
user_agent = ua.random

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--mute-audio")
chrome_options.add_argument(f"user-agent={user_agent}")

driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)
logging.info(f"Initialized ChromeDriver at {driver_path}")

def play_videos():
    for url in video_urls:
        video_id = url.split('=')[1]
        logging.info(f"{video_id}: Init")
        driver.get(url)
        time.sleep(5)  

        try:
            play_button = driver.find_element(
                By.CSS_SELECTOR, 'button.ytp-large-play-button')
            ActionChains(driver).move_to_element(play_button).click().perform()
            logging.info(f"{video_id}: Start")
        except Exception as e:
            logging.info(f"{video_id}: Play button not found or already playing - {str(e)}")

        # Customize the viewing time
        view_time = random.randint(70, 540)
        logging.info(f"{video_id}: Viewing for {view_time} seconds")

        start_time = time.time()
        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time

            if elapsed_time >= view_time:
                logging.info(f"{video_id}: Next")
                break

            try:
                skip_button = driver.find_element(
                    By.CSS_SELECTOR, 'button.ytp-ad-skip-button')
                ActionChains(driver).move_to_element(
                    skip_button).click().perform()
                logging.info(f"{video_id}: SkipAd")
            except Exception as e:
                pass

            time.sleep(3)

try:
    play_videos()
    logging.info(f"Playlist ended")
except KeyboardInterrupt:
    logging.info(f"KeyboardInterrupt detected")
except Exception as e:
    logging.error(f"Unexpected error: {e}")
finally:
    driver.quit()
    logging.info(f"Driver quit")

time.sleep(3)
