
import string
import random

class Helper:
    @staticmethod
    def generate_email():
        s = ''
        for i in range(10):
            s += random.choice(string.ascii_letters)


        return f"anastasiya+{s}@ya.ru"

    @staticmethod
    def generate_password():

        f = ''
        for i in range(7):
            f += random.choice(string.digits)

        return f