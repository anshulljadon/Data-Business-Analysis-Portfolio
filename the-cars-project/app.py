# ============================================================
# app.py
# 🚗 Cars Data Analysis Dashboard
# Portfolio-Grade Streamlit Application
# Author: Anshul
# ============================================================

# -----------------------------
# IMPORT LIBRARIES
# -----------------------------
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="Cars Data Analysis Dashboard",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Cars Data Analysis Dashboard")
st.markdown(
    "A **professional, beginner-friendly** data analysis dashboard built using Python & Streamlit."
)

sns.set_style("whitegrid")


# -----------------------------
# LOAD DATA WITH ERROR HANDLING
# -----------------------------
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("Cars.csv")
        return df
    except FileNotFoundError:
        st.error("❌ Cars.csv not found. Please keep Cars.csv in the same folder as app.py")
        return None


df = load_data()
if df is None:
    st.stop()


# -----------------------------
# REQUIRED COLUMN CHECK
# -----------------------------
required_columns = [
    "Company_Name", "Year", "Price",
    "Fuel_Type", "Transmission"
]

missing_cols = [c for c in required_columns if c not in df.columns]

if missing_cols:
    st.error(f"❌ Missing columns in CSV file: {missing_cols}")
    st.stop()


# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("🔍 Filter Options")

company = st.sidebar.selectbox(
    "Company",
    ["All"] + sorted(df["Company_Name"].dropna().unique().tolist())
)

fuel = st.sidebar.selectbox(
    "Fuel Type",
    ["All"] + sorted(df["Fuel_Type"].dropna().unique().tolist())
)

transmission = st.sidebar.selectbox(
    "Transmission",
    ["All"] + sorted(df["Transmission"].dropna().unique().tolist())
)

year_min = int(df["Year"].min())
year_max = int(df["Year"].max())

year_range = st.sidebar.slider(
    "Year Range",
    year_min,
    year_max,
    (year_min, year_max)
)


# -----------------------------
# APPLY FILTERS SAFELY
# -----------------------------
filtered_df = df.copy()

if company != "All":
    filtered_df = filtered_df[filtered_df["Company_Name"] == company]

if fuel != "All":
    filtered_df = filtered_df[filtered_df["Fuel_Type"] == fuel]

if transmission != "All":
    filtered_df = filtered_df[filtered_df["Transmission"] == transmission]

filtered_df = filtered_df[
    (filtered_df["Year"] >= year_range[0]) &
    (filtered_df["Year"] <= year_range[1])
]

if filtered_df.empty:
    st.warning("⚠️ No data available for selected filters.")
    st.stop()


# -----------------------------
# TABS (PROFESSIONAL LAYOUT)
# -----------------------------
tab1, tab2, tab3, tab4 = st.tabs(
    ["📊 Overview", "📈 Trends", "🏭 Comparison", "📁 Data"]
)


# ============================================================
# TAB 1: OVERVIEW (KPIs)
# ============================================================
with tab1:
    st.subheader("📊 Key Business Metrics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Cars", len(filtered_df))
    col2.metric("Average Price", f"₹ {filtered_df['Price'].mean():,.0f}")
    col3.metric("Max Price", f"₹ {filtered_df['Price'].max():,.0f}")
    col4.metric("Min Price", f"₹ {filtered_df['Price'].min():,.0f}")

    st.info(
        "📌 **Business Insight:** This summary gives a quick understanding of "
        "market size and pricing range."
    )


# ============================================================
# TAB 2: TRENDS
# ============================================================
with tab2:
    st.subheader("📈 Price Distribution")

    fig, ax = plt.subplots()
    ax.hist(filtered_df["Price"].dropna(), bins=20)
    ax.set_xlabel("Price")
    ax.set_ylabel("Number of Cars")
    st.pyplot(fig)

    st.info(
        "📌 **Insight:** Most cars are concentrated in a specific price range, "
        "indicating customer affordability patterns."
    )

    st.subheader("📅 Average Price Trend by Year")

    yearly_price = (
        filtered_df.groupby("Year")["Price"]
        .mean()
        .reset_index()
    )

    fig, ax = plt.subplots()
    ax.plot(yearly_price["Year"], yearly_price["Price"], marker="o")
    ax.set_xlabel("Year")
    ax.set_ylabel("Average Price")
    st.pyplot(fig)

    st.info(
        "📌 **Insight:** Prices generally decrease as cars become older due to depreciation."
    )


# ============================================================
# TAB 3: COMPARISON
# ============================================================
with tab3:
    st.subheader("🏭 Average Price by Company")

    company_price = (
        filtered_df.groupby("Company_Name")["Price"]
        .mean()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots()
    company_price.plot(kind="bar", ax=ax)
    ax.set_xlabel("Company")
    ax.set_ylabel("Average Price")
    st.pyplot(fig)

    st.info(
        "📌 **Insight:** Premium brands maintain higher resale value."
    )

    st.subheader("⛽ Fuel Type Price Comparison")

    fig, ax = plt.subplots()
    sns.barplot(
        data=filtered_df,
        x="Fuel_Type",
        y="Price",
        estimator=np.mean,
        ax=ax
    )
    ax.set_xlabel("Fuel Type")
    ax.set_ylabel("Average Price")
    st.pyplot(fig)

    st.info(
        "📌 **Insight:** Fuel type plays an important role in determining car prices."
    )


# ============================================================
# TAB 4: DATA PREVIEW + DOWNLOAD
# ============================================================
with tab4:
    st.subheader("📁 Data Preview")

    st.dataframe(filtered_df.head(20))

    csv = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download Filtered Data",
        data=csv,
        file_name="filtered_cars_data.csv",
        mime="text/csv"
    )


# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown(
    """
    **Portfolio Project by Anshul**  
    MBA (Finance & Marketing) | Aspiring Data Analyst  

    🔹 Tools: Python, Pandas, NumPy, Seaborn, Streamlit  
    🔹 Focus: Business insights, clean code, professional dashboard
    """
)

st.markdown("© 2024 Anshul. All rights reserved.")