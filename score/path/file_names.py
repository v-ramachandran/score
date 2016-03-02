import re

def output_name_to_case_name(value):
    return re.sub("_?output\.yaml$", value, "\.yaml")

def case_name_to_output_name(value):
    return re.sub("\.yaml$",value,"_output\.yaml")

def make_assignment_case_folder(assignment_num):
    return "assignment{assignment_num}/tests/cases".format(assignment_num=assignment_num)
