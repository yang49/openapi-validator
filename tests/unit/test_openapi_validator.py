import unittest
from pathlib import Path

## Add to the home path
import sys

file_path = str(Path(__file__).parent.parent.parent)
sys.path.append(file_path)

from src.openapi_validator import OpenApiValidator


class TestOpenAPIValidator(unittest.TestCase):

    def test_create_validator_with_valid_path(self):
        path = Path(__file__).with_name("openapi.yaml")
        validator = OpenApiValidator(str(path))
        self.assertIsNotNone(validator)

    def test_create_validator_with_invalid_path(self):
        with self.assertRaises(Exception):
            OpenApiValidator("random_path")

    def test_create_validator_with_invalid_yaml(self):
        path = Path(__file__).with_name("invalid_openapi.yaml")
        with self.assertRaises(Exception):
            OpenApiValidator(str(path))
