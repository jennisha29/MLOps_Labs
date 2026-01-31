import unittest
from src import string_operations as so

class TestStringOperations(unittest.TestCase):

    def test_reverse_text(self):
        self.assertEqual(so.reverse_text("data science"), "ecneics atad")
        self.assertEqual(so.reverse_text(""), "")
        with self.assertRaises(ValueError):
            so.reverse_text(123)

    def test_capitalize_text(self):
        self.assertEqual(so.capitalize_text("machine learning"), "Machine learning")
        self.assertEqual(so.capitalize_text("mACHINE lEARNING"), "Machine learning")
        with self.assertRaises(ValueError):
            so.capitalize_text(None)

    def test_count_words(self):
        self.assertEqual(so.count_words("machine learning pipeline"), 3)
        self.assertEqual(so.count_words(" one   two  three "), 3)
        self.assertEqual(so.count_words(""), 0)
        with self.assertRaises(ValueError):
            so.count_words(["not", "a", "string"])

    def test_remove_duplicates(self):
        self.assertEqual(so.remove_duplicates("ml ops ml ops"), "ml ops")
        self.assertEqual(so.remove_duplicates("test test test test"), "test")
        self.assertEqual(so.remove_duplicates(""), "")
        with self.assertRaises(ValueError):
            so.remove_duplicates(3.14)

    def test_to_uppercase(self):
        self.assertEqual(so.to_uppercase("ml pipeline"), "ML PIPELINE")
        self.assertEqual(so.to_uppercase("Data 123"), "DATA 123")
        with self.assertRaises(ValueError):
            so.to_uppercase(10)

    def test_to_lowercase(self):
        self.assertEqual(so.to_lowercase("MACHINE LEARNING"), "machine learning")
        self.assertEqual(so.to_lowercase("Model 123"), "model 123")
        with self.assertRaises(ValueError):
            so.to_lowercase(True)

    def test_count_characters(self):
        self.assertEqual(so.count_characters("m l o p s"), 5)
        self.assertEqual(so.count_characters("datascience"), 11)
        self.assertEqual(so.count_characters(""), 0)
        with self.assertRaises(ValueError):
            so.count_characters(None)

    def test_remove_spaces(self):
        self.assertEqual(so.remove_spaces("m l o p s"), "mlops")
        self.assertEqual(so.remove_spaces("  data   science  "), "datascience")
        self.assertEqual(so.remove_spaces(""), "")
        with self.assertRaises(ValueError):
            so.remove_spaces([])

    def test_is_palindrome(self):
        self.assertTrue(so.is_palindrome("level"))
        self.assertTrue(so.is_palindrome("never odd or even"))
        self.assertFalse(so.is_palindrome("machine learning"))
        with self.assertRaises(ValueError):
            so.is_palindrome(123)

    def test_title_case(self):
        self.assertEqual(so.title_case("machine learning model"), "Machine Learning Model")
        self.assertEqual(so.title_case(""), "")
        with self.assertRaises(ValueError):
            so.title_case(123)

    def test_starts_with(self):
        self.assertTrue(so.starts_with("data science pipeline", "data"))
        self.assertFalse(so.starts_with("data science pipeline", "pipeline"))
        with self.assertRaises(ValueError):
            so.starts_with("mlops", 5)

    def test_ends_with(self):
        self.assertTrue(so.ends_with("deploy model pipeline", "pipeline"))
        self.assertFalse(so.ends_with("deploy model pipeline", "deploy"))
        with self.assertRaises(ValueError):
            so.ends_with("mlops", None)


if __name__ == "__main__":
    unittest.main()
