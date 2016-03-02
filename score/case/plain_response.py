import re

class PlainResponse(object):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return re.sub("\W", "", str(self.value)) == re.sub("\W", "", str(other.value))
