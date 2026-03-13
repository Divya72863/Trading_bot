import logging

def place_order(client, symbol, side, order_type, quantity, price=None):

    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    logging.info(f"Order Request: {params}")

    try:
        response = client.create_order(**params)
        logging.info(f"Order Response: {response}")
        return response
    except Exception as e:
        logging.error(str(e))
        raise