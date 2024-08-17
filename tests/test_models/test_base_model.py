#!/usr/bin/python3
"""Contins unittests for the class BaseModel."""

import unittest
import os
from unittest.mock import patch
from io import StringIO
from models import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test functions for the class BaseModel."""

    def tearDown(self):
        """Clean up units/files after each test."""
        pass

