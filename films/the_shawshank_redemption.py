from movie import Movie

class The_Shawshank_Redemption(Movie):

    @staticmethod
    def get_name():
        return "The Shawskank Redemption"

    @staticmethod
    def seating_plan():
        return range(1, 26), "ABCDEGHI"