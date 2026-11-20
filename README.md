# Power BI Sales Performance Analysis Dashboard

[![Power BI](https://img.shields.io/badge/Power_BI-Desktop-F2C811?logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub Pages](https://img.shields.io/badge/Live_Demo-GitHub_Pages-2ea44f?logo=github)](index.html)

An end-to-end business intelligence solution analyzing company sales, revenue, profit margins, regional performance, and customer purchasing patterns.

---

## 📌 Dashboard Overview

The dashboard answers critical executive business questions across five core dimensions:

1. **Executive KPI Cards**: Real-time snapshot of Total Revenue, Total Profit, Gross Profit Margin %, Total Orders, and Average Order Value (AOV).
2. **Sales & Profit Trends**: Monthly and yearly trends highlighting seasonality and profit margins using a combo line and column chart.
3. **Top-Selling Products**: Ranking of top revenue-generating products and their profit contributions.
4. **Regional Performance**: Geographic distribution across North America, Europe, Asia Pacific, and Latin America.
5. **Customer Purchasing Patterns**: Segment behavior (Corporate bulk buyers vs. Consumer retail shoppers vs. Home Office bundles).

> 💡 **Interactive Web Prototype**: Open `index.html` in any web browser to test the interactive prototype with dynamic filters.

---

## 🏗️ Data Model (Star Schema)

The project implements a clean Star Schema data model:

```
        +-------------------+
        |    DimCustomer    |
        +-------------------+
                  | (1:N)
                  v
+--------------+  |  +---------------+
|   DimDate    |---->|   FactSales   |<----+ DimProduct
+--------------+  |  +---------------+     +------------+
                  ^          ^
                  | (1:N)    | (1:N)
        +-------------------+
        |     DimRegion     |
        +-------------------+
```

### Table Relationships
- `FactSales` &larr; `DimDate`: `FactSales[OrderDate]` &rarr; `DimDate[Date]` (1:N)
- `FactSales` &larr; `DimProduct`: `FactSales[ProductID]` &rarr; `DimProduct[ProductID]` (1:N)
- `FactSales` &larr; `DimCustomer`: `FactSales[CustomerID]` &rarr; `DimCustomer[CustomerID]` (1:N)
- `FactSales` &larr; `DimRegion`: `FactSales[RegionID]` &rarr; `DimRegion[RegionID]` (1:N)

---

## 📐 DAX Measures Library

Add these DAX measures to your Power BI report in a dedicated `_Measures` table:

```dax
// 1. Total Net Revenue
Total Revenue = 
SUMX(
    FactSales,
    FactSales[Quantity] * FactSales[UnitPrice] * (1 - FactSales[Discount])
)

// 2. Total Cost of Goods Sold (COGS)
Total Cost = 
SUMX(
    FactSales,
    FactSales[Quantity] * FactSales[UnitCost]
)

// 3. Total Profit
Total Profit = 
[Total Revenue] - [Total Cost]

// 4. Profit Margin Percentage
Profit Margin % = 
DIVIDE([Total Profit], [Total Revenue], 0)

// 5. Total Orders
Total Orders = 
DISTINCTCOUNT(FactSales[OrderID])

// 6. Average Order Value (AOV)
Average Order Value = 
DIVIDE([Total Revenue], [Total Orders], 0)

// 7. Year-over-Year Revenue Growth %
YoY Revenue Growth % = 
VAR _PriorYear = CALCULATE([Total Revenue], SAMEPERIODLASTYEAR(DimDate[Date]))
RETURN
DIVIDE([Total Revenue] - _PriorYear, _PriorYear, 0)
```

---

## 📂 Repository Structure

```
├── DimCustomer.csv           # Customer dimension table (Segments, Loyalty Tiers)
├── DimDate.csv               # Complete date calendar table (2023 - 2024)
├── DimProduct.csv            # Product catalog dimension (Categories, Costs, Prices)
├── DimRegion.csv             # Geographic territory table (Regions, Countries, Managers)
├── FactSales.csv             # Transactional fact table (1,200 records)
├── generate_data.py          # Python data generation script
├── index.html                # Interactive dashboard web preview & simulator
├── .gitignore                # Git ignore rules
└── README.md                 # Complete documentation and setup guide
```

---

## 🚀 Quickstart: Setting Up in Power BI Desktop

1. **Clone this repository**:
   ```bash
   git clone <YOUR-REPO-URL>
   cd <YOUR-REPO-FOLDER>
   ```
2. **Open Power BI Desktop**.
3. Go to **Get Data** &rarr; **Text/CSV** and import all 5 `.csv` files.
4. Switch to **Model View** and verify the 1-to-Many relationships.
5. Create a table named `_Measures`, paste the DAX calculations above, and build the visual report canvas!

---

## 📄 License
This project is open-source and available under the MIT License.
