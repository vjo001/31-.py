class parent():
    
    def __init__(self):
        print("This is the Parent Class")
        
    def menu(dish):
        if dish == "Ice Cream":
            print("You May Add The Following Toppings")
            print("Whipped Cream | Choco Syrup | Cherry")
        elif dish == "Mango Juice":
            print("You May Add The Following Toppings")
            print("Extra Mangoes | Mango-Designed Straw")
        else:
            print("PLEASE ENTER A VALID DISH")
            
    def final_amount(dish, add_ons):
        if dish == "Ice Cream" and add_ons == "Cherry":
            print("Total Cost: $5.50")
        elif dish == "Ice Cream" and add_ons == "Choco Syrup":
            print("Total Cost: $5.50")
        elif dish =="Mango Juice" and add_ons == "Extra Mangoes":
            print("Total Cost: $2.50")
        elif dish == "Mango Juice" and add_ons == "Mango-Degisned Straw":
            print("Total Cost: $2.25")
            
class child1 (parent):
    
    def __init__(self, dish):
        self.new_dish = dish
        
    def get_menu(self):
        parent.menu(self.new_dish)
        
class child2 (parent):
    
    def __init__(self,dish,addons):
        self.new_dish = dish
        self.addons = addons
        
    def get_final_amount(self):
        parent.final_amount(self.new_dish,self.addons)
        
child1_object = child1("Ice Cream")
child1_object.get_menu()

child2_object = child2("Ice Cream","Choch Syrup")
child2_object.get_final_amount()