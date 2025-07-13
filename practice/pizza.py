from collections import namedtuple
import math

BasePizza = namedtuple(
    "BasePizza", ["toppings"], defaults=[[]]
)


class Pizza(BasePizza):

    @classmethod
    def margherita(cls):
        return cls(toppings=["mozzarella", "tomatoes"])


    @classmethod
    def prosciutto(cls):
        return cls(["mozzarella", "tomatoes", "ham"])


    @staticmethod
    def get_size_in_inches(size):
        size_map = {
            "small": 8,
            "medium": 12,
            "large": 16,
        }
        return size_map.get(size, "unknown size")
    

    @staticmethod
    def get_area(radius):
        return math.pi * pow(radius, 2)
    

    def add_toppings(self, topping):
        self.toppings.append(topping)

    def remove_toppings(self, topping):
        if topping in self.toppings:
            self.toppings.remove(topping)


pizza = Pizza()
pizza.add_toppings("garlic")
pizza.remove_toppings("cheese")
print(pizza)

margherita = pizza.margherita()

margherita.add_toppings("cheese")
print(margherita)

print(f"{Pizza.get_area(margherita.get_size_in_inches("large")):.2f}")
