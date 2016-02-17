from enum import Enum
from json_response import JsonResponse
from plain_response import PlainResponse

class ResponseType(Enum):
    plain = (PlainResponse)
    json = (JsonResponse)

    def __init__(self, cls):
        self.cls = cls
