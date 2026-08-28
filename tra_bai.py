#Bai 1:
a = input("Nhập chuỗi kí tự: ")
b = list(a)
tra_ve = []
def sort(*s):
    
    if len(s) == 1:
        return s[0]
    else:
        for i in range(len(s)**4):


print(a, "có các hoán vị là", sort(b))



# #bài 2:
class BeverageStore:
    def __init__(self, name, inventory):
        self.name = name
        Self.invetory = inventory

    def calculate_price(quantity)
        pass

    def show()
        pass

    def required_ingredients(quantity)
        pass

class CoffeeStore(BeverageStore):
    super