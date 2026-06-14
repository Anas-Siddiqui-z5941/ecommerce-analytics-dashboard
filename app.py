import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Customer Spending Analytics Dashboard",
    layout="wide"
)

st.title("📊 Customer Spending Analytics Dashboard")

# =====================================
# LOAD DATA
# =====================================

df = pd.read_csv("data/cleaned_data.csv", sep="\t")

# =====================================
# FEATURE ENGINEERING
# =====================================

spending_cols = [
    "MntWines",
    "MntFruits",
    "MntMeatProducts",
    "MntFishProducts",
    "MntSweetProducts",
    "MntGoldProds"
]

df["TotalSpent"] = df[spending_cols].sum(axis=1)

# =====================================
# SIDEBAR FILTERS
# =====================================

st.sidebar.header("Filters")

education = st.sidebar.selectbox(
    "Education",
    ["All"] + sorted(df["Education"].unique().tolist())
)

marital_status = st.sidebar.selectbox(
    "Marital Status",
    ["All"] + sorted(df["Marital_Status"].unique().tolist())
)

# Apply filters

filtered_df = df.copy()

if education != "All":
    filtered_df = filtered_df[
        filtered_df["Education"] == education
    ]

if marital_status != "All":
    filtered_df = filtered_df[
        filtered_df["Marital_Status"] == marital_status
    ]

# =====================================
# KPI SECTION
# =====================================

total_spending = filtered_df["TotalSpent"].sum()
avg_spending = filtered_df["TotalSpent"].mean()
avg_income = filtered_df["Income"].mean()
customer_count = len(filtered_df)

st.subheader("📌 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Spending",
    f"${total_spending:,.0f}"
)

col2.metric(
    "Avg Spending",
    f"${avg_spending:,.0f}"
)

col3.metric(
    "Avg Income",
    f"${avg_income:,.0f}"
)

col4.metric(
    "Customers",
    customer_count
)

# =====================================
# DATASET PREVIEW
# =====================================

with st.expander("View Dataset Preview"):
    st.dataframe(filtered_df.head(10))

# =====================================
# CHART 1
# SPENDING BY EDUCATION
# =====================================

st.subheader("Average Spending by Education")

education_spending = (
    filtered_df.groupby("Education")["TotalSpent"]
    .mean()
    .sort_values(ascending=False)
)

fig1, ax1 = plt.subplots(figsize=(8, 4))

education_spending.plot(
    kind="bar",
    ax=ax1
)

ax1.set_ylabel("Average Spending")

st.pyplot(fig1)

# =====================================
# CHART 2
# SPENDING BY MARITAL STATUS
# =====================================

st.subheader("Average Spending by Marital Status")

marital_spending = (
    filtered_df.groupby("Marital_Status")["TotalSpent"]
    .mean()
    .sort_values(ascending=False)
)

fig2, ax2 = plt.subplots(figsize=(8, 4))

marital_spending.plot(
    kind="bar",
    ax=ax2
)

ax2.set_ylabel("Average Spending")

st.pyplot(fig2)

# =====================================
# CHART 3
# SPENDING DISTRIBUTION
# =====================================

st.subheader("Customer Spending Distribution")

fig3, ax3 = plt.subplots(figsize=(8, 4))

ax3.hist(
    filtered_df["TotalSpent"],
    bins=30
)

ax3.set_xlabel("Total Spending")
ax3.set_ylabel("Number of Customers")

st.pyplot(fig3)

# =====================================
# INSIGHTS
# =====================================

st.subheader("📈 Insights")

best_education = (
    filtered_df.groupby("Education")["TotalSpent"]
    .mean()
    .idxmax()
)

best_marital = (
    filtered_df.groupby("Marital_Status")["TotalSpent"]
    .mean()
    .idxmax()
)

highest_income_group = (
    filtered_df.groupby("Education")["Income"]
    .mean()
    .idxmax()
)

st.success(
    f"Highest Spending Education Group: {best_education}"
)

st.success(
    f"Highest Spending Marital Status: {best_marital}"
)

st.success(
    f"Highest Income Education Group: {highest_income_group}"
)

# =====================================
# FOOTER
# =====================================

st.markdown("---")
st.caption(
    "Built using Streamlit, Pandas and Matplotlib"
)