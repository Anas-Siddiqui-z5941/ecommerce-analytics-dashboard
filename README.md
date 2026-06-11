# 🧹 Data Cleaning & Analysis Pipeline

A Python pipeline that processes raw CSV datasets — handling missing values, removing duplicates, standardizing formats, and fixing data types — then runs exploratory business analysis and exports charts and a business report.

---

## ✨ Features

- **Missing value handling** — fills numeric columns with mean, categorical columns with mode
- **Duplicate removal** — drops all duplicate rows automatically
- **Date standardization** — converts date columns to consistent `YYYY-MM-DD` format
- **Data type fixing** — converts age and numeric columns to correct types
- **Business analysis** — computes revenue, campaign response rates, and customer segmentation by education and marital status
- **Visualizations** — generates 5 charts (bar, histogram, pie) saved to the `charts/` folder
- **Auto-generated report** — produces a full Markdown business report (`business_report.md`)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pandas
- matplotlib

```bash
pip install pandas matplotlib
```

### Step 1 — Clean the data

```bash
git clone https://github.com/Anas-Siddiqui-z5941/data-cleaning-project.git
cd data-cleaning-project
python cleaning.py
```

Input: `data/marketing_campaign.csv`  
Output: `data/cleaned_data.csv`

### Step 2 — Run analysis

```bash
python analysis.py
```

Output:
- `charts/` — 5 PNG charts
- `business_report.md` — full business analytics report

---

## 📁 Project Structure

```
data-cleaning-project/
│
├── cleaning.py              # Data cleaning pipeline
├── analysis.py              # Business analysis + chart generation
│
├── data/
│   ├── marketing_campaign.csv   # Raw input dataset
│   └── cleaned_data.csv         # Auto-generated cleaned output
│
├── charts/                  # Auto-generated PNG charts
│   ├── revenue_by_education.png
│   ├── revenue_by_marital_status.png
│   ├── spending_distribution.png
│   ├── education_distribution.png
│   └── response_by_education.png
│
├── business_report.md       # Auto-generated business analytics report
├── report.md                # Additional report
└── README.md
```

---

## ⚙️ Cleaning Pipeline Steps

| Step | Function                  | Description                                           |
| ---- | ------------------------- | ----------------------------------------------------- |
| 1    | `load_dataset()`          | Loads raw CSV into a pandas DataFrame                 |
| 2    | `handle_missing_values()` | Fills nulls with mean (numeric) or mode (categorical) |
| 3    | `remove_duplicates()`     | Drops duplicate rows                                  |
| 4    | `standardize_formats()`   | Converts date column to YYYY-MM-DD                    |
| 5    | `fix_data_types()`        | Converts age column to integer                        |
| 6    | `save_cleaned_data()`     | Exports cleaned DataFrame to CSV                      |

---

## 📊 Analysis Covers

- Total and average revenue per customer
- Revenue breakdown by education level and marital status
- Average spending and income by education
- Campaign response rates by education and marital status
- Top 10 highest-spending customers
- Education performance summary table

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square&logo=python&logoColor=white)

---

## 👤 Author

**Anas Mohiuddin Siddiqui**  
B.Tech CSE @ Integral University | Aspiring ML Engineer  
[LinkedIn](https://www.linkedin.com/in/anas-siddiqui-z5941) • [GitHub](https://github.com/Anas-Siddiqui-z5941)