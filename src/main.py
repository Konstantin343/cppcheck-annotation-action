import os
import subprocess
import xml.etree.ElementTree as ElementTree
import json

# Input parameters from GitHub Action
INPUT_JSON_RESULTS_FILE = os.getenv("INPUT_JSON-RESULTS-FILE")
INPUT_ENABLE = os.getenv("INPUT_ENABLE")
INPUT_LOG_LEVEL = os.getenv("INPUT_LOG-LEVEL")
INPUT_STD = os.getenv("INPUT_STD")
INPUT_PLATFORM = os.getenv("INPUT_PLATFORM")
INPUT_SUPPRESS = os.getenv("INPUT_SUPPRESS")
INPUT_SOURCES = os.getenv("INPUT_SOURCES")
INPUT_ADDITIONAL_ARGS = os.getenv("INPUT_ADDITIONAL-ARGS")
INPUT_ANNOTATION_WARNINGS = os.getenv("INPUT_ANNOTATION-WARNINGS")
INPUT_ANNOTATION_NOTICES = os.getenv("INPUT_ANNOTATION-NOTICES")
INPUT_ANNOTATION_FAILURES = os.getenv("INPUT_ANNOTATION-FAILURES")
INPUT_ANNOTATION_LEVEL_DEFAULT = os.getenv("INPUT_ANNOTATION-LEVEL-DEFAULT")

# Constants
EXECUTABLE = "cppcheck"
OUTPUT_FILE = "cppcheck-results.xml"


def get_annotation_level(severity):
    if severity in INPUT_ANNOTATION_NOTICES.split(","):
        return "notice"
    if severity in INPUT_ANNOTATION_WARNINGS.split(","):
        return "warning"
    if severity in INPUT_ANNOTATION_FAILURES.split(","):
        return "failure"

    return INPUT_ANNOTATION_LEVEL_DEFAULT


def get_args():
    args = ["--xml", f'--output-file={OUTPUT_FILE}']

    log_level = INPUT_LOG_LEVEL
    if log_level in ["verbose", "quiet"]:
        args.append(f'--{log_level}')

    if INPUT_SUPPRESS != "":
        suppressions = INPUT_SUPPRESS.split(",")
        for suppression in suppressions:
            args.append(f'--suppress={suppression}')

    if INPUT_ENABLE != "":
        args.append(f'--enable={INPUT_ENABLE}')

    if INPUT_STD != "":
        args.append(f'--std={INPUT_STD}')

    if INPUT_PLATFORM != "":
        args.append(f'--platform={INPUT_PLATFORM}')

    if INPUT_ADDITIONAL_ARGS != "":
        additional_args = filter(lambda arg: arg != "", INPUT_ADDITIONAL_ARGS.split(" "))
        args.extend(additional_args)

    if INPUT_SOURCES != "":
        args.append(INPUT_SOURCES)

    return args


def parse_cppcheck_xml(reportFile):
    root = ElementTree.parse(reportFile).getroot()
    errors = root.find("errors").findall("error")
    annotations = []
    for error in errors:
        print(error.attrib)
        location = error.find("location")
        if location is None:
            continue
        annotations.append({
            "title": error.get("msg"),
            "message": error.get("verbose").replace(". ", ".\n"),
            "annotation_level": get_annotation_level(error.get("severity")),
            "file": location.get("file"),
            "line": int(location.get("line")),
            "start_column": int(location.get("column")),
            "end_column": int(location.get("column"))
        })
    return annotations


def main():
    command = (EXECUTABLE, *get_args())
    cppcheckResult = subprocess.run(command, capture_output=True, check=False)
    print("CMD:\n ", *cppcheckResult.args)

    if cppcheckResult.returncode != 0:
        print("STDOUT:\n ", cppcheckResult.stdout.decode("utf-8"))
        print("STDERR:\n ", cppcheckResult.stderr.decode("utf-8"))
        return cppcheckResult.returncode

    annotations = parse_cppcheck_xml(OUTPUT_FILE)
    print(json.dumps(annotations, indent=2), file=open(INPUT_JSON_RESULTS_FILE, "w"))
    print(json.dumps(annotations, indent=2))

    if any(filter(lambda a: a["annotation_level"] == "failure", annotations)):
        return 1


if __name__ == '__main__':
    main()
