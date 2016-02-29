from score.path.file_names import output_name_to_case_name
from os import path, listdir

import yaml

class ResultDigest(object):

    SCORE = "%SCORE%"
    POSSIBLE_SCORE = "%POSSIBLE_SCORE%"
    NUM_TESTS = "%NUM_TESTS%"

    CASE_NAME = "%CASE_NAME%"
    CASE_NUMBER = "%CASE_NUMBER%"
    CASE_POINTS = "%CASE_POINTS%"

    TEST_GOAL = "%TEST_GOAL%"
    DID_PASS = "%DID_PASS%"
    REQUEST = "%REQUEST%"
    RESPONSE_RECEIVED = "%RESPONSE_RECEIVED%"
    RESPONSE_EXPECTED = "%RESPONSE_EXPECTED%"

    AMENDMENT_REASON = "%AMENDMENT_REASON%"
    AMENDED_POINTS = "%AMENDED_POINTS%"

    @staticmethod
    def output_text_result_digest(output_directory_path):
        outputs = []
        cases = []
        for output_filename in listdir(output_directory_path):
            if fnmatch(output_filename, "*output.yaml"):
                case_filename = output_name_to_case_name(output_filename)
                cases.append(case_filename)
                output = yaml.load(open(path.join(output_directory_path, output_filename)))
                output.append(output)
        digest_template = yaml.load(open("digest_template.yaml"))
        digest = __generate_text_result_digest(outputs, cases)
        digest_location = path.join(output_directory_path, "results.digest")
        with open(digest_location, 'w') as digest_file:
            digest_file.write(digest)
        return digest_location

    def __generate_text_result_digest(digest_template, outputs, cases):
        summary = __generate_summary(digest_template, outputs, cases)
        cases_summary = __generate_cases_summary(digest_template, outputs, cases)
        return summary + cases_summary

    def __generate_summary(digest_template, outputs, cases):
        total_points = reduce(lambda x, y : x["points_available"] + y["points_available"], outputs)
        scored_points = reduce(lambda x, y : x["points_scored"] + y["points_scored"], outputs)
        total_cases = len(cases)

        summary = digest_template["summary"].replace(
            POSSIBLE_SCORE, total_points
        ).replace(
            SCORE, scored_points
        ).replace(
            NUM_CASES, total_cases
        )
        return summary

    def __generate_cases_summary(digest_template, outputs, cases):
        performance_header = digest_template["performance"]["header"]
        cases_summary = ""
        for output in outputs:
            if output.has_key("amended"):

            else output["passed_case"]:

            digest_template["performance"]
        return performance_header + cases_summary
