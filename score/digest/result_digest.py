from score.path.file_names import output_filename_to_case_name
from os import path, listdir
from fnmatch import fnmatch

import pkg_resources
import yaml

ASSIGNMENT_ID = "%ASSIGNMENT_ID%"
SCORE = "%SCORE%"
POSSIBLE_SCORE = "%POSSIBLE_SCORE%"
NUM_TESTS = "%NUM_TESTS%"

CASE_NAME = "%CASE_NAME%"
CASE_NUMBER = "%CASE_NUMBER%"
CASE_SCORE = "%CASE_SCORE%"
CASE_POINTS = "%CASE_POINTS%"
GOAL = "%GOAL%"

FAILURE_REASON = "%FAILURE_REASON%"

def __generate_text_result_digest(digest_template, outputs, cases, assignment_id):
    summary = __generate_summary(digest_template, outputs, cases, assignment_id)
    cases_summary = __generate_cases_summary(digest_template, outputs, cases)
    return summary + cases_summary

def output_text_result_digest(output_directory_path, assignment_id):
    outputs = []
    cases = []
    for output_filename in listdir(output_directory_path):
        if fnmatch(output_filename, "*output.yaml"):
            case_name = output_filename_to_case_name(output_filename)
            cases.append(case_name)
            output = yaml.load(open(path.join(output_directory_path, output_filename)))
            outputs.append(output)
    digest_template = yaml.load(pkg_resources.resource_string(__name__, 'digest_template.yaml'))

    digest = __generate_text_result_digest(digest_template, outputs, cases, assignment_id)
    digest_location = path.join(output_directory_path, "results.digest")
    with open(digest_location, 'w') as digest_file:
        digest_file.write(digest)
    return digest_location

def __generate_summary(digest_template, outputs, cases, assignment_id):
    total_points = reduce(lambda x, y : x + y["points_available"], outputs, 0)
    scored_points = reduce(lambda x, y : x + y["points_scored"], outputs, 0)
    total_cases = len(cases)

    summary = digest_template["summary"].replace(
        POSSIBLE_SCORE, str(total_points)
    ).replace(
        SCORE, str(scored_points)
    ).replace(
        NUM_TESTS, str(total_cases)
    ).replace(
        ASSIGNMENT_ID, assignment_id
    )
    return summary

def __generate_cases_summary(digest_template, outputs, cases):
    performance_header = digest_template["performance"]["header"]
    cases_summary = ""
    for idx, (output, case) in enumerate(zip(outputs, cases)):
        cases_summary += digest_template["performance"]["case_result"].replace(
            CASE_NAME, case
        ).replace(
            CASE_NUMBER, str(idx)
        ).replace(
            CASE_SCORE, str(output['points_scored'])
        ).replace(
            CASE_POINTS, str(output['points_available'])
        ).replace(
            GOAL, output['goal'].rstrip(".")
        )
        if output.has_key('reason'):
            cases_summary += digest_template["performance"]["failure"].replace(
                FAILURE_REASON, output["reason"]
            )
    return performance_header + cases_summary
