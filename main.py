from cloudflare_bypass import initialize_driver
from login import login_to_site
from job_scraper import extract_job_data
from csv_saver import save_to_csv

def main():
    url = "https://www.indeed.com"
    
    # Initialize the driver
    driver = initialize_driver()

    try:
        # Step 1: Login or handle Cloudflare
        login_to_site(driver, url)
        
        # Step 2: Perform job search (modify the logic if needed)
        search_job = driver.find_element(By.ID, "text-input-what")
        search_job.send_keys("Data Engineer")

        search_location = driver.find_element(By.ID, "text-input-where")
        search_location.clear()
        search_location.send_keys("New York, NY")
        search_location.send_keys("\n")  # Press Enter to search

        # Wait for the results page to load
        driver.implicitly_wait(10)
        
        # Step 3: Extract job data
        job_data = extract_job_data(driver)

        # Step 4: Save job data to a CSV file
        save_to_csv(job_data)

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        print("Closing the browser...")
        driver.quit()

if __name__ == "__main__":
    main()





# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from seleniumbase import Driver  
# import time

# # Set up Chrome options
# chrome_options = Options()
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-infobars")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument(r"--user-data-dir=C:\Users\user\AppData\Local\Google\Chrome\User Data")  # Adjust this
# chrome_options.add_argument(r"--profile-directory=Profile 4")  # Adjust profile as needed

# # Initialize SeleniumBase Driver for Cloudflare bypass
# driver = Driver(uc=True)  # Enable undetected mode for bypassing Cloudflare.

# try:
#     print("Navigating to Indeed...")
#     url = 'https://www.indeed.com'
#     driver.get(url)  # Open the URL
#     driver.uc_gui_click_captcha()  # Handle Cloudflare CAPTCHA if present
#     time.sleep(5)  # Wait for the page to load after CAPTCHA

#     print("Filling out the job search fields...")
#     # Enter the job position
#     what_elem = driver.find_element(By.ID, 'text-input-what')
#     what_elem.send_keys('Data engineer')
#     time.sleep(2)

#     # Enter the location
#     where_elem = driver.find_element(By.ID, 'text-input-where')
#     where_elem.clear()  # Clear the location field
#     where_elem.send_keys('USA')
#     where_elem.send_keys(Keys.ENTER)  # Submit the form

#     print("Job search initiated. Waiting for results...")
#     time.sleep(10)  # Wait for the results page to load

# except Exception as e:
#     print(f"An error occurred: {e}")

# finally:
#     print("Closing the browser...")
#     time.sleep(60)
#     driver.quit()










