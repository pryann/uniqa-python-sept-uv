import pytest

from src.shop import gross_price, apply_discount, average_rating


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


def test_apply_discount() -> None:
    # AAA pattern : Arrange, Act , Assert

    # Arrange
    price = 1000
    discount_percent = 10

    # Act
    result = apply_discount(price, discount_percent)

    # Assert
    assert result == 900


def test_apply_discount_bottom_interval_value_error() -> None:
    # AAA pattern : Arrange, Act , Assert
    # Arrange
    price = 1000
    discount_percent = -1

    with pytest.raises(ValueError):
        apply_discount(price, discount_percent)


def test_apply_discount_top_interval_value_error() -> None:
    # AAA pattern : Arrange, Act , Assert
    # Arrange
    price = 1000
    discount_percent = 101

    with pytest.raises(ValueError):
        apply_discount(price, discount_percent)


def test_average_rating() -> None:
    ratings = [1, 2]

    result = average_rating(ratings)

    assert result == 1.5


def test_average_rating_no_ratings() -> None:
    # ratings = []

    # result = average_rating(ratings)

    # assert result == 0.0

    assert average_rating([]) == 0.0


def test_average_rating_appox() -> None:
    ratings = [4.5, 4.6, 4.7]

    result = average_rating(ratings)

    assert result == pytest.approx(4.6)
