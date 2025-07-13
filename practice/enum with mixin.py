from enum import Enum

class MixinA:
    def a(self):
        print(f"{self.value}")
    
class MixinB:
    def b(self):
        print(f"{self.value}")

class ValidEnum(MixinA,MixinB,int,Enum):
    MEMBER = 10

print(ValidEnum.MEMBER.name)
print(ValidEnum.MEMBER.value)
ValidEnum.MEMBER.a()
ValidEnum.MEMBER.b()
# print(ValidEnum.MEMBER.upper())