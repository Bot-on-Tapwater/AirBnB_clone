import unittest
from models.state import State

class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def tearDown(self):
        self.state = None

    def test_attributes_initialization(self):
        self.assertEqual(self.state.name, "")
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_str_method(self):
        state_str = str(self.state)
        self.assertIn("[State]", state_str)
        self.assertIn("id", state_str)
        self.assertIn("created_at", state_str)
        self.assertIn("updated_at", state_str)

    # def test_to_dict_method(self):
    #     state_dict = self.state.to_dict()
    #     self.assertTrue(isinstance(state_dict, dict))
    #     self.assertEqual(state_dict["__class__"], "State")
    #     self.assertEqual(self.state.__dict__, state_dict)

    def test_save_method(self):
        old_updated_at = self.state.updated_at
        self.state.save()
        new_updated_at = self.state.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

if __name__ == "__main__":
    unittest.main()
