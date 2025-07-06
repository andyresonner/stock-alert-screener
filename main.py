import requests
import time

# Define your stock symbols and threshold alerts
WATCHLIST = {
    "AAPL": 200.00,
    "TSLA": 800.00,
    "NVDA": 130.00
}

API_KEY = "demo"  # Replace with your real API key
BASE_URL = "https://www.alphavantage.co/query"

def get_price(symbol):
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    try:
        price = float(data["Global Quote"]["05. price"])
        return price
    except (KeyError, ValueError):
        return None

def check_stocks():
    for symbol, threshold in WATCHLIST.items():
        price = get_price(symbol)
        if price is None:
            print(f"⚠️ Error fetching price for {symbol}")
        elif price >= threshold:
            print(f"📈 {symbol} is above your alert threshold: ${price:.2f}")
        else:
            print(f"{symbol} is currently ${price:.2f}")

if __name__ == "__main__":
    while True:
        print("\n🔍 Checking stock prices...")
        check_stocks()
        time.sleep(300)  # Wait 5 minutes before next check
