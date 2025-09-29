import requests
from prettytable import PrettyTable

API_URL = "https://api.coingecko.com/api/v3/simple/price"

# Portföyünü buraya gir (coin adı: miktar)
portfolio = {
    "bitcoin": 0.05,   # 0.05 BTC
    "ethereum": 1.2,   # 1.2 ETH
    "solana": 15       # 15 SOL
}

params = {
    "ids": ",".join(portfolio.keys()),
    "vs_currencies": "usd"
}

def get_prices():
    try:
        response = requests.get(API_URL, params=params)
        return response.json()
    except Exception as e:
        print("Hata:", e)
        return {}

def calculate_portfolio(prices):
    table = PrettyTable()
    table.field_names = ["Coin", "Miktar", "Fiyat (USD)", "Toplam (USD)"]

    total_value = 0
    for coin, amount in portfolio.items():
        price = prices[coin]["usd"]
        value = price * amount
        total_value += value
        table.add_row([coin.capitalize(), amount, f"${price:,.2f}", f"${value:,.2f}"])

    print(table)
    print(f"\n💰 Portföy Toplam Değeri: ${total_value:,.2f}")

if __name__ == "__main__":
    prices = get_prices()
    calculate_portfolio(prices)
