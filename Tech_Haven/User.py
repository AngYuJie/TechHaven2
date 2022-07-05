class User:
    count_id = 0
    avatar = '/static/ProfilePhotos/default.jpg'
    def __init__(self, first_name, last_name, email ,street,postal_code,unit_number,mobile_number,password):
        User.count_id += 1
        self.__user_id = User.count_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password
        self.__street = street
        self.__postal_code = postal_code
        self.__unit_number = unit_number
        self.__mobile_number = mobile_number









    def __repr__(self):
        return f'<User: {self.__email}>'

    def get_user_id(self):
        return self.__user_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_password(self):
        return self.__password

    def get_email(self):
        return self.__email

    def get_street(self):
        return self.__street

    def get_postal_code(self):
        return self.__postal_code

    def get_unit_number(self):
        return self.__unit_number

    def get_mobile_number(self):
        return self.__mobile_number

    def get_full_name(self):
        return self.__first_name + " " + self.__last_name





    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name


    def set_password(self, password):
        self.__password = password

    def set_email(self, email):
        self.__email = email

    def set_street(self, street):
        self.__street = street

    def set_postal_code(self, postal_code):
        self.__postal_code = postal_code

    def set_unit_number(self, unit_number):
        self.__unit_number = unit_number

    def set_mobile_number(self, mobile_number):
        self.__mobile_number = mobile_number


