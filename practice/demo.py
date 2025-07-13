class DemoClass:
    def instance_method(self):
        return ("instance method called", self)
    
    @classmethod
    def class_method(cls):
        return ("Class method called", cls)

    @staticmethod
    def static_method():
        return ("static method called",)

print(DemoClass.static_method())