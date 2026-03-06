# Retail Sales Dashboard (Power BI)

Interactive **Power BI dashboard** for exploring a company’s **2024 retail sales performance** across key business dimensions such as **Region, Store, Product Category, and Time**.

The dashboard enables data-driven insights into revenue trends, product performance, and store-level comparisons through interactive visualizations and KPIs.

---

# Project Overview

This project analyzes retail sales data and provides business insights through an interactive dashboard that highlights:

- Total Revenue
- Sales Quantity
- Profitability
- Regional and store performance
- Product category performance
- Monthly revenue trends

The dashboard supports both **executive-level summaries** and **detailed operational analysis**.

---

# Dataset Overview

The project uses five datasets:

| Dataset | Description | Rows |
|------|------|------|
| `calendar.csv` | Date metadata including Year, Month, Quarter, Weekday | 365 |
| `cities_lookup.csv` | Mapping of non-standard city names to standardized ones | 10 |
| `products.csv` | Product information including category, cost price, and sale price | 20 |
| `sales.csv` | Fact table with DateID, StoreID, ProductID, Quantity Sold, and Revenue | 5000 |
| `stores.csv` | Store metadata including StoreID, Store Name, Region, and City | 10 |

---

# Business Questions Addressed

The dashboard focuses on answering key analytical questions:

- Which **regions or stores generate the highest revenue**?
- How does **profit margin vary by product or category**?
- How do **revenue and profit evolve month-over-month**?
- Which **products drive the most revenue or quantity sold**?
- Which **stores underperform in sales or average sale value**?

---

# Key KPIs (DAX Measures)

### Total Revenue
```DAX
Total Revenue = SUM(FactSales[Revenue])

Total Quantity Sold = SUM(FactSales[QtySold])

Avg Sale Value = [Total Revenue] / [Total Quantity Sold]

Total Cost = SUM(FactSales[QtySold] * RELATED(DimProduct[CostPrice]))

Profit Margin % = DIVIDE([Total Revenue] - [Total Cost], [Total Revenue], 0)

Total Profit = [Total Revenue] - [Total Cost]

```
# Dashboard Structure

The Power BI report is organized into three pages:

# 1. Homepage

# Purpose: Provide an overview and navigation layer.

# Content:

- Executive summary of the dashboard objectives

- Description of data sources and KPIs

- Navigation buttons linking to other dashboard pages

# 2. Executive Summary

# Purpose: Offer a high-level view of company-wide performance.

# Visuals include:

# KPI cards:

- Total Revenue

- Quantity Sold

- Avg Sale Value

- Profit Margin

# Bar charts:

- Revenue by Region

- Revenue by Category

# Line chart:

- Revenue and Profit Margin over time (monthly)

# Pie chart:

- Revenue distribution across regions

# Interactive slicers:

- Region

- Category

- Month

- Year

- Drill-down functionality:

- Region → Store navigation in bar charts

# 3. Store & Product Deep Dive

# Purpose:
Support granular analysis by product and geography.

# Visuals include:

- Matrix: Revenue by Category and Region

- Stacked Bar Chart: Top Products by Revenue

- Table: Store-level KPIs including Quantity, Revenue, and Margin

- Bar Chart: Quantity Sold by Product Category

Filter context is preserved through slicers across visuals.

# Dashboard Features:

- Interactive slicers

- Date (DimDate)

- Region

- Category

- Store

- Drill-down analysis

- Users can drill from Region → Store

- Cross-filtering

All visuals interact dynamically based on slicer selections

# Tools Used:

- Power BI

- DAX

- CSV datasets

- Data modeling (Fact & Dimension tables)

# Project Purpose

This project demonstrates how Power BI can transform raw retail data into actionable business insights, enabling better performance monitoring, decision-making, and business strategy development.
