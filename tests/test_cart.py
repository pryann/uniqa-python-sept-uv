import pytest
from src.cart import Cart, CartItem, ItemNotInCartError


CATALOG: dict[str, tuple[str, int]] = {
    "BOOK-1": ("Python cookbook", 1000),
    "MUG-1": ("Coffee MUG", 200),
}


def make_item(sku: str, quantity: int = 1) -> CartItem:
    name, unit_price = CATALOG[sku]
    return CartItem(sku, name, unit_price, quantity)


@pytest.fixture
def cart() -> Cart:
    return Cart()


def test_new_cart_is_empty(cart: Cart) -> None:
    assert cart.is_empty()
    assert cart.total() == 0


def test_add_same_sku_merge_quantity(cart: Cart) -> None:
    cart.add(make_item("BOOK-1"))
    cart.add(make_item("BOOK-1", 2))

    assert len(cart.items) == 1
    assert cart.items[0].quantity == 3


def test_average_price(cart: Cart) -> None:
    cart.add(make_item("BOOK-1"))
    cart.add(make_item("MUG-1", 2))

    result = cart.total() / 3

    assert result == pytest.approx(466.67, abs=0.005)


def test_remove_item(cart: Cart) -> None:
    cart.add(make_item("BOOK-1"))

    cart.remove("BOOK-1")

    assert cart.is_empty()


def test_remove_error_if_item_not_exist(cart: Cart) -> None:
    with pytest.raises(ItemNotInCartError):
        cart.remove("NOT_EXIST")


@pytest.mark.parametrize("quantity", [0, -1, -10])
def test_reject_error_if_quantity_is_not_positive(cart: Cart, quantity: int) -> None:
    with pytest.raises(ValueError, match="pozitívnak"):
        cart.add(make_item("BOOK-1", quantity=quantity))
