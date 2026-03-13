# Trading Bot (Binance Futures)

A minimal Python trading bot scaffold for placing **Binance Futures** orders via **Binance Testnet**.

## ✅ Prerequisites

- Python 3.11+ (or compatible)
- A Binance Futures testnet API key + secret
- `python-dotenv` (already listed in `requirements.txt`)

## 🧩 Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project root with your testnet credentials:

```env
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_api_secret
```

> Note: This project is currently configured to use the Binance **Futures testnet** endpoint.

## 🚀 Usage

Place an order from the command line:

```bash
python cli.py SYMBOL SIDE TYPE QUANTITY [--price PRICE]
```

### Examples

- Market buy 0.001 BTCUSDT:

```bash
python cli.py BTCUSDT BUY MARKET 0.001
```

- Limit sell 0.001 BTCUSDT at 60,000:

```bash
python cli.py BTCUSDT SELL LIMIT 0.001 --price 60000
```

## 🧠 Code Layout

- `bot/client.py`: Wraps the Binance `Client`, points to the futures testnet, and creates orders.
- `bot/orders.py`: Builds order parameters and calls the client’s `create_order`.
- `bot/validators.py`: Validates user input (side, type, price requirements).
- `bot/logging_config.py`: Configures logging (file + console) and enables python-binance request/response logging to `trading_bot.log`.
- `cli.py`: Command-line entrypoint to place orders.

## 🛠️ Next Improvements (Optional)

- Add order status checks / trade history logging.
- Add risk management (position sizing, stop loss, take profit).
- Add support for live Binance (non-testnet) by making endpoint configurable.
