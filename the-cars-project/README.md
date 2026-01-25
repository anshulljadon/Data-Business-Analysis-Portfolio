# Cars Data Analysis Dashboard

Author: Anshul Jadon
    Tech Stack:

        · Python 
        · Pandas 
        · Streamlit 
        · Matplotlib 
        · Seaborn

# Project Overview

    This project is an interactive Streamlit dashboard built to analyze the Indian used car market.
    It helps users explore pricing patterns, car features, and relationships between variables through filters, visualizations, and statistical summaries.

    The focus of this project is practical data analysis and decision support, not just visuals.

# Quick Start
    1️ Install Dependencies
    pip install -r requirements.txt

    2️ Run the Application
    streamlit run streamlit_app.py

    3️ Open in Browser
    http://localhost:8501

# Application Pages

    Overview
        High-level metrics, dataset preview, and key insights

    Analysis
         Visualizations for price, mileage, engine size, and fuel type

    Filters
        Interactive filters by price range, fuel type, transmission, and location

    Stats
        Statistical summaries and correlations for numeric features

# Key Features

    *  Interactive filtering and search
    *  Download filtered data as CSV
    *  Distribution plots and correlation analysis
    *  Descriptive statistical analysis
    *  Clean, beginner-friendly UI
    *  Real-world dataset with business relevance

#  Project Structure
    cars-dashboard/
    │
    ├── streamlit_app.py      # Main Streamlit application
    ├── app.py                # Data loading and preprocessing
    ├── Cars.csv              # Dataset (5,961 records)
    ├── cars-project.ipynb    # Exploratory data analysis notebook
    ├── requirements.txt      # Project dependencies
    └── README.md             # Project documentation

📊 Dataset Information

    * Source: Indian used car listings
     
    * Records: 5,961 cars

    * Key Features:

          --  Price
          --  Manufacturing Year
          --  Mileage
          --  Engine Capacity
          --  Fuel Type
          -- Transmission
          --  Location

# Project Objective

The goal of this project is to:

    Practice end-to-end data analysis
    Build business-focused dashboards
    Translate raw data into actionable insights
    Demonstrate real-world data science skills using Streamlit

# Conclusion

This dashboard demonstrates how simple analysis and clear visualization can provide valuable insights from messy real-world data.
