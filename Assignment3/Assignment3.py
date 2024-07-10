from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open IMDb website
    driver.get("https://www.imdb.com/")

    # Click on the menu to expand
    menu_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="imdbHeader-navDrawerOpen"]/span'))
    )
    menu_button.click()

    # Click on India Movie Spotlight
    india_movie_spotlight = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="imdbHeader"]/div[2]/aside[1]/div/div[2]/div/div[1]/span/div/div/ul/a[8]/span'))
    )
    india_movie_spotlight.click()

    # Click on Trending
    trending_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div[3]/div[2]/div/div[2]/ul/a[3]/span'))
    )
    trending_link.click()

    # Click on the menu again to ensure navigation is clear
    menu_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="imdbHeader-navDrawerOpen"]/span'))
    )
    menu_button.click()

    # Click on Showtimes & Tickets
    showtimes_and_tickets = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="imdbHeader"]/div[2]/aside[1]/div/div[2]/div/div[1]/span/div/div/ul/a[6]/span'))
    )
    showtimes_and_tickets.click()

    # Click on Galaxy Cinemas Waterloo
    galaxy_cinemas_waterloo = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@href="/showtimes/cinema/US/ci0961554?ref_=sh_ov_th"]'))
    )
    galaxy_cinemas_waterloo.click()

    # Click on the 2:10 pm showtime
    showtime = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@href="https://atomtickets.com/checkout/redirect?ref=imdb&venueId=7941&productionDetails=328226&localShowtime=2024-07-09T14:10"]'))
    )
    showtime.click()

    # Wait for 1 minute before exiting
    time.sleep(60)

finally:
    # Close the browser window
    driver.quit()
