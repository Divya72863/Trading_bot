import logging


def setup_logger():
    """Configure logging for the trading bot.

    This sets a file logger and ensures python-binance request/response
    logging is enabled.
    """

    logging.basicConfig(
        filename="trading_bot.log",
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    # Also print INFO+ messages to the console.
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    )
    logging.getLogger().addHandler(console)

    # Ensure python-binance (and its underlying HTTP libs) log at DEBUG.
    logging.getLogger("binance").setLevel(logging.DEBUG)
    logging.getLogger("urllib3").setLevel(logging.DEBUG)
    logging.getLogger("requests").setLevel(logging.DEBUG)
