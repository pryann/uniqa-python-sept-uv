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


def test_gross_price_with_custom_vat() -> None:
    # AAA pattern : Arrange, Act , Assert

    # Arrange
    net_price = 1000
    vat_rate = 10

    # Act
    result = gross_price(net_price, vat_rate)

    # Assert
    assert result == 1100


def test_gross_price_reject_negative_value_error() -> None:
    # AAA pattern : Arrange, Act , Assert

    # Arrange
    net_price = -1000
    vat_rate = 10

    # Act - Assert
    with pytest.raises(ValueError):
        gross_price(net_price, vat_rate)
