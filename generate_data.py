import csv
import random
import os
from datetime import datetime, timedelta

output_dir = r"C:\Users\mehru\.gemini\antigravity\scratch\powerbi-sales-dashboard"
os.makedirs(output_dir, exist_ok=True)

# 1. DimRegion
regions = [
    {"RegionID": 1, "RegionName": "North America", "Country": "United States", "Manager": "Sarah Jenkins"},
    {"RegionID": 2, "RegionName": "Europe", "Country": "Germany", "Manager": "Lukas Weber"},
    {"RegionID": 3, "RegionName": "Asia Pacific", "Country": "Japan", "Manager": "Kenji Sato"},
    {"RegionID": 4, "RegionName": "Latin America", "Country": "Brazil", "Manager": "Mariana Silva"}
]
with open(os.path.join(output_dir, "DimRegion.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["RegionID", "RegionName", "Country", "Manager"])
    writer.writeheader()
    writer.writerows(regions)

# 2. DimProduct
products = [
    {"ProductID": "P101", "ProductName": "UltraBook Pro 15", "Category": "Technology", "SubCategory": "Laptops", "UnitCost": 750.00, "BasePrice": 1200.00},
    {"ProductID": "P102", "ProductName": "Wireless Noise-Canceling Headphones", "Category": "Technology", "SubCategory": "Audio", "UnitCost": 85.00, "BasePrice": 180.00},
    {"ProductID": "P103", "ProductName": "Smart 4K Monitor 27\"", "Category": "Technology", "SubCategory": "Displays", "UnitCost": 180.00, "BasePrice": 320.00},
    {"ProductID": "P104", "ProductName": "Ergonomic Mesh Chair", "Category": "Furniture", "SubCategory": "Seating", "UnitCost": 120.00, "BasePrice": 250.00},
    {"ProductID": "P105", "ProductName": "Motorized Standing Desk", "Category": "Furniture", "SubCategory": "Desks", "UnitCost": 260.00, "BasePrice": 480.00},
    {"ProductID": "P106", "ProductName": "Executive Leather Armchair", "Category": "Furniture", "SubCategory": "Seating", "UnitCost": 190.00, "BasePrice": 380.00},
    {"ProductID": "P107", "ProductName": "Heavy-Duty Paper Shredder", "Category": "Office Supplies", "SubCategory": "Equipment", "UnitCost": 45.00, "BasePrice": 95.00},
    {"ProductID": "P108", "ProductName": "Premium Multi-Color Gel Pens (Box)", "Category": "Office Supplies", "SubCategory": "Writing", "UnitCost": 6.50, "BasePrice": 18.00},
    {"ProductID": "P109", "ProductName": "Recycled Copy Paper Case", "Category": "Office Supplies", "SubCategory": "Paper", "UnitCost": 18.00, "BasePrice": 36.00},
    {"ProductID": "P110", "ProductName": "Wireless Laser Pointer Presenter", "Category": "Technology", "SubCategory": "Accessories", "UnitCost": 15.00, "BasePrice": 45.00}
]
with open(os.path.join(output_dir, "DimProduct.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["ProductID", "ProductName", "Category", "SubCategory", "UnitCost", "BasePrice"])
    writer.writeheader()
    writer.writerows(products)

# 3. DimCustomer
segments = ["Consumer", "Corporate", "Home Office"]
customer_names = [
    "Alice Cooper", "Bob Smith", "Charlie Brown", "Diana Prince", "Evan Wright",
    "Fiona Gallagher", "George Clark", "Hannah Abbott", "Ian Malcolm", "Julia Roberts",
    "Kevin Bacon", "Laura Croft", "Michael Scott", "Nora Jones", "Oscar Martinez",
    "Pam Beesly", "Quentin Tarantino", "Rachel Green", "Steve Rogers", "Tony Stark",
    "Apex Tech Solutions", "Nexus Global Corp", "Vanguard Logistics", "BlueSky Enterprises", "Horizon Media"
]
customers = []
for i, name in enumerate(customer_names, 1):
    seg = segments[0] if i <= 12 else (segments[1] if i > 20 else segments[2])
    customers.append({
        "CustomerID": f"CUST{i:03d}",
        "CustomerName": name,
        "Segment": seg,
        "LoyaltyTier": random.choice(["Silver", "Gold", "Platinum", "Standard"])
    })

with open(os.path.join(output_dir, "DimCustomer.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["CustomerID", "CustomerName", "Segment", "LoyaltyTier"])
    writer.writeheader()
    writer.writerows(customers)

# 4. DimDate (Calendar Table for 2023 - 2024)
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 31)
curr = start_date
dates = []
while curr <= end_date:
    dates.append({
        "Date": curr.strftime("%Y-%m-%d"),
        "Year": curr.year,
        "MonthNumber": curr.month,
        "MonthName": curr.strftime("%B"),
        "MonthYear": curr.strftime("%b %Y"),
        "Quarter": f"Q{(curr.month-1)//3 + 1}",
        "DayOfWeek": curr.strftime("%A")
    })
    curr += timedelta(days=1)

with open(os.path.join(output_dir, "DimDate.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Date", "Year", "MonthNumber", "MonthName", "MonthYear", "Quarter", "DayOfWeek"])
    writer.writeheader()
    writer.writerows(dates)

# 5. FactSales
random.seed(42)
sales_records = []
order_id_counter = 1001

# Simulate 1200 sales transactions across 2023 and 2024
for _ in range(1200):
    prod = random.choice(products)
    cust = random.choice(customers)
    reg = random.choice(regions)
    
    # Random date with upward trend in 2024
    year = random.choices([2023, 2024], weights=[0.42, 0.58])[0]
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    order_date = f"{year}-{month:02d}-{day:02d}"
    
    # Corporate buyers buy higher quantities
    if cust["Segment"] == "Corporate":
        qty = random.choices([2, 3, 5, 10, 15], weights=[0.3, 0.3, 0.2, 0.15, 0.05])[0]
        discount = random.choice([0.05, 0.10, 0.15])
    elif cust["Segment"] == "Home Office":
        qty = random.choices([1, 2, 3, 4], weights=[0.5, 0.3, 0.15, 0.05])[0]
        discount = random.choice([0.0, 0.05, 0.08])
    else: # Consumer
        qty = random.choices([1, 2, 3], weights=[0.75, 0.2, 0.05])[0]
        discount = random.choice([0.0, 0.0, 0.05, 0.10])
        
    unit_price = prod["BasePrice"]
    unit_cost = prod["UnitCost"]
    gross_revenue = round(qty * unit_price, 2)
    net_revenue = round(gross_revenue * (1 - discount), 2)
    total_cost = round(qty * unit_cost, 2)
    profit = round(net_revenue - total_cost, 2)
    
    sales_records.append({
        "OrderID": f"ORD-{order_id_counter}",
        "OrderDate": order_date,
        "CustomerID": cust["CustomerID"],
        "ProductID": prod["ProductID"],
        "RegionID": reg["RegionID"],
        "Quantity": qty,
        "UnitPrice": unit_price,
        "UnitCost": unit_cost,
        "Discount": discount,
        "NetRevenue": net_revenue,
        "TotalCost": total_cost,
        "Profit": profit
    })
    order_id_counter += 1

with open(os.path.join(output_dir, "FactSales.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "OrderID", "OrderDate", "CustomerID", "ProductID", "RegionID",
        "Quantity", "UnitPrice", "UnitCost", "Discount", "NetRevenue", "TotalCost", "Profit"
    ])
    writer.writeheader()
    writer.writerows(sales_records)

print(f"Generated {len(sales_records)} sales records successfully in {output_dir}")
