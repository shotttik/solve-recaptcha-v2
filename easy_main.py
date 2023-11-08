# Import the required modules
import tempfile
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
import os
import whisper
import warnings
from selenium.webdriver.chrome.service import Service


def transcribe(url) -> str:
    # Suppress warnings
    warnings.filterwarnings("ignore")

    # Load the Whisper model
    MODEL = whisper.load_model("base")

    # Create a temporary file to store the audio content
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        # Write the content from the URL to the temporary file
        temp_file.write(requests.get(url).content)
        temp_file_name = temp_file.name

    # Transcribe the audio using the Whisper model
    result = MODEL.transcribe(temp_file_name)

    # Clean up the temporary file
    os.remove(temp_file_name)

    # Return the transcribed text
    return result["text"].strip()


def request_audio(driver):
    # Switch to the reCAPTCHA iframe and click the checkbox
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(
        By.XPATH, ".//iframe[@title='reCAPTCHA']"))
    driver.find_element(By.ID, "recaptcha-anchor-label").click()
    driver.switch_to.default_content()

    time.sleep(1)
    # Switch to the recaptcha challenge iframe and request the audio version
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(
        By.XPATH, ".//iframe[@title='recaptcha challenge expires in two minutes']"))
    driver.find_element(By.ID, "recaptcha-audio-button").click()


def solve_captcha(driver):
    # Transcribe and enter the audio text, then verify the CAPTCHA
    text = transcribe(driver.find_element(
        By.ID, "audio-source").get_attribute('src'))
    driver.find_element(By.ID, "audio-response").send_keys(text)
    driver.find_element(By.ID, "recaptcha-verify-button").click()
    time.sleep(1)
    driver.switch_to.default_content()
    driver.find_element(
        By.XPATH, "//input[@id='recaptcha-demo-submit']").click()


if __name__ == "__main__":
    # Initialize the Chrome webdriver
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()))

    # Open the reCAPTCHA demo page
    driver.get("https://www.google.com/recaptcha/api2/demo")

    request_audio(driver)
    time.sleep(1)

    # Solve the audio CAPTCHA
    solve_captcha(driver)

    # Print a success message
    print("Captcha solved!")

    # Wait for 10 seconds (you can adjust this as needed)
    time.sleep(10)
