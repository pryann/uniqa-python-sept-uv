def gross_price(net_price: int, vat_percent: int = 27) -> float:
    if net_price < 0:
        raise ValueError("Price can not be negative value")
    return net_price * (1 + vat_percent / 100)


def apply_discount(price: int, discount_percent: int) -> float:
    if not 0 <= discount_percent <= 100:
        raise ValueError(f"Invalid discount percent: {discount_percent}")
    return price * (1 - discount_percent / 100)


def average_rating(ratings: list[int]) -> float:
    return 0.0 if not ratings else sum(ratings) / len(ratings)


def summa_net_prices(net_prices: list[int]) -> int:
    """sum prices if list is empty return 0"""
    # summa = 0
    # for i in net_prices:
    #     summa += i
    # return summa

    # if len(net_prices) == 0:
    #     return 0
    # return sum(net_prices)

    # if not len(net_prices):
    #     return 0
    # return sum(net_prices)

    # if not net_prices:
    #     return 0
    # return sum(net_prices)

    # return 0 if not net_prices else sum(net_prices)

    return sum(net_prices)
