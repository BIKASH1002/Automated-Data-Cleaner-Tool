# DataWiz: An Automated Data Cleaning Tool

# Overview

DataWiz is an intuitive application designed to simplify the tedious process of cleaning and preprocessing datasets. Built with a sleek and modern GUI using CustomTkinter, DataWizard empowers data scientists, analysts and enthusiasts to prepare their data efficiently without writing a single line of code.

# Setup

- Visual Studio Code

- Tkinter and Customtkinter for GUI

# Features

- **User-Friendly Interface:** Navigate through the data cleaning process with an intuitive GUI.

- **Quick Dataset Loading:** Import CSV or Excel files effortlessly.

- **Comprehensive Data Analysis:** View initial dataset statistics at a glance.

- **Flexible Missing Value Handling:**

    - Impute missing values using mean or median.

    - Remove rows with missing data.

- **Robust Outlier Detection:**

    - Detect and handle outliers using IQR or Z-score methods.

- **Data Visualization:**

    - Visualize numerical data distributions with histograms.

    - Explore categorical data with count plots.

- **Easy Data Export:** Save your cleaned dataset in CSV or Excel format.

# Usage

Run main.py

# GUI Walkthrough

The DataWiz GUI is designed for simplicity and efficiency. Below is a step-by-step guide to using the application. (_Refer to the accompanying screenshots for visual guidance._)

**1. Loading a Dataset**

- **Step 1:** Click on the `Load Dataset` button.

<div align = "center">
    <img src="https://github.com/user-attachments/assets/c20c7c1b-347f-40c8-9cd4-7275ff27fb51" alt="1" width="50%">
</div>

- **Step 2:** Select your CSV or Excel file from the file dialog.
  
- **Step 3:** Once loaded, the application displays initial analysis cards showing:

  - Total Rows

  - Rows with Missing Values

  - Duplicate Rows

  - Outliers

<div align = "center">
    <img src="https://github.com/user-attachments/assets/17d79f40-52b5-4562-ba28-e2cd79607a72" alt="1" width="50%">
</div>

**2. Handling Missing Values**

- **Step 4:** In the Cleaned Dataset Analysis section, choose how to handle missing values:

    - Select Impute or Remove from the dropdown.

<div align = "center">
    <img src="https://github.com/user-attachments/assets/67009203-c7d1-41d0-a4c3-f8b57da17a7c" alt="1" width="50%">
</div>

- **Step 5:** If you choose **Impute**, select the imputation method (**mean** or **median**).

**3. Handling Outliers**

- **Step 6:** Choose an outlier detection method:
  
    - IQR: Interquartile Range method.
  
     - Z-score: Standard score method.

<div align = "center">
    <img src="https://github.com/user-attachments/assets/e894dc7c-08d6-4e25-8f08-858889206862" alt="1" width="50%">
</div>

**4. Processing the Data**

- **Step 7:** Click on the `Process Data` button.

 <div align = "center">
    <img src="https://github.com/user-attachments/assets/fa025f71-4819-4c6b-8bf1-aff320a439f6" alt="1" width="50%">
</div> 

- **Step 8:** The application cleans the data based on your selections and displays visualizations:

  - A histogram for numerical data distribution.

    - A count plot for categorical data distribution.

 <div align = "center">
    <img src="https://github.com/user-attachments/assets/3bf44d0b-bf61-4693-8469-7307fcab7c83" alt="1" width="50%">
</div> 

**5. Saving the Cleaned Data**

- **Step 9:** Click on the `Save Cleaned Data` button.

 <div align = "center">
    <img src="https://github.com/user-attachments/assets/0e26b527-ba94-452d-820a-b23bdc501b0a" alt="1" width="50%">
</div> 

- **Step 10:** Choose the destination and file format (CSV or Excel) to save your cleaned dataset.

# Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.
