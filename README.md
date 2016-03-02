# scale 

scale is a suite of auto-grading tools built to efficiently grade submissions in UT Austin's Modern Web Applications course. 

## Purpose

## Usage
### Components
This package offers four main pieces of functionality: retrieving submissions, setting up a tests project, executing test cases, and generating a digest out of the test case execution output.

#### pull_submissions

```
usage: pull_submissions [-h] [-a ASSIGNMENT] [-s STUDENTS_FILE] [-d DIRECTORY]
                        [-i INSTRUCTOR]

optional arguments:
  -h, --help            show this help message and exit
  -a ASSIGNMENT, --assignment ASSIGNMENT
                        Specify the assignment number for which code should be
                        pulled
  -s STUDENTS_FILE, --students_file STUDENTS_FILE
                        Provide the path to the YAML file containing student
                        names, ids, and bitbucket ids.
  -d DIRECTORY, --directory DIRECTORY
                        Specify the location to which the assignments should
                        be pulled. DEFAULT: './assignments'
  -i INSTRUCTOR, --instructor INSTRUCTOR
                        Specify the instructor's bitbucket id.
```

#### make_test_skeleton

usage: make_test_skeleton [-h] [-p PATH] [-o] [-n NAME] [-s SOURCE]
                          [-a ASSIGNMENT]

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Specify directory(-ies) in which to create the
                        skeleton. Can be a pattern. DEFAULT: '.'
  -o, --overwrite       Overwrite any existing test folder with the same
                        source path and name.
  -n NAME, --name NAME  Specify the name of the test skeleton folder to be
                        created. DEFAULT: 'tests'
  -s SOURCE, --source SOURCE
                        Specify the source git clone URL from which to clone
                        and extract cases.
  -a ASSIGNMENT, --assignment ASSIGNMENT
                        Specify the assignment number for which code should be
                        pulled

#### run_test_cases

The run_test_cases utility can be used to execute a set of test cases against a given application hosted at a specified URL. 

```
usage: run_test_cases [-h] [-r ROOT] [-n NAME] [-p PREPARE] [-t TIMEOUT]
                      [-u URL] [-c CASE]

optional arguments:
  -h, --help            show this help message and exit
  -r ROOT, --root ROOT  Specify the root for the execution of test cases. Can
                        be a pattern. DEFAULT: '.'
  -n NAME, --name NAME  Specify the name of the test cases folder. DEFAULT:
                        'tests'
  -p PREPARE, --prepare PREPARE
                        Specify a command if a web application needs to be
                        prepared for test.
  -t TIMEOUT, --timeout TIMEOUT
                        Specify the seconds to wait if a web application needs
                        to be prepared. DEFAULT: '60'
  -u URL, --url URL     Specify the URL to which requests will be made.
                        DEFAULT: 'http://localhost:8080'
  -c CASE, --case CASE  Specify the name of the individual test case to run.
```
#### generate_digest

```
usage: generate_digest [-h] [-a ASSIGNMENT] [-p PATH] [-n NAME]

optional arguments:
  -h, --help            show this help message and exit
  -a ASSIGNMENT, --assignment ASSIGNMENT
                        Specify the assignment number for which the digest is
                        generated.
  -p PATH, --path PATH  Specify directory(-ies) in which to create digests.
                        Can be a pattern. DEFAULT: '.'
  -n NAME, --name NAME  Specify the name of the tests folder to parse results.
                        DEFAULT: 'tests'
```

## Verification

