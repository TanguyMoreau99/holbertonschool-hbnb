#!/usr/bin/python3

import unittest
from datetime import datetime
from model.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country = Country("France")

    def test_creation_country(self):
        self.assertEqual(self.country.name, "France")

        self.assertTrue(self.country.country_id)

        self.assertIsInstance(self.country.created_at, datetime)
        self.assertIsInstance(self.country.updated_at, datetime)
        self.assertAlmostEqual((self.country.updated_at - self.country.created_at).total_seconds(), 0, delta=1)

    def test_to_dict(self):
        country_dict = self.country.to_dict()
        self.assertIsInstance(country_dict, dict)
        self.assertIn('country_id', country_dict)
        self.assertIn('name', country_dict)
        self.assertIn('created_at', country_dict)
        self.assertIn('updated_at', country_dict)

        self.assertEqual(country_dict['name'], self.country.name)
        self.assertEqual(country_dict['country_id'], self.country.country_id)
        self.assertEqual(country_dict['created_at'], self.country.created_at.isoformat())
        self.assertEqual(country_dict['updated_at'], self.country.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
