import sys
import json
import random
from datetime import datetime

def generate_portfolio(date):
    portfolio = {
        "date": date,
        "funds": []
    }
    
    fund_names = ["Fund A", "Fund B", "Fund C", "Fund D"]  # Example fund names
    num_funds = random.randint(2, len(fund_names))
    selected_funds = random.sample(fund_names, num_funds)
    
    for fund in selected_funds:
        units_owned = round(random.uniform(10, 500), 2)
        portfolio["funds"].append({
            "name": fund,
            "units_owned": units_owned
        })
    
    return portfolio

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1]:
        date = sys.argv[1]
    else:
        date = datetime.now().strftime("%Y-%m-%d")
    
    portfolio_data = generate_portfolio(date)
    
    output_file = "artifacts/portfolio.json"
    with open(output_file, "w") as f:
        json.dump(portfolio_data, f, indent=4)

    print(f"Generated portfolio artifact: {output_file}")