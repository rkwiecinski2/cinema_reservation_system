from movie import Movie



class The_Green_Mile(Movie):

    @staticmethod
    def get_name():
        return "The Green Mile"

    @staticmethod
    def seating_plan():
        return range(1, 26), "ABCDEGHIKLMNOP"