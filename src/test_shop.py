import pytest

from shop import gross_price, apply_discount, average_rating


def test_gross_price_add_default_vat() -> None:
    # AAA pattern : Arrange, Act , Assert

    # Arrange
    net_price = 1000

    # Act
    result = gross_price(net_price)

    # Assert
    assert result == 1270
