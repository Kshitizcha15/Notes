class abc:
    def show(self, name):
        return f"{name} is owner of the class"

obj = abc()
print(obj.show("A"))

