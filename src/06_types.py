def summa(a: int, b: int) -> int:
    return a + b


print(summa(10, 10))

# int, float, complex, str, None
# list[int], tuple[str, str], dict[str, str | int | float]
# union: str | None


def calculate_gross_price(net_price: int | float, vat_rate_percent: int = 27) -> float:
    return net_price * (1 + vat_rate_percent / 100)


print(calculate_gross_price(100))
print(calculate_gross_price(1000))
print(calculate_gross_price(5000))
print(calculate_gross_price(50000, 5))


# def add_item_to_basket(item: str, basket: list[str] = []) -> list[str]:
def add_item_to_basket(item: str, basket: list[str] | None = None) -> list[str]:
    if basket is None:
        basket = []
    basket.append(item.upper())
    return basket


# basket = []
# add_item_to_basket("alma", basket)
# add_item_to_basket("körte", basket)
# add_item_to_basket("szilva", basket)
print(add_item_to_basket("alma"))
print(add_item_to_basket("körte"))
print(add_item_to_basket("szilva"))
