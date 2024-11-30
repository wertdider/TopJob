from selenium.webdriver.common.by import By

def extract_job_data(driver):
    job_data = []

    print("Extracting job listings...")
    # Locate all job containers
    job_containers = driver.find_elements(By.CSS_SELECTOR, "div.slider_container")

    if not job_containers:
        print("No job listings found.")
    else:
        for job in job_containers:
            try:
                # Extract job details
                job_title = job.find_element(By.CSS_SELECTOR, "h2.jobTitle").text
                company_name = job.find_element(By.CSS_SELECTOR, "span.companyName").text
                location = job.find_element(By.CSS_SELECTOR, "div.companyLocation").text

                print(f"Job Found: {job_title} at {company_name} in {location}")
                job_data.append([job_title, company_name, location])
            except Exception as e:
                print(f"Error extracting job details: {e}")
    
    return job_data