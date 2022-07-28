# CppCheck Annotation Action

![tests](https://github.com/Konstantin343/cppcheck-annotation-action/actions/workflows/test.yml/badge.svg?branch=main)


Github action, which allows you to annotate C/C++ code in a pull request with warnings, errors, etc. from [cppcheck](https://github.com/deep5050/cppcheck-action/blob/main/README.md) static analysis tool.

## Usage

**Create `.github/workflows/cppcheck-annotaion`.**  
**Add default content to it:**
```yaml
name: cppcheck-annotations

on:
  pull_request:

jobs:
  build:
    name: cppcheck-annotations
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Run cppcheck-annotation-action
        uses: Konstantin343/cppcheck-annotation-action@v1.0
        with:
          std: 'c++14'
          platform: 'unix64'
          log-level: 'verbose'

      - name: Annotate lines with errors
        uses: yuzutech/annotations-action@v0.4.0
        with:
          repo-token: "${{ secrets.GITHUB_TOKEN }}"
          title: 'Results of CppCheck'
          input: 'annotations.json'
```

### Inputs

| Input | Description | Default |
| :--- | :--- | :--- |
| **json-results-file**  | File to store results in format described on https://docs.github.com/en/rest/checks/runs#create-a-check-run--parameters |  `annotations.json` |
| **enable**  | Value for cppcheck argument --enable, comma-separated checks. See https://linux.die.net/man/1/cppcheck | `all` |
| **log-level**  | Log level for cppcheck command, possible values: `quite`, `verbose`. Other values will be ignored | ` ` |
| **std**  | C++ Standard for cppcheck command. See https://linux.die.net/man/1/cppcheck | `c++20` |
| **platform**  | Platform for cppcheck command. See https://linux.die.net/man/1/cppcheck | `unix32` |
| **suppress**  | Comma-separated suppressions for --suppress parameter. See https://linux.die.net/man/1/cppcheck | ` ` |
| **additional-args**  | Additional arguments for cppcheck command. See https://linux.die.net/man/1/cppcheck | ` ` |
| **sources**  | Path to folder with source code. See https://linux.die.net/man/1/cppcheck | `.` |
| **annotation-warnings**  | Comma-separated severities of checks of cppcheck that should be warnings in GitHub annotations. See https://linux.die.net/man/1/cppcheck | `warning` |
| **annotation-notices**  | Comma-separated severities of checks of cppcheck that should be notices in GitHub annotations. See https://linux.die.net/man/1/cppcheck | `information` |
| **annotation-failures**  | Comma-separated severities of checks of cppcheck that should be failures in GitHub annotations. See https://linux.die.net/man/1/cppcheck | `error` |
| **annotation-level-default**  | Default level for all annotations that not presented in annotation-warnings, annotation-notices, annotation-failures. Possible values: `notice`, `warning`, `failure` | `warning` |

### Outputs

Generate file with name that passed as `json-results-file` in inputs.   
This file contains json object with **GitHub Checks** annotations in format described on https://docs.github.com/en/rest/checks/runs#create-a-check-run--parameters.  
Example:
```json
[
    {
    "title": "Division by zero.",
    "message": "Division by zero.",
    "annotation_level": "failure",
    "file": "tests/test.cpp",
    "line": 14,
    "start_column": 23,
    "end_column": 23
  },
  {
    "title": "Variable 'arr[10]' is assigned a value that is never used.",
    "message": "Variable 'arr[10]' is assigned a value that is never used.",
    "annotation_level": "warning",
    "file": "tests/test.cpp",
    "line": 14,
    "start_column": 13,
    "end_column": 13
  }
]
```

## License
>MIT License

>Copyright (c) 2022 Konstantin343

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
