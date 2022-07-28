import subprocess
import xml.etree.ElementTree as ElementTree
import json


def main():
    print(subprocess.run((
        "cppcheck",
        "--xml",
        "--output-file=report.xml",
        "--enable=all",
        "--suppress=missingIncludeSystem",
        "/github/workspace/tests/a.cpp"
    ), capture_output=True, check=False).stdout)

    root = ElementTree.parse('report.xml').getroot()
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
            "annotation_level": "failure",
            "file": location.get("file"),
            "line": int(location.get("line")),
            "start_column": int(location.get("column")),
            "end_column": int(location.get("column"))
        })
    print(json.dumps(annotations, indent=2), file=open("annotations.json", "w"))


if __name__ == '__main__':
    main()
