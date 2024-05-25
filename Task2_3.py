# Lesson 2: Tuples
# 3. Python Loops and Tuples in Analytical Applications

def average_closing_price(stock_data, stock_symbol):
    """
    Calculates the average closing price for a specified stock symbol.
    """
    total_closing_price = 0
    count = 0

    for stock in stock_data:
        symbol, _, closing_price = stock
        if symbol == stock_symbol:
            total_closing_price += closing_price
            count += 1

    if count == 0:
        print(f"No data found for stock symbol '{stock_symbol}'.")
        return None

    average_price = total_closing_price / count
    return average_price

# Example usage
stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]

specified_stock = "AAPL"
average_price = average_closing_price(stock_data, specified_stock)

if average_price is not None:
    print(f"Average closing price for {specified_stock}: ${average_price:.2f}")
