import csv

def save_to_csv(job_data, filename="vacancies.csv"):
    if not job_data:
        print("No data to save.")
        return

    print(f"Saving data to {filename}...")
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company Name", "Location"])
        writer.writerows(job_data)
    print("Data saved successfully.")