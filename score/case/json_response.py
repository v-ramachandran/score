from jsoncompare import jsoncompare

import json

class JsonResponse(object):
    def __init__(self, value):
        if isinstance(value, basestring):
            try:
                self.json = json.loads(value)
            except ValueError as exception:
                self.json = {}
        else:
            self.json = value

    def __eq__(self, other):
        return jsoncompare.are_same(self.json, other.json)[0]
