"""Bevásárlókosár: állapotot tartó osztály."""

from dataclasses import dataclass


class ItemNotInCartError(KeyError):
    """A megadott cikkszám nincs a kosárban."""


@dataclass(slots=True)
class CartItem:
    sku: str
    name: str
    unit_price: int
    quantity: int = 1

    @property
    def subtotal(self) -> int:
        return self.unit_price * self.quantity


class Cart:
    """Cikkszám szerint összevont tételek listája."""

    def __init__(self) -> None:
        self._items: dict[str, CartItem] = {}

    def add(self, item: CartItem) -> None:
        if item.quantity <= 0:
            raise ValueError("A mennyiségnek pozitívnak kell lennie")
        existing = self._items.get(item.sku)
        if existing is None:
            self._items[item.sku] = item
        else:
            existing.quantity += item.quantity

    def remove(self, sku: str) -> None:
        if sku not in self._items:
            raise ItemNotInCartError(sku)
        del self._items[sku]

    @property
    def items(self) -> list[CartItem]:
        return list(self._items.values())

    def is_empty(self) -> bool:
        return not self._items

    def total(self) -> int:
        return sum(item.subtotal for item in self._items.values())
