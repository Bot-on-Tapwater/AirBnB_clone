import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def tearDown(self):
        self.review = None

    def test_attributes_initialization(self):
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))

    def test_str_method(self):
        review_str = str(self.review)
        self.assertIn("[Review]", review_str)
        self.assertIn("id", review_str)
        self.assertIn("created_at", review_str)
        self.assertIn("updated_at", review_str)

    # def test_to_dict_method(self):
    #     review_dict = self.review.to_dict()
    #     self.assertTrue(isinstance(review_dict, dict))
    #     self.assertEqual(review_dict["__class__"], "Review")
    #     self.assertEqual(self.review.__dict__, review_dict)

    def test_save_method(self):
        old_updated_at = self.review.updated_at
        self.review.save()
        new_updated_at = self.review.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

if __name__ == "__main__":
    unittest.main()
