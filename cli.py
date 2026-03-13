import argparse
import sys

from dotenv import load_dotenv

from bot.client import BinanceFuturesClient
from bot.logging_config import setup_logger
from bot.orders import place_order
from bot.validators import validate_limit, validate_side, validate_type


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        prog="trading_bot",
        description="Place Binance Futures orders via the command line (testnet).",
    )

    parser.add_argument("symbol", help="Trading pair (e.g. BTCUSDT)")
    parser.add_argument(
        "side",
        choices=["BUY", "SELL"],
        help="Order side: BUY or SELL",
    )
    parser.add_argument(
        "type",
        choices=["MARKET", "LIMIT"],
        help="Order type: MARKET or LIMIT",
    )
    parser.add_argument(
        "quantity",
        type=float,
        help="Quantity to buy or sell (in contract units)",
    )
    parser.add_argument(
        "--price",
        type=float,
        default=None,
        help="Price for LIMIT orders (required for LIMIT)",
    )

    return parser.parse_args(argv)


def main(argv=None):
    load_dotenv()  # allow .env in project root
    setup_logger()

    args = parse_args(argv)

    validate_side(args.side)
    validate_type(args.type)
    validate_limit(args.type, args.price)

    client = BinanceFuturesClient()

    try:
        response = place_order(
            client=client,
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
        )
        print("Order placed successfully:")
        print(response)

    except Exception as e:
        print("Failed to place order:", str(e), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
