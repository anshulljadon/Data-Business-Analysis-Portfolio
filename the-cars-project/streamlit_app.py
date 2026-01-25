"""
Cars Dashboard - Simple & Clean
Author: ANSHUL JADON
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ==================== CONFIG ====================
st.set_page_config(page_title="Cars Dashboard", page_icon="🚗", layout="wide")
sns.set_style("whitegrid")

# ==================== LOAD DATA ====================
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('Cars.csv')
        df.drop_duplicates(inplace=True)
        
        # Convert numeric columns first
        df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
        df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
        df['Kilometers_Driven'] = pd.to_numeric(df['Kilometers_Driven'], errors='coerce')
        
        # Feature extraction from string columns
        mileage_split = df['Mileage'].astype(str).str.split(' ', expand=True, n=1)
        df['Mileage_Value'] = pd.to_numeric(mileage_split[0], errors='coerce')
        
        power_split = df['Power'].astype(str).str.split(' ', expand=True, n=1)
        df['Power_Value'] = pd.to_numeric(power_split[0], errors='coerce')
        
        engine_split = df['Engine'].astype(str).str.split(' ', expand=True, n=1)
        df['Engine_Value'] = pd.to_numeric(engine_split[0], errors='coerce')
        
        name_split = df['Name'].astype(str).str.rsplit(n=1, expand=True)
        df['Company_Name'] = name_split[0]
        df['Model_Name'] = name_split[1] if 1 in name_split.columns else ''
        
        # Drop original columns
        df.drop(columns=['Mileage', 'Engine', 'Power', 'Name'], inplace=True)
        if 'New_Price' in df.columns:
            df.drop(columns=['New_Price'], inplace=True)
        
        # Fill missing numeric values with median
        numeric_cols = ['Price', 'Year', 'Kilometers_Driven', 'Mileage_Value', 'Power_Value', 'Engine_Value']
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
                median_val = df[col].median()
                if pd.notna(median_val) and median_val > 0:
                    df[col].fillna(median_val, inplace=True)
        
        # Remove rows with still-missing critical values
        df = df.dropna(subset=['Price'])
        df = df[df['Price'] > 0]
        
        return df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        st.stop()

df = load_data()

# ==================== SIDEBAR ====================
st.sidebar.title("🚗 Cars Dashboard")
st.sidebar.write(f"**Author:** ANSHUL JADON")
st.sidebar.write(f"**Total Cars:** {len(df):,}")
st.sidebar.markdown("---")

page = st.sidebar.radio("📌 SELECT PAGE:", ["Overview", "Analysis", "Filters", "Statistics"])

# ==================== OVERVIEW ====================
if page == "Overview":
    st.title("🚗 Cars Market Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📊 Total Cars", f"{len(df):,}")
    col2.metric("💰 Avg Price", f"₹{df['Price'].mean():.1f}L")
    col3.metric("📅 Avg Year", f"{df['Year'].mean():.0f}")
    col4.metric("⛽ Avg Mileage", f"{df['Mileage_Value'].mean():.2f}")
    
    st.markdown("---")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Price Distribution")
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.hist(df['Price'], bins=50, color='#1f77b4', edgecolor='black', alpha=0.7)
        ax.set_xlabel('Price (₹L)', fontsize=10)
        ax.set_ylabel('Count', fontsize=10)
        ax.grid(True, alpha=0.3)
        st.pyplot(fig, use_container_width=True)
    
    with col2:
        st.subheader("Year Distribution")
        fig, ax = plt.subplots(figsize=(8, 4))
        year_counts = df['Year'].value_counts().sort_index()
        ax.bar(year_counts.index, year_counts.values, color='#ff7f0e', alpha=0.7)
        ax.set_xlabel('Year', fontsize=10)
        ax.set_ylabel('Count', fontsize=10)
        ax.grid(True, alpha=0.3)
        st.pyplot(fig, use_container_width=True)
    
    st.markdown("---")
    st.subheader("📋 Data Sample")
    display_cols = ['Company_Name', 'Model_Name', 'Year', 'Price', 'Mileage_Value', 'Fuel_Type']
    st.dataframe(df[display_cols].head(15), use_container_width=True)

# ==================== ANALYSIS ====================
elif page == "Analysis":
    st.title("📊 Market Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Price by Fuel Type")
        fig, ax = plt.subplots(figsize=(8, 5))
        fuel_price = df.groupby('Fuel_Type')['Price'].mean().sort_values()
        fuel_price.plot(kind='barh', ax=ax, color='#2ca02c', alpha=0.7)
        ax.set_xlabel('Avg Price (₹L)', fontsize=10)
        ax.grid(True, alpha=0.3)
        st.pyplot(fig, use_container_width=True)
    
    with col2:
        st.subheader("Price by Transmission")
        fig, ax = plt.subplots(figsize=(8, 5))
        trans_price = df.groupby('Transmission')['Price'].mean().sort_values()
        trans_price.plot(kind='barh', ax=ax, color='#d62728', alpha=0.7)
        ax.set_xlabel('Avg Price (₹L)', fontsize=10)
        ax.grid(True, alpha=0.3)
        st.pyplot(fig, use_container_width=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏢 Top 10 Companies")
        top_comp = df['Company_Name'].value_counts().head(10)
        fig, ax = plt.subplots(figsize=(8, 5))
        top_comp.plot(kind='barh', ax=ax, color='#9467bd', alpha=0.7)
        ax.set_xlabel('Count', fontsize=10)
        ax.grid(True, alpha=0.3)
        st.pyplot(fig, use_container_width=True)
    
    with col2:
        st.subheader("📍 Top 10 Locations by Avg Price")
        top_loc = df.groupby('Location')['Price'].mean().nlargest(10)
        fig, ax = plt.subplots(figsize=(8, 5))
        top_loc.plot(kind='barh', ax=ax, color='#8c564b', alpha=0.7)
        ax.set_xlabel('Avg Price (₹L)', fontsize=10)
        ax.grid(True, alpha=0.3)
        st.pyplot(fig, use_container_width=True)

# ==================== FILTERS ====================
elif page == "Filters":
    st.title("🔍 Filter & Search Cars")
    
    # Price range
    price_max = int(df['Price'].max())
    col1, col2, col3 = st.columns(3)
    
    with col1:
        min_price = st.slider("Min Price (₹L)", 0, price_max, 0, key='min_price')
    with col2:
        max_price = st.slider("Max Price (₹L)", 0, price_max, price_max, key='max_price')
    with col3:
        fuel_list = sorted([x for x in df['Fuel_Type'].unique() if pd.notna(x)])
        fuel_types = st.multiselect("Fuel Type", fuel_list, default=fuel_list)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        trans_list = sorted([x for x in df['Transmission'].unique() if pd.notna(x)])
        transmissions = st.multiselect("Transmission", trans_list, default=trans_list)
    
    with col2:
        owner_list = sorted([x for x in df['Owner_Type'].unique() if pd.notna(x)])
        owners = st.multiselect("Owner Type", owner_list, default=owner_list)
    
    with col3:
        loc_list = sorted([x for x in df['Location'].unique() if pd.notna(x)])
        locations = st.multiselect("Location", loc_list, default=loc_list[:10])
    
    # Apply filters
    filtered = df[
        (df['Price'] >= min_price) &
        (df['Price'] <= max_price) &
        (df['Fuel_Type'].isin(fuel_types)) &
        (df['Transmission'].isin(transmissions)) &
        (df['Owner_Type'].isin(owners)) &
        (df['Location'].isin(locations))
    ]
    
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🚗 Results", f"{len(filtered)}")
    col2.metric("💰 Avg Price", f"₹{filtered['Price'].mean():.1f}L" if len(filtered) > 0 else "N/A")
    col3.metric("⛽ Avg Mileage", f"{filtered['Mileage_Value'].mean():.2f}" if len(filtered) > 0 else "N/A")
    col4.metric("📅 Avg Year", f"{filtered['Year'].mean():.0f}" if len(filtered) > 0 else "N/A")
    
    st.markdown("---")
    
    if len(filtered) > 0:
        st.subheader(f"Results ({len(filtered)} cars)")
        display_cols = ['Company_Name', 'Model_Name', 'Year', 'Price', 'Mileage_Value', 'Fuel_Type', 'Transmission', 'Location']
        st.dataframe(filtered[display_cols], use_container_width=True)
        
        csv = filtered[display_cols].to_csv(index=False)
        st.download_button("📥 Download CSV", csv, "filtered_cars.csv", "text/csv")
    else:
        st.warning("❌ No cars match your filters. Try adjusting your criteria.")

# ==================== STATISTICS ====================
elif page == "Statistics":
    st.title("📈 Statistical Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💰 Price Statistics")
        price_stats = {
            "Mean": f"₹{df['Price'].mean():.2f}L",
            "Median": f"₹{df['Price'].median():.2f}L",
            "Std Dev": f"₹{df['Price'].std():.2f}L",
            "Min": f"₹{df['Price'].min():.2f}L",
            "Max": f"₹{df['Price'].max():.2f}L",
            "Q1": f"₹{df['Price'].quantile(0.25):.2f}L",
            "Q3": f"₹{df['Price'].quantile(0.75):.2f}L"
        }
        for key, val in price_stats.items():
            st.write(f"**{key}:** {val}")
    
    with col2:
        st.subheader("⛽ Mileage Statistics")
        mileage_stats = {
            "Mean": f"{df['Mileage_Value'].mean():.2f} kmpl",
            "Median": f"{df['Mileage_Value'].median():.2f} kmpl",
            "Std Dev": f"{df['Mileage_Value'].std():.2f} kmpl",
            "Min": f"{df['Mileage_Value'].min():.2f} kmpl",
            "Max": f"{df['Mileage_Value'].max():.2f} kmpl",
            "Q1": f"{df['Mileage_Value'].quantile(0.25):.2f} kmpl",
            "Q3": f"{df['Mileage_Value'].quantile(0.75):.2f} kmpl"
        }
        for key, val in mileage_stats.items():
            st.write(f"**{key}:** {val}")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Price Correlations")
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        corr_with_price = df[numeric_cols].corr()['Price'].sort_values(ascending=False)
        
        fig, ax = plt.subplots(figsize=(8, 5))
        corr_with_price[1:].plot(kind='barh', ax=ax, color='#17becf', alpha=0.7)
        ax.set_xlabel('Correlation with Price', fontsize=10)
        ax.grid(True, alpha=0.3)
        st.pyplot(fig, use_container_width=True)
    
    with col2:
        st.subheader("⛽ Fuel Type Distribution")
        fuel_dist = df['Fuel_Type'].value_counts()
        fig, ax = plt.subplots(figsize=(8, 5))
        colors = plt.cm.Set3(range(len(fuel_dist)))
        ax.pie(fuel_dist.values, labels=fuel_dist.index, autopct='%1.1f%%', colors=colors, startangle=90)
        st.pyplot(fig, use_container_width=True)

st.markdown("---")
st.markdown("<p align='center'>🚗 <b>Cars Market Dashboard</b> | Author: <b>Anshul</b></p>", unsafe_allow_html=True)
