#!/usr/bin/python3
"""Module contains unittests for the class FileStorage."""

import unittest
import os
from io import StringIO
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test functions for the class FileStorage."""

    def setUp(self):
        """Set up the test environment before each test."""
        # clear __objects and remove file.json if it exists before each test
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def tearDown(self):
        """Clean up units/files after each test."""
        # Clear __objects and remove file.json after each test
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_new(self):
        """Test the new() method of class FileStorage."""
        self.assertEqual(storage.all(), {})
        model = BaseModel()
        storage.new(model)
        key = f"BaseModel.{model.id}"
        self.assertIn(key, storage.all())

    def test_save(self):
        """Test the save() method of FileStorage."""
        model = BaseModel()
        storage.new(model)
        storage.save()
        self.assertTrue(os.path.exists(storage._FileStorage__file_path))

    def test_reload(self):
        """Test the reload() method of FileStorage."""
        model = BaseModel()
        storage.new(model)
        storage.save()
        storage._FileStorage__objects = {}
        storage.reload()
        key = f"BaseModel.{model.id}"
        self.assertIn(key, storage.all())

    def test_all(self):
        """Test the all() method of FileStorage."""
        model = BaseModel()
        storage.new(model)
        objects = storage.all()
        self.assertIsInstance(objects, dict)
        self.assertIn(f"BaseModel.{model.id}", objects)


if __name__ == '__main__':
    unittest.main()
