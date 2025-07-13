from dataclasses import dataclass
from pympler import asizeof
@dataclass
class Position:
    __slots__ = ['name','lon','lat']
    name: str
    lon: float
    lat: float

@dataclass
class Capital(Position):
    country: str

pos = Capital('Oslo',10.8,59.9,"Norway")
print(pos)

print(asizeof.asizesof(pos))