
# Collaborative Development of CSV Explorer Web App

<<<<<<< HEAD
<<<<<<< HEAD
## Authors
Group Members:

- Fatemeh Elyasifar (25589351) 
- Krishnan Unni Prasad (25225362) 
- Prisa Senduangdeth (25402088) 

## Description
=======
>>>>>>> 349ed9d3622a7e8fb9253f838dba875a77cbd56f
=======
>>>>>>> origin/main
CSV Explorer is a Streamlit-based application built for data scientists, analysts, and anyone who needs a quick, interactive exploration tool for CSV datasets. This app allows users to upload a CSV file and access data insights through separate tabs for DataFrames, Numeric Series, Text Series, and Date Series. Each tab is designed to perform unique analyses on its respective data type, facilitating easy and efficient exploration of the data's characteristics.

### Features:
- **DataFrame Tab**: Provides an overview of the entire dataset, allowing users to view and navigate the data.
- **Numeric Serie Tab**: Displays statistics and visualizations for numeric columns, such as mean, median, standard deviation, and distributions.
- **Text Serie Tab**: Analyzes text data, including frequency counts, word clouds, and other text-based insights.
- **Date Serie Tab**: Parses and explores datetime columns, enabling users to extract trends and patterns over time.

## How to Setup

1. **Clone the Repository**: Download or clone this repository to your local machine.
   ```bash
<<<<<<< HEAD
<<<<<<< HEAD
   git clone https://github.com/KrishUnni-Z/dsp_at3_group8.git
   cd dsp_at3_group8
=======
   git clone https://github.com/ftme-lyc/data-exploration-app.git
   cd data-exploration-app
>>>>>>> 349ed9d3622a7e8fb9253f838dba875a77cbd56f
=======
   git clone https://github.com/ftme-lyc/data-exploration-app.git
   cd data-exploration-app
>>>>>>> origin/main
   ```
   
2. **Install Dependencies**: Install the required packages by running the following command:
   ```bash
   pip install -r requirements.txt
   ```

3. **Project Directory Structure**: Confirm that your files are organized as follows:
   ```
   app/
   │
   ├── streamlit_app.py       # Main application script to run the Streamlit app
   │
   ├── tab_df/                # Directory containing DataFrame display and logic functions
   │   ├── display.py
   │   └── logics.py
   │
   ├── tab_date/              # Directory containing Date Series display and logic functions
   │   ├── display.py
   │   └── logics.py
   │
   ├── tab_numeric/           # Directory containing Numeric Series display and logic functions
   │   ├── display.py
   │   └── logics.py
   │
   └── tab_text/              # Directory containing Text Series display and logic functions
       ├── display.py
       └── logics.py
   ```

## How to Run the Program

1. **Launch the Streamlit App**: Navigate to the main directory and execute the following command:
   ```bash
   streamlit run app/streamlit_app.py
   ```
2. **Upload a CSV File**: Open the app in your browser, upload a CSV file, and navigate through the tabs to explore the dataset.

## Project Structure

This project is divided into multiple subdirectories to handle different aspects of the data exploration:

- `streamlit_app.py`: The main script for running the app. It sets up the page layout, session states, and tab structure.
- **tab_df**: Contains logic and display code for the DataFrame tab.
  - `display.py`: Renders DataFrame content in the app.
  - `logics.py`: Contains helper functions for DataFrame operations.
- **tab_numeric**: Includes files for handling numeric series analysis.
  - `display.py`: Provides visualizations and statistics for numeric data.
  - `logics.py`: Contains functions for numeric calculations and transformations.
- **tab_text**: Manages text-based data exploration.
  - `display.py`: Displays text-related insights like word frequency.
  - `logics.py`: Contains text-processing functions.
- **tab_date**: Handles datetime columns.
  - `display.py`: Shows time-series patterns and trends.
  - `logics.py`: Contains functions for parsing and analyzing datetime data.

## Citations

- Streamlit. (2022). Streamlit (Version 1.13.0) [Computer software]. Streamlit, Inc. Available from https://streamlit.io

- McKinney, W. (2023). pandas (Version 2.0.3) [Computer software]. pandas development team. Available from https://pandas.pydata.org

- VanderPlas, J. (2022). Altair: Declarative statistical visualization library (Version 4.2.0) [Computer software]. Available from https://altair-viz.github.io

- Python Software Foundation. (2023). Python Standard Library [Computer software]. Available from https://docs.python.org

<<<<<<< HEAD
<<<<<<< HEAD
---
=======
=======
>>>>>>> origin/main
## Authors
Group Members:

- Fatemeh Elyasifar (25589351) 
- Krishnan Unni Prasad (25225362) 
- Prisa Senduangdeth (25402088) 
<<<<<<< HEAD
>>>>>>> 349ed9d3622a7e8fb9253f838dba875a77cbd56f
=======
>>>>>>> origin/main
