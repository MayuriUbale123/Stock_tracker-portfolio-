import csv

def get_stock_input(prices):

    stock = input("Enter stock symbol (or 'done' to finish): ").strip().upper()
    if stock == "DONE":
        return None, None
    qty_str = input("Enter quantity: ").strip()
    try:
        qty = int(qty_str)
    except ValueError:
        print("Invalid quantity. Please enter an integer.")
        return get_stock_input(prices)
    return stock, qty

def calculate_portfolio_value(prices, user_entries):
    
    

    results = []
    total = 0
    for stock, qty in user_entries:
        if stock in prices:
            value = prices[stock] * qty
            results.append({
                "stock": stock,
                "quantity": qty,
                "price": prices[stock],
                "value": value
            })
            total += value
        else:
            print(f"Warning: {stock} not found in price list — skipping.")
    return results, total

def save_to_txt(filename, portfolio_results, total_value):

    
    
    with open(filename, "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write("========================\n")
        f.write(f"{'Stock':<10}{'Qty':<8}{'Price':<10}{'Value':<10}\n")
        for entry in portfolio_results:
            f.write(f"{entry['stock']:<10}{entry['quantity']:<8}{entry['price']:<10}{entry['value']:<10}\n")
        f.write("\n")
        f.write(f"Total Investment Value: {total_value}\n")

def save_to_csv(filename, portfolio_results, total_value):
    
    
    
    fieldnames = ["stock", "quantity", "price", "value"]
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in portfolio_results:
            writer.writerow(entry)
        
        writer.writerow({
            "stock": "TOTAL",
            "quantity": "",
            "price": "",
            "value": total_value
        })

def main():
    
    prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOG": 2000,
        "MSFT": 300
    }

    print("Welcome to Stock Portfolio Tracker")
    print("Enter stock and quantity. Type 'done' when finished.\n")

    user_entries = []
    while True:
        stock, qty = get_stock_input(prices)
        if stock is None:
            break
        user_entries.append((stock, qty))

    if not user_entries:
        print("No stocks entered. Exiting.")
        return

    portfolio_results, total_value = calculate_portfolio_value(prices, user_entries)

    print("\nYour Portfolio:")
    for entry in portfolio_results:
        print(f"{entry['stock']}: qty = {entry['quantity']}, price = {entry['price']}, value = {entry['value']}")
    print(f"Total Investment Value = {total_value}")

    
    txt_filename = "portfolio_summary.txt"
    csv_filename = "portfolio_summary.csv"
    save_to_txt(txt_filename, portfolio_results, total_value)
    save_to_csv(csv_filename, portfolio_results, total_value)

    print(f"\nSaved summary to {txt_filename} and {csv_filename}")

if __name__ == "__main__":
    main()
