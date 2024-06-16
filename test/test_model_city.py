#!/usr/bin/python3
import unittest
from model.city import City
import uuid
from datetime import datetime

class TestCity(unittest.TestCase):

    def test_creation_city(self):
        city_name = "Paris"
        country_id = "country123"
        city = City(city_name, country_id)

        self.assertEqual(city.name, city_name)
        self.assertEqual(city.country_id, country_id)

        self.assertTrue(uuid.UUID(city.city_id))

        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)

    def test_to_dict(self):
        city = City("New York", "country456")

        city_dict = city.to_dict()

        self.assertIsInstance(city_dict, dict)
        self.assertIn('city_id', city_dict)
        self.assertIn('name', city_dict)
        self.assertIn('country_id', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)
        self.assertEqual(city_dict['name'], city.name)
        self.assertEqual(city_dict['city_id'], city.city_id)
        self.assertEqual(city_dict['country_id'], city.country_id)
        self.assertEqual(city_dict['created_at'], city.created_at.isoformat())
        self.assertEqual(city_dict['updated_at'], city.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
