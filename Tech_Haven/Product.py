class Product:
    def __init__(self, product_id, quantity):
        self.__product_id = product_id
        # self.__name = name
        self.__quantity = quantity
        # self.__price = price


    # def __str__(self):
    #     return f'Product: {self.__name}, Price: {self.__price}'

    def get_product_id(self):
        return self.__product_id

    # def get_name(self):
    #     return self.__name

    def get_quantity(self):
        return self.__quantity

    # def get_price(self):
    #     return self.__price


    def set_product_id(self, product_id):
        self.__product_id = product_id
    #
    # def set_name(self, name):
    #     self.__name = name

    def set_quantity(self, quantity):
        self.__quantity = quantity

    # def set_price(self, price):
    #     self.__price = price
