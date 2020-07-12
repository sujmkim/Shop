#USM2-Assgn-8
class FruitInfo:
    __fruit_name_list = ["Apple", "Guava", "Orange", "Grape", "Sweet Lime"]
    __fruit_price_list = [200, 80, 70, 110, 60]
    
    @staticmethod
    def get_fruit_price(fruit_name):
        if(fruit_name in FruitInfo.__fruit_name_list):
            index = FruitInfo.__fruit_name_list.index(fruit_name)
            return FruitInfo.__fruit_price_list[index]
        return -1
    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list
    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list
class Customer:
    def __init__(self, customer_name, cust_type):
        self.__customer_name = customer_name
        self.__cust_type = cust_type
    def get_customer_name(self):
        return self.__customer_name
    def get_cust_type(self):
        return self.__cust_type
class Purchase:
    __counter = 101
    def __init__(self, customer, fruit_name, quantity):
        self.__purchase_id = None
        self.__customer = customer
        self.__fruit_name = fruit_name
        self.__quantity = quantity
    def get_purchase_id(self):
        return self.__purchase_id
    def get_customer(self):
        return self.__customer
    def get_quantity(self):
        return self.__quantity
    def calculate_price(self):
        final_fruit_price = 0
        individual_fruit_price = FruitInfo.get_fruit_price(self.__fruit_name)
        #checking if the fruit exists
        if(FruitInfo.get_fruit_price(self.__fruit_name) != -1):
            #updating the total price
            final_fruit_price += FruitInfo.get_fruit_price(self.__fruit_name)*self.get_quantity()
            if(individual_fruit_price == max(FruitInfo.get_fruit_price_list()) and self.get_quantity() > 1):
                final_fruit_price = final_fruit_price - final_fruit_price*0.02
            elif(individual_fruit_price == min(FruitInfo.get_fruit_price_list()) and self.get_quantity() >= 5):
                final_fruit_price = final_fruit_price - final_fruit_price*0.05
            if(self.get_customer().get_cust_type() == "wholesale"):
                final_fruit_price = final_fruit_price - final_fruit_price*0.1
            self.__purchase_id = "P" + str(Purchase.__counter)
            Purchase.__counter += 1
            return final_fruit_price
        return -1
            
            
cust = Customer("tom", "wholesale")
purchase1 = Purchase(cust, "Apple", 5)
print(purchase1.calculate_price())    
    
'''
Created on Oct 3, 2019

@author: sujean.kim
'''
