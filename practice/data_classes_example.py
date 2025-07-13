from dataclasses import dataclass, field, fields
# from typing import List
from math import asin, cos, radians, sin, sqrt
from pympler import asizeof


@dataclass
class Position:
    name: str
    lat: float = field(default=0.0, repr=True, metadata={"unit": "degrees"})
    lon: float = 0.0

    def distance_to(self, other):
        r = 6371  # Earth radius in kilometers
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (
            sin((phi_2 - phi_1) / 2) ** 2
            + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2) ** 2
        )
        return 2 * r * asin(sqrt(h))


oslo = Position("Oslo", 10.8, 59.9)
vancouver = Position("Vancouver", -123.1, 49.3)
print(oslo.distance_to(vancouver))
print(oslo)
print(type(fields(oslo)))
print(fields(oslo)[1].default)
print(type(fields(oslo)[1]))


@dataclass
class Capital(Position):
    country: str = "Unknown"


madrid = Capital("Madrid", country="Spain")
print(madrid)


@dataclass
class SlotSimple:
    __slots__ = ["name", "lat", "lon"]
    name: str
    lat: float
    lon: float


slot = SlotSimple("Madrid", -3.7, 40.4)

print(asizeof.asizeof(slot))
print(asizeof.asizeof(oslo))
