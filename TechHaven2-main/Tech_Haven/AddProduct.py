class AddProduct:
    def __init__(self, img, product_id, name, description, price, form_name):
        self.__img = img
        self.__product_id = product_id
        self.__description = description
        self.__name = name
        self.__price = price
        self.__form_name = form_name

    def get_img(self):
        return self.__img

    def get_product_id(self):
        return self.__product_id

    def get_description(self):
        return self.__description

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_form_name(self):
        return self.__form_name

    def set_img(self, img):
        self.__img = img

    def set_product_id(self, product_id):
        self.__product_id = product_id

    def set_description(self, description):
        self.__description = description

    def set_form_name(self, form_name):
        self.__form_name = form_name

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price
