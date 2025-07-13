from abc import ABC,abstractmethod

class Polygon(ABC):
    
    @abstractmethod
    def noofsides(self):
        pass

    @abstractmethod
    def noofcorners(self):
        pass

class Triangle(Polygon):

    def noofsides(self):
        return "3 sides"

    def noofcorners(self):
        return "3 corners"

class Square(Polygon):

    def noofsides(self):
        return "4 sides"

    def noofcorners(self):
        return "4 corners"

def main():
    t = Triangle()
    print(t.noofsides())
    print(t.noofcorners())

    s = Square()
    print(s.noofsides())
    print(s.noofcorners())

if __name__ == "__main__":
    main()
