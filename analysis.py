# analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import os

# ==========================================

# LOAD DATA

# ==========================================

df = pd.read_csv("data/cleaned_data.csv", sep="\t")

# Create charts folder automatically

os.makedirs("charts", exist_ok=True)

# ==========================================

# FEATURE ENGINEERING

# ==========================================

spending_cols = [
'MntWines',
'MntFruits',
'MntMeatProducts',
'MntFishProducts',
'MntSweetProducts',
'MntGoldProds'
]

df['TotalSpent'] = df[spending_cols].sum(axis=1)

# ==========================================

# BUSINESS QUESTIONS

# ==========================================

print("\n========== BUSINESS ANALYTICS ==========\n")

# 1. Total Revenue

total_revenue = df['TotalSpent'].sum()

print("1. Total Revenue")
print(total_revenue)

# ------------------------------------------

# 2. Average Revenue Per Customer

avg_revenue = df['TotalSpent'].mean()

print("\n2. Average Revenue Per Customer")
print(round(avg_revenue, 2))

# ------------------------------------------

# 3. Revenue by Education

print("\n3. Revenue by Education")

revenue_education = (
df.groupby('Education')['TotalSpent']
.sum()
.sort_values(ascending=False)
)

print(revenue_education)

# ------------------------------------------

# 4. Revenue by Marital Status

print("\n4. Revenue by Marital Status")

revenue_marital = (
df.groupby('Marital_Status')['TotalSpent']
.sum()
.sort_values(ascending=False)
)

print(revenue_marital)

# ------------------------------------------

# 5. Average Spending by Education

print("\n5. Average Spending by Education")

avg_spending_edu = (
df.groupby('Education')['TotalSpent']
.mean()
.sort_values(ascending=False)
)

print(avg_spending_edu)

# ------------------------------------------

# 6. Most Common Education Levels

print("\n6. Most Common Education Levels")

print(df['Education'].value_counts())

# ------------------------------------------

# 7. Most Common Marital Status

print("\n7. Most Common Marital Status")

print(df['Marital_Status'].value_counts())

# ------------------------------------------

# 8. Average Income by Education

print("\n8. Average Income by Education")

avg_income = (
df.groupby('Education')['Income']
.mean()
.sort_values(ascending=False)
)

print(avg_income)

# ------------------------------------------

# 9. Campaign Response Rate by Education

print("\n9. Campaign Response Rate by Education")

response_edu = (
df.groupby('Education')['Response']
.mean()
.sort_values(ascending=False)
)

print(response_edu)

# ------------------------------------------

# 10. Campaign Response Rate by Marital Status

print("\n10. Campaign Response Rate by Marital Status")

response_marital = (
df.groupby('Marital_Status')['Response']
.mean()
.sort_values(ascending=False)
)

print(response_marital)

# ------------------------------------------

# 11. Top 10 Highest Spending Customers

print("\n11. Top 10 Highest Spending Customers")

top_customers = (
df[['ID', 'TotalSpent']]
.sort_values('TotalSpent', ascending=False)
.head(10)
)

print(top_customers)

# ------------------------------------------

# 12. Business Summary Table

print("\n12. Education Performance Summary")

summary = (
df.groupby('Education')
.agg({
'Income': 'mean',
'TotalSpent': 'mean',
'Response': 'mean'
})
.sort_values('TotalSpent', ascending=False)
)

print(summary)

# ==========================================

# VISUALIZATIONS

# ==========================================

# Revenue by Education

plt.figure(figsize=(8, 5))

revenue_education.plot(kind='bar')

plt.title("Revenue by Education")
plt.xlabel("Education")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig("charts/revenue_by_education.png")

plt.close()

# ==========================================

# Revenue by Marital Status

plt.figure(figsize=(8, 5))

revenue_marital.plot(kind='bar')

plt.title("Revenue by Marital Status")
plt.xlabel("Marital Status")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig("charts/revenue_by_marital_status.png")

plt.close()

# ==========================================

# Distribution of Customer Spending

plt.figure(figsize=(8, 5))

plt.hist(df['TotalSpent'], bins=30)

plt.title("Distribution of Customer Spending")
plt.xlabel("Total Spent")
plt.ylabel("Customers")

plt.tight_layout()

plt.savefig("charts/spending_distribution.png")

plt.close()

# ==========================================

# Education Distribution

plt.figure(figsize=(8, 8))

df['Education'].value_counts().plot(
kind='pie',
autopct='%1.1f%%'
)

plt.ylabel("")
plt.title("Education Distribution")

plt.tight_layout()

plt.savefig("charts/education_distribution.png")

plt.close()

# ==========================================

# Campaign Response by Education

plt.figure(figsize=(8, 5))

response_edu.plot(kind='bar')

plt.title("Campaign Response Rate by Education")
plt.xlabel("Education")
plt.ylabel("Response Rate")

plt.tight_layout()

plt.savefig("charts/response_by_education.png")

plt.close()

# ==========================================

print("\nAll charts saved successfully!")
print("Check the charts folder.")

# ==========================================
# GENERATE BUSINESS REPORT
# ==========================================

report = f"""
# Business Analytics Report

## Dataset Overview

This analysis was performed on a customer marketing dataset containing {len(df)} customers.

### Key Metrics

- Total Customers: {len(df)}
- Total Revenue: {total_revenue:,.0f}
- Average Revenue per Customer: {avg_revenue:.2f}

---

# Revenue Analysis

## Revenue by Education

{revenue_education.to_markdown()}

### Insight

Graduation customers generate the highest total revenue.

---

## Revenue by Marital Status

{revenue_marital.to_markdown()}

### Insight

Married customers generate the highest revenue.

---

# Customer Segmentation

## Average Spending by Education

{avg_spending_edu.to_markdown()}

### Insight

PhD customers spend the most per customer.

---

## Average Income by Education

{avg_income.to_markdown()}

### Insight

PhD customers have the highest average income.

---

# Marketing Campaign Analysis

## Campaign Response Rate by Education

{response_edu.to_markdown()}

### Insight

PhD customers respond best to campaigns.

---

## Campaign Response Rate by Marital Status

{response_marital.to_markdown()}

### Insight

Widow and Single customers have the strongest campaign response rates among major customer groups.

---

# Top Spending Customers

{top_customers.to_markdown(index=False)}

---

# Key Findings

1. Total customer revenue reached **{total_revenue:,.0f}**.
2. Average customer spending was **{avg_revenue:.2f}**.
3. Highest revenue education group: **{revenue_education.idxmax()}**.
4. Highest revenue marital status: **{revenue_marital.idxmax()}**.
5. Highest average spending group: **{avg_spending_edu.idxmax()}**.
6. Highest average income group: **{avg_income.idxmax()}**.
7. Best campaign response group: **{response_edu.idxmax()}**.
8. Most common education level: **{df['Education'].value_counts().idxmax()}**.
9. Most common marital status: **{df['Marital_Status'].value_counts().idxmax()}**.
10. Highest spending customer spent **{top_customers['TotalSpent'].max():,.0f}**.

---

# Visualizations

## Revenue by Education

![Revenue by Education](charts/revenue_by_education.png)

## Revenue by Marital Status

![Revenue by Marital Status](charts/revenue_by_marital_status.png)

## Distribution of Customer Spending

![Spending Distribution](charts/spending_distribution.png)

## Education Distribution

![Education Distribution](charts/education_distribution.png)

## Campaign Response by Education

![Campaign Response](charts/response_by_education.png)

---

# Recommendations

1. Focus marketing efforts on PhD, Master, and Graduation customers.
2. Develop loyalty programs for high-spending customers.
3. Create specialized campaigns for Single and Widow customers.
4. Increase engagement among low-spending customer segments.
5. Continue customer segmentation analysis to improve campaign effectiveness.
"""

with open("business_report.md", "w", encoding="utf-8") as f:
    f.write(report)

print("\nBusiness report saved as business_report.md")
