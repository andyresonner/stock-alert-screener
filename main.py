import requests
import time

# Basic config
WATCHLIST = {
    "AAPL": 185,
    "NVDA": 130,
    "TSLA": 210,
}

ALERT_ABOVE = True  # True = alert if price goes above threshold, False = below

def fetch_price(ticker):
    url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={ticker}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["quoteResponse"]["result"][0]["regularMarketPrice"]
    return None

def check_alerts():
    print("\nChecking stock prices...\n")
    for ticker, threshold in WATCHLIST.items():
        price = fetch_price(ticker)
        if price is None:
            print(f"{ticker}: Failed to fetch price.")
            continue

        if (ALERT_ABOVE and price > threshold) or (not ALERT_ABOVE and price < threshold):
            print(f"🚨 ALERT: {ticker} is at ${price} (threshold: {threshold})")
        else:
            print(f"{ticker} is at ${price} (no alert)")

if __name__ == "__main__":
    while True:
        check_alerts()
        time.sleep(60)  # check every 60 seconds
