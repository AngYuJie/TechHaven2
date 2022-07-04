class Feedback:
    def __init__(self, first_name, last_name, email, subject, inquiry, feedback_id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__subject = subject
        self.__inquiry = inquiry
        self.__feedback_id = feedback_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_subject(self):
        return self.__subject

    def get_inquiry(self):
        return self.__inquiry

    def get_feedback_id(self):
        return self.__feedback_id
