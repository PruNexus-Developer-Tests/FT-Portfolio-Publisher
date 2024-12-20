import json
import random
from datetime import datetime

# Fund names
fund_names = ["Fund A", "Fund B", "Fund C", "Fund D", "Fund E"]

# Generate random portfolio data
def generate_portfolio():
    portfolio = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "funds": []
    }
    
    num_funds = random.randint(2, len(fund_names))
    selected_funds = random.sample(fund_names, num_funds)
    
    for fund in selected_funds:
        units_owned = round(random.uniform(10, 500), 2)
        portfolio["funds"].append({
            "name": fund,
            "units_owned": units_owned
        })
    
    return portfolio

# Write to JSON file
output_file = "artifacts/portfolio.json"
portfolio_data = generate_portfolio()
with open(output_file, "w") as f:
    json.dump(portfolio_data, f, indent=4)

print(f"Generated portfolio artifact: {output_file}")