from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class concrete(Base):
    def foo(self):
        print("foo")


c = concrete()
