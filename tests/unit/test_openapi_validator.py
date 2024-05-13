import unittest
from pathlib import Path

import sys
print(sys.path)

from src.openapi_validator import OpenApiValidator

class TestOpenAPIValidator(unittest.TestCase):

    def test_validate_request(self):
        path = Path(__file__).with_name('openapi.yaml')
        validator = OpenApiValidator(str(path))
        self.assertIsNotNone(validator)
        