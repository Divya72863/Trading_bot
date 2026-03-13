import logging
import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

class BinanceFuturesClient:
    def __init__(self):
        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        if not api_key or not api_secret:
            raise RuntimeError(
                "API_KEY and API_SECRET must be set in the environment (or .env)"
            )

        self.client = Client(api_key, api_secret)

        # Enable debug logging of requests/responses from python-binance.
        self.client.verbose = True
        self.client.logger = logging.getLogger("binance")

        # Use Binance Futures testnet endpoint.
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def create_order(self, **params):
        return self.client.futures_create_order(**params)