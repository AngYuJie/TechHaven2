class Review:
    count_id = 0
    def __init__(self, rating, title, review, user_object):
        Review.count_id += 1
        self.__review_id = Review.count_id
        self.__rating = rating
        self.__title = title
        self.__review = review
        self.__user_object = user_object

    def get_review_id(self):
        return self.__review_id
    def get_rating(self):
        return self.__rating
    def get_title(self):
        return self.__title
    def get_review(self):
        return self.__review
    def get_user_object(self):
        return self.__user_object

    def set_review_id(self, review_id):
        self.__review_id = review_id
    def set_rating(self, rating):
        self.__rating = rating
    def set_title(self, title):
        self.__title = title
    def set_review(self, review):
        self.__review = review
    def set_user_object(self, user_object):
        self.__user_object = user_object
