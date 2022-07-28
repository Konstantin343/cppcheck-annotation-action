import unittest


class CppCheckAnnotationTest(unittest.TestCase):
    def test_annotations(self):
        annotations_file_content = open("annotations.json").read()
        print(annotations_file_content)
        self.assertEqual(
            annotations_file_content,
            """[
  {
    "title": "Array 'arr[5]' accessed at index 10, which is out of bounds.",
    "message": "Array 'arr[5]' accessed at index 10, which is out of bounds.",
    "annotation_level": "warning",
    "file": "/home/test/tests/a.cpp",
    "line": 14,
    "start_column": 8,
    "end_column": 8
  },
  {
    "title": "Division by zero.",
    "message": "Division by zero.",
    "annotation_level": "warning",
    "file": "/home/test/tests/a.cpp",
    "line": 2,
    "start_column": 10,
    "end_column": 10
  },
  {
    "title": "Division by zero.",
    "message": "Division by zero.",
    "annotation_level": "warning",
    "file": "/home/test/tests/a.cpp",
    "line": 4,
    "start_column": 14,
    "end_column": 14
  },
  {
    "title": "Division by zero.",
    "message": "Division by zero.",
    "annotation_level": "warning",
    "file": "/home/test/tests/a.cpp",
    "line": 6,
    "start_column": 10,
    "end_column": 10
  },
  {
    "title": "Division by zero.",
    "message": "Division by zero.",
    "annotation_level": "warning",
    "file": "/home/test/tests/a.cpp",
    "line": 14,
    "start_column": 23,
    "end_column": 23
  },
  {
    "title": "Variable 'arr[10]' is assigned a value that is never used.",
    "message": "Variable 'arr[10]' is assigned a value that is never used.",
    "annotation_level": "failure",
    "file": "/home/test/tests/a.cpp",
    "line": 14,
    "start_column": 13,
    "end_column": 13
  },
  {
    "title": "Variable 'p' is assigned a value that is never used.",
    "message": "Variable 'p' is assigned a value that is never used.",
    "annotation_level": "failure",
    "file": "/home/test/tests/a.cpp",
    "line": 22,
    "start_column": 6,
    "end_column": 6
  },
  {
    "title": "The function 'f' is never used.",
    "message": "The function 'f' is never used.",
    "annotation_level": "failure",
    "file": "/home/test/tests/a.cpp",
    "line": 12,
    "start_column": 0,
    "end_column": 0
  }
]
"""
        )


if __name__ == '__main__':
    unittest.main()
