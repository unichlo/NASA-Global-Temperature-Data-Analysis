"""nasa_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gov3TgI3M1pGkdI0W1iBwVrYnZPpESyN
"""

import pandas as pd

# Input data file
from google.colab import files
uploaded = files.upload()

from IPython.display import display
import os


# Read data from csv file
def get_data_from_file(fileName):
    with open(fileName, "r") as f:
        lines = f.readlines()
        data = []

        # Skip the header and processing from 2nd line
        for line in lines[1:]:
            split_line = line.strip().split(',')
            Year, No_Smoothing, Lowess = split_line[:3]
            data.append((int(Year), float(No_Smoothing), float(Lowess)))

    return data

# Prompt the user to input the file name
def input_file():
    input_file_name = input("Enter the name of file: ")
    return input_file_name

# Store the input in a variable
file = input_file()

# Display output data
def display_output(output_data):
    print("The Output Data:")
    print(output_data)

# Write the output data to txt file
def write_output_file(output_data):
    output_file = input("Enter the name for the output file: ")

# Calculate the average of a list
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    return average

# Find maximum number in a list
def find_maximum(numbers):
    maximum = 0
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

# Find minimum number in a list
def find_minimum(numbers):
    minimum = 0
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

# Calculate median number in a list
def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        median = sorted_numbers[n//2]
    return median

# Calculate frequency of positive number
def frequency_of_positives(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    return count

# Calculate frequency of negative number
def frequency_of_negatives(numbers):
    count = 0
    for num in numbers:
        if num < 0:
            count += 1
    return count

# Calculate variance which is average of squared deviations from the mean
def calculate_variance(numbers):
    mean = calculate_average(numbers)
    variance = 0
    for num in numbers:
        variance += (num - mean) ** 2
    return variance / len(numbers)


# Calculate standard deviation
def calculate_sd(numbers):
    return (calculate_variance(numbers)) ** 0.5



# Main program
input_data = get_data_from_file(file)
if input_data: # Check if list is not empty
    # Extract No_Smoothing and Lowess data from the input
    no_smoothing_values = [float(row[1]) for row in input_data]
    lowess_values = [float(row[2]) for row in input_data]

    # Function to generate a analysis report
    def generate_report(data, name):
        avg_result = calculate_average(data)
        max_result = find_maximum(data)
        min_result = find_minimum(data)
        median_result = calculate_median(data)
        positive_count = frequency_of_positives(data)
        negative_count = frequency_of_negatives(data)
        variance_result = calculate_variance(data)
        sd_result = calculate_sd(data)

        # Initialize the output_data variable
        output_data = ""

        # Prepare the output data, put the results into a string
        output_data += f"Average of {name}: {avg_result}\n"
        output_data += f"Maximum of {name}: {max_result}\n"
        output_data += f"Minimum of {name}: {min_result}\n"
        output_data += f"Median of {name}: {median_result}\n"
        output_data += f"Number of positive values in {name}: {positive_count}\n"
        output_data += f"Number of negative values in {name}: {negative_count}\n"
        output_data += f"Variance of {name}: {variance_result}\n"
        output_data += f"Standard Deviation of {name}: {sd_result}\n"

        return output_data

# Generate report for 'No_Smoothing' and 'Lowess' data
no_smoothing_report = generate_report(no_smoothing_values, "No_Smoothing")
lowess_report = generate_report(lowess_values, "Lowess")

# Combine both reports
final_report = no_smoothing_report + "\n" + lowess_report

# Display the report
display_output(final_report)
write_output_file(final_report)

# Download the output file
with open('nasa_output.txt', 'w') as output_file:
    output_file.write(final_report)
files.download('nasa_output.txt')