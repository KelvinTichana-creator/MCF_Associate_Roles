# MasterCard Foundation Associate Roles Applications Cleaner

Author: Kelvin Carrington Tichana

## Overview

The MasterCard Foundation Associate Roles Applications Cleaner is a Streamlit web application designed to clean and analyze Excel spreadsheet data related to job applications. This app performs data cleaning tasks and provides basic statistics on age, gender, and country data within the uploaded Excel file.

## Features

- Data cleaning: Filters and cleans the Excel data based on specific criteria.
- Basic statistics: Calculates and displays statistics on age, gender, and country columns.
- Data download: Allows users to download the cleaned data as an Excel file.

## Usage

1. Clone the repository to your local machine:

git clone https://github.com/KelvinTichana-creator/MCF_Associate_Roles.git

2. Install the required Python packages:

pip install streamlit pandas matplotlib seaborn

3. Run the Streamlit app:

streamlit run clean.py

4. Access the app in your web browser at the provided URL (typically, http://localhost:8501).

Upload an Excel file containing the job application data.

Review the cleaned data, basic statistics, and download the cleaned data.

## App Structure

1. clean.py: The main Streamlit app script.

2. requirements.txt: Lists the required Python packages.

## Data Cleaning

1. The app filters rows where a specified column ("Have you completed school already or will you have completed school by 30th September 2023?") is "Yes".

2. Rows with empty values in a specified column (column AP) are removed.

## Statistics

1. Basic statistics are displayed for the following columns (if present in the data):

	Age: Displays descriptive statistics (mean, median, min, max, etc.) and a histogram plot.

	Gender: Displays the count of each gender category.

	Country of Origin: Displays the count of applicants from each country.

## Data Download

The cleaned data can be downloaded as an Excel file using the provided download link.

## Author

Kelvin Carrington Tichana


