# FFXSS - FUZZ FOR CROSS-SITE SCRIPTING
### A python script to fuzz for XSS vulnerabilities. 

### Description:
This script is designed to fuzz websites for Cross-Site Scripting (XSS) vulnerabilities. It uses the Python requests library to send POST requests to the target URL with different input values for specified input fields. The script takes input arguments from the command line using argparse module, such as the target URL, input fields to fuzz, values to use for fuzzing, and characters to use for fuzzing.

The script defines a function generate_random_value() to generate random values for fuzzing. The input fields are looped over, and for each field, the script fuzzes with predefined values, random values, and combinations of predefined values. If a fuzzed value is found in the response text, the script prints a message indicating that an XSS vulnerability has been detected and outputs the vulnerable input field and value. The script finishes after all input fields have been fuzzed.
