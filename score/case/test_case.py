from response_type import ResponseType
from os import path

import requests
import yaml
from yaml.representer import SafeRepresenter
import re

class folded_str(str): pass
class literal_str(str): pass

def change_style(style, representer):
    def new_representer(dumper, data):
        scalar = representer(dumper, data)
        scalar.style = style
        return scalar
    return new_representer

represent_folded_str = change_style('>', SafeRepresenter.represent_str)
represent_literal_str = change_style('|', SafeRepresenter.represent_str)
yaml.add_representer(folded_str, represent_folded_str)
yaml.add_representer(literal_str, represent_literal_str)

class TestCase(object):

    def __init__(self, url_root, case, output_filepath):
        self.url_root = url_root
        self.output_filepath = output_filepath
        self.case = case

    @classmethod
    def from_yaml_file(cls, url_root, case_filepath, output_directory_path):
        name, extension = path.splitext(case_filepath)
        output_filename = "{base}_output.yaml".format(base=path.basename(name))
        output_filepath = path.join(output_directory_path, output_filename)
        case = yaml.load(open(case_filepath))
        return cls(url_root, case, output_filepath)

    def evaluate_and_output_results(self):
        output_dict = {"points_available": self.case["points"], "responses":[],
            "goal": literal_str(self.case["goal"])}
        scored_points = self.case["points"]
        for request in self.case["requests"]:
            response_dict = self.__execute_request(request)
            output_dict["responses"].append(response_dict)
            if response_dict.has_key("correct_response") and not response_dict["correct_response"]:
                scored_points = 0
        if self.case.has_key("compare_responses"):
            output_dict["points_scored"] = scored_points
        with open(self.output_filepath, 'w') as yaml_file:
            yaml_file.write(yaml.dump(output_dict,  default_flow_style=False))
        return self.output_filepath

    def __execute_request(self,request):
        request_url = self.url_root + "/" + request["request"].lstrip("/")
        http_response = requests.get(url=request_url)
        if request.has_key("status_code_expected"):
            status_code = request["status_code_expected"]
        else:
            status_code = 200
        output_dict = {"request": request["request"],
            "status_code_expected": status_code,
            "status_code_received": http_response.status_code}

        if request.has_key("response_expected"):
            output_dict["response_expected"] = request["response_expected"]["value"]
            received_response = re.sub("[ \r]+\n", '\n', http_response.content)
            output_dict["response_received"] = received_response
            expected_response_type = request["response_expected"]["type"].lower()
            response_type_cls = ResponseType[expected_response_type].cls
            output_dict["response_received_matches"] = (
                response_type_cls(output_dict["response_expected"]) ==
                response_type_cls(output_dict["response_received"]))
            output_dict["response_expected"] = literal_str(output_dict["response_expected"])
            output_dict["response_received"] = literal_str(output_dict["response_received"])
            if self.case.has_key("compare_responses"):
                output_dict["correct_response"] = (status_code == http_response.status_code) and (
                    output_dict["response_received_matches"])
        return output_dict
