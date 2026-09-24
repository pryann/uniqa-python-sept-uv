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
