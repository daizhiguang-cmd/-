import random

class Codes(object):
    def __init__(self):
        re = ""
        for i in range(6):
            num = random.randint(0,9)
            re += str(num)
        self.result = re
