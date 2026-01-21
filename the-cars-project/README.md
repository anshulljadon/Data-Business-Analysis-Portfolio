Cars Market Analysis Dashboard


A comprehensive data analysis and interactive dashboard for used car market insights built with Python, Pandas, and Streamlit.

📋 Project Overview
This project analyzes a dataset of 5,961+ used cars across Indian cities, providing:

Data Cleaning & EDA:
Comprehensive exploratory data analysis in Jupyter Notebook

Interactive Dashboard:
Streamlit-based web app for business insights

Market Insights:
Price trends, brand comparisons, and feature analysis


📁 Project Structure
the-cars-project/
├── app.py                      # Streamlit web application
├── cars-project.ipynb          # Jupyter notebook with EDA
├── Cars.csv                    # Dataset (5,961 records)
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── tempCodeRunnerFile.py


📊 Dataset Overview
File: Cars.csv
Records: 5,961 used cars

Features (15 columns):

Car Info: Name, Company_Name, Model_Name
Location & Time: Location, Year
Technical: Fuel_Type, Transmission, Engine, Power, Mileage
Condition: Kilometers_Driven, Owner_Type, Seats, No. of Doors, Colour
Pricing: Price, New_Price

Data Sample:
Mahindra Scorpio,Pune,2012,99000,Diesel,Manual,Third,12.05 kmpl,2179 CC,120 bhp,Black/Silver,8,5,,6
Maruti Baleno,Kochi,2018,18678,Petrol,Manual,First,21.1 kmpl,998 CC,100 bhp,Others,5,4,,8.32

🔍 Key Analysis Findings

Data Quality
Missing Values: New_Price (86.2% missing) → Dropped for analysis
Outliers Present: Kilometers_Driven, Power_Value, Engine_Value → Filled with median
Data Types: Mix of numerical (5 cols) and categorical (10 cols)

Market Insights

Price Range: ₹0.44 Cr to ₹160 Cr (Mean: ₹9.53 Cr)
Popular Brands: Maruti, Hyundai, Mahindra dominate
Transmission: Manual cars outnumber automatic significantly
Fuel Type: Diesel & Petrol equally preferred
Prime Locations: Delhi, Bangalore, Pune, Mumbai, Hyderabad


🚀 Getting Started
Prerequisites
Python 3.7+
pip package manager
Installation
Clone the repository

Install dependencies

View the requirements

📈 Running the Project
Option 1: Interactive Dashboard (Recommended)
Access the dashboard at: http://localhost:8501

Option 2: Jupyter Notebook Analysis
🎯 Dashboard Features

📊 Tab 1: Overview (KPIs)
Average Price
Average Kilometers Driven
Most Common Fuel Type
Average Engine Power

📈 Tab 2: Trends
Price trends by year
Mileage & kilometers trends
Year-over-year analysis

🏭 Tab 3: Comparison
Company-wise pricing
Fuel type comparison
Transmission impact on price

📁 Tab 4: Data Preview
View filtered dataset
Download filtered data as CSV

🎛️ Filters
Location: Select specific cities
Company: Filter by car manufacturer
Fuel Type: Petrol, Diesel, CNG, LPG
Transmission: Manual or Automatic
Year Range: Custom date range selector

🛠️ Technologies Used
Component	Technology
Data Processing	Pandas, NumPy
Visualization	Matplotlib, Seaborn
Web Dashboard	Streamlit
Data Analysis	Jupyter Notebook
Language	Python 3


📊 Notebook Contents
cars-project.ipynb includes:

Data Loading & Info: Structure and types
Missing Value Analysis: Identification and treatment
Statistical Summary: Descriptive statistics
Univariate Analysis: Distribution of each feature
Bivariate Analysis: Relationships between features
Data Preprocessing: Cleaning and transformation
Insights & Conclusions: Key findings
📈 Key Insights
Price Determinants
Engine power strongly correlates with price
Newer cars command premium pricing
Automatic transmission increases price
Lower mileage associated with higher prices
Market Trends
Diesel cars: Better fuel efficiency, popular for commercial use
Metropolitan cities: Higher average prices
First owners: Majority of dataset
5-seater vehicles: Most common
💡 Use Cases
Price Prediction: Build ML models using this dataset
Market Research: Understand used car pricing dynamics
Business Intelligence: Dealership pricing strategies
Data Portfolio: Demonstrate data analysis skills
🎓 Learning Outcomes
This project demonstrates:

✅ Data cleaning & preprocessing
✅ Exploratory Data Analysis (EDA)
✅ Statistical analysis
✅ Data visualization
✅ Building interactive dashboards
✅ Business insights generation
📝 Notes
New_Price Column: Contains 86.2% missing values (not used)
Outliers: Identified using boxplots; handled with median imputation
Data Freshness: Dataset appears to be from 2019 and earlier
🔗 Files Reference
File	Purpose
app.py	Streamlit dashboard application
cars-project.ipynb	Complete EDA & analysis
Cars.csv	Raw dataset
requirements.txt	Python dependencies





👤 Author

Anshul

📚 MBA (Finance & Marketing) | Aspiring Data Analyst
🔹 Tools: Python, Pandas, NumPy, Seaborn, Streamlit
🔹 Focus: Business insights, clean code, professional dashboards