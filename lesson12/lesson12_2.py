from typing import Dict

class Item:
    def __init__(self, name: str, price: float, description: str, dimensions: str) -> None:
        self.name: str = name
        self.price: float = price
        self.description: str = description
        self.dimensions: str = dimensions

    def __str__(self) -> str:
        return f"{self.name}, price: {self.price} UAH"

class User:
    def __init__(self, name: str, surname: str, numberphone: str) -> None:
        self.name: str = name
        self.surname: str = surname
        self.numberphone: str = numberphone

    def __str__(self) -> str:
        return f"{self.surname} {self.name}"

class Purchase:
    def __init__(self, user: User) -> None:
        self.products: Dict[Item, int] = {}
        self.user: User = user
        self.total: float = 0.0

    def add_item(self, item: Item, cnt: int) -> None:
        self.products[item] = self.products.get(item, 0) + cnt

    def get_total(self) -> float:
        self.total = sum(item.price * count for item, count in self.products.items())
        return self.total

    def __str__(self) -> str:
        items_str = "\n".join(f"{item.name}: {count} pcs." for item, count in self.products.items())
        return f"User: {self.user}\nItems:\n{items_str}"

if __name__ == "__main__":
    cucumbers: Item = Item("cucumbers", 20.0, "green", "small")
    tomatoes: Item = Item("tomatoes", 10.0, "red", "middle")
    print(cucumbers)

    buyer: User = User("PaPavlo", "Grushevsky", "0994428123")
    print(buyer)

    cart: Purchase = Purchase(buyer)
    cart.add_item(cucumbers, 4)
    cart.add_item(tomatoes, 20)
    print(cart)

    cart.add_item(tomatoes, 10)
    print(cart)
