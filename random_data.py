import json
import random
from faker import Faker
from datetime import datetime

# Number of test accounts to generate
number_of_accounts = 30

# Initialize the Faker generator
fake = Faker()

# Get the current date in YYYY-MM-DD format
current_date = datetime.now().strftime("%Y-%m-%d")


def generate_random_account():
    email = f"Test account, {current_date}@remitly.com"
    username = fake.user_name()
    password = fake.password()

    return {
        "email": email,
        "username": username,
        "password": password,
    }


# Generate random test accounts
test_accounts = [generate_random_account() for _ in range(number_of_accounts)]

# Write the test accounts to a JSON file
output_file_name = "test-accounts.json"
with open(output_file_name, "w") as json_file:
    json.dump(test_accounts, json_file, indent=2)

print(f"Generated {number_of_accounts} test accounts and saved them to {output_file_name}")
