#!/usr/bin/python3
import unittest
from model.amenity import Amenity
import uuid
from datetime import datetime

class TestAmenity(unittest.TestCase):

    def test_creation_amenity(self):
        amenity_name = "Swimming Pool"
        amenity = Amenity(amenity_name)

        self.assertEqual(amenity.name, amenity_name)

        self.assertTrue(uuid.UUID(amenity.amenity_id))

        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)

def test_to_dict(self):
        amenity = Amenity()
        amenity.amenity_id = 'db8e1524-2ebf-4b71-9212-e372623907bc'
        amenity.name = 'Gym'
        amenity.created_at = datetime.datetime(2024, 6, 16, 11, 3, 23, 883774)
        amenity.updated_at = datetime.datetime(2024, 6, 16, 11, 3, 23, 883775)

        amenity_dict = amenity.to_dict()

        self.assertIsInstance(amenity_dict, dict)
        self.assertIn('amenity_id', amenity_dict)
        self.assertIn('name', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)
        self.assertEqual(amenity_dict['name'], amenity.name)
        self.assertEqual(amenity_dict['amenity_id'], amenity.amenity_id)
        self.assertEqual(amenity_dict['created_at'], amenity.created_at.isoformat())
        self.assertEqual(amenity_dict['updated_at'], amenity.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
