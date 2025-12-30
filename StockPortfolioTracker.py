# Task 2: Stock Portfolio Tracker

# Step 1: Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 300,
    "GOOG": 2800,
    "AMZN": 3500
}

portfolio = {}
total_value = 0

print("Welcome to Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

# Step 2: User input loop
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not available. Try again.")
        continue

    quantity = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Step 3: Calculate total investment
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    value = qty * stock_prices[stock]
    total_value += value
    print(f"{stock}: {qty} shares → ${value}")

print(f"\nTotal Investment Value: ${total_value}")

# Step 4: Optional file save
save = input("Do you want to save results to file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio.txt", "w") as f:
        f.write("Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            value = qty * stock_prices[stock]
            f.write(f"{stock}: {qty} shares → ${value}\n")
        f.write(f"\nTotal Investment Value: ${total_value}\n")
    print("Portfolio saved to portfolio.txt")