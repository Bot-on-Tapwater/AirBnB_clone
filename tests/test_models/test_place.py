import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def tearDown(self):
        self.place = None

    def test_attributes_initialization(self):
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])
        self.assertTrue(hasattr(self.place, "id"))
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))

    def test_str_method(self):
        place_str = str(self.place)
        self.assertIn("[Place]", place_str)
        self.assertIn("id", place_str)
        self.assertIn("created_at", place_str)
        self.assertIn("updated_at", place_str)

    # def test_to_dict_method(self):
    #     place_dict = self.place.to_dict()
    #     self.assertTrue(isinstance(place_dict, dict))
    #     self.assertEqual(place_dict["__class__"], "Place")
    #     self.assertEqual(self.place.__dict__, place_dict)

    def test_save_method(self):
        old_updated_at = self.place.updated_at
        self.place.save()
        new_updated_at = self.place.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)


if __name__ == "__main__":
    unittest.main()
