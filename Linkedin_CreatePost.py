import subprocess  # For running subprocesses (like installing packages)
import sys  # For system-specific parameters and functions
from selenium import webdriver  # Importing the WebDriver for browser automation
from selenium.webdriver.common.by import By  # For locating elements on the page
from selenium.webdriver.chrome.service import Service  # For managing ChromeDriver service
from selenium.webdriver.chrome.options import Options  # For setting Chrome options
import time  # For adding delays

# ANSI escape code for green text
GREEN = "\033[92m"  # Code to set text color to green
RESET = "\033[0m"  # Code to reset text color to default

# Before running the script, in terminal type - "pip install selenium" and Click - "Enter"
# After installing, click on Run/ctrl+f5

try:
    from selenium import webdriver  # Attempt to import WebDriver
    from selenium.webdriver.common.by import By  # Attempt to import By for element location
    from selenium.webdriver.common.keys import Keys  # Attempt to import Keys for keyboard actions

except ImportError:  # If the import fails
    print("Selenium is not installed. Installing now...")  # Notify user about installation
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'selenium'])  # Install Selenium
    print("Selenium has been installed. Please rerun the script.")  # Notify user to rerun the script
    exit(1)  # Exit the script after installation

# Use abc LinkedIn ID only as of now
LINKEDIN_EMAIL = 'abc123alphanumeric@gmail.com'  # Placeholder for LinkedIn email
LINKEDIN_PASSWORD = 'abc123alphanumeric@'  # Placeholder for LinkedIn password

# Set up Chrome options for incognito mode
chrome_options = Options()  # Create an instance of Options
chrome_options.add_argument("--incognito")  # Add argument to open Chrome in incognito mode

# Set up the WebDriver with Chrome options
driver = webdriver.Chrome(options=chrome_options)  # Initialize Chrome WebDriver with specified options

try:
    # Navigate to the LinkedIn login page
    driver.get("https://www.linkedin.com/login")  # Open LinkedIn login page
    driver.maximize_window()  # Maximize the browser window
    time.sleep(5)  # Wait for 5 seconds for the page to load

    # Find the email field and enter your email
    email_field = driver.find_element(By.ID, "username")  # Locate the email input field by ID
    email_field.send_keys(LINKEDIN_EMAIL)  # Enter the email into the field
    time.sleep(2)  # Wait for 2 seconds

    # Find the password field and enter your password
    password_field = driver.find_element(By.ID, "password")  # Locate the password input field by ID
    password_field.send_keys(LINKEDIN_PASSWORD)  # Enter the password into the field
    time.sleep(2)  # Wait for 2 seconds  

    # Find the login button
    login = driver.find_element(By.XPATH, "//button[@type='submit']")  # Locate the login button using XPath

    # Scroll the login button into view
    driver.execute_script("arguments[0].scrollIntoView(true);", login)  # Scroll the button into view using JavaScript
    time.sleep(1)  # Optional: wait a moment after scrolling

    login.click()  # Click the login button
    # Wait for the page to load
    time.sleep(10)  # Wait for 10 seconds for the page to load

    # Check if login was successful by looking for a specific element on the homepage
    if "feed" in driver.current_url:  # Check if "feed" is in the current URL
        print(f"{GREEN}Login successful!{RESET}")  # Print success message in green color
    time.sleep(2)  # Wait for 2 seconds 

finally:
    # Close the browser
    driver.quit()  # Ensure the browser is closed at the end of the script