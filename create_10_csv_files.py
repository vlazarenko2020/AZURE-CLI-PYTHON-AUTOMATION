import csv
import random
from datetime import datetime, timedelta

# Sample pools for generating realistic data
FIRST_NAMES = ["Alex", "Jordan", "Taylor", "Morgan", "Sam", "Chris", "Pat", "Casey", "Riley", "Jamie"]
LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
TITLES = ["Software Engineer", "Data Analyst", "Product Manager", "UX Designer", "DevOps Engineer", "QA Tester", "System Administrator"]

local_output_folder = "input_csv_files"

def random_dob():
    """Generates a random birth date for ages roughly between 22 and 60."""
    start_date = datetime(1965, 1, 1)
    end_date = datetime(2003, 1, 1)
    days_between = (end_date - start_date).days
    random_days = random.randint(0, days_between)
    return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

def generate_csv_files(num_files=10, rows_per_file=100):
    fieldnames = ["id", "fist_name", "last_name", "DOB", "title", "salary"]
    global_id = 1  # Continuous unique ID across files

    for file_num in range(1, num_files + 1):
        filename = f"{local_output_folder}/data_part_{file_num:02d}.csv"
        
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for _ in range(rows_per_file):
                writer.writerow({
                    "id": global_id,
                    "fist_name": random.choice(FIRST_NAMES),
                    "last_name": random.choice(LAST_NAMES),
                    "DOB": random_dob(),
                    "title": random.choice(TITLES),
                    "salary": random.randint(55000, 145000)
                })
                global_id += 1

        print(f"Generated: {filename}")

if __name__ == "__main__":
    generate_csv_files()

