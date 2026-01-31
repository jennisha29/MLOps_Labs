import pytest
from src import string_operations as so

def test_reverse_text():
    assert so.reverse_text("data science") == "ecneics atad"
    assert so.reverse_text("") == ""
    with pytest.raises(ValueError):
        so.reverse_text(123)

def test_capitalize_text():
    assert so.capitalize_text("machine learning") == "Machine learning"
    assert so.capitalize_text("mACHINE lEARNING") == "Machine learning"
    with pytest.raises(ValueError):
        so.capitalize_text(None)

def test_count_words():
    assert so.count_words("machine learning pipeline") == 3
    assert so.count_words(" one   two  three ") == 3
    assert so.count_words("") == 0
    with pytest.raises(ValueError):
        so.count_words(["not", "a", "string"])

def test_remove_duplicates():
    assert so.remove_duplicates("ml ops ml ops") == "ml ops"
    assert so.remove_duplicates("test test test test") == "test"
    assert so.remove_duplicates("") == ""
    with pytest.raises(ValueError):
        so.remove_duplicates(3.14)

def test_to_uppercase():
    assert so.to_uppercase("ml pipeline") == "ML PIPELINE"
    assert so.to_uppercase("Data 123") == "DATA 123"
    with pytest.raises(ValueError):
        so.to_uppercase(10)

def test_to_lowercase():
    assert so.to_lowercase("MACHINE LEARNING") == "machine learning"
    assert so.to_lowercase("Model 123") == "model 123"
    with pytest.raises(ValueError):
        so.to_lowercase(True)

def test_count_characters():
    assert so.count_characters("m l o p s") == 5
    assert so.count_characters("datascience") == 11
    assert so.count_characters("") == 0
    with pytest.raises(ValueError):
        so.count_characters(None)

def test_remove_spaces():
    assert so.remove_spaces("m l o p s") == "mlops"
    assert so.remove_spaces("  data   science  ") == "datascience"
    assert so.remove_spaces("") == ""
    with pytest.raises(ValueError):
        so.remove_spaces([])

def test_is_palindrome():
    assert so.is_palindrome("level") is True
    assert so.is_palindrome("never odd or even") is True
    assert so.is_palindrome("machine learning") is False
    with pytest.raises(ValueError):
        so.is_palindrome(123)

def test_title_case():
    assert so.title_case("machine learning model") == "Machine Learning Model"
    assert so.title_case("") == ""
    with pytest.raises(ValueError):
        so.title_case(123)

def test_starts_with():
    assert so.starts_with("data science pipeline", "data") is True
    assert so.starts_with("data science pipeline", "pipeline") is False
    with pytest.raises(ValueError):
        so.starts_with("mlops", 5)

def test_ends_with():
    assert so.ends_with("deploy model pipeline", "pipeline") is True
    assert so.ends_with("deploy model pipeline", "deploy") is False
    with pytest.raises(ValueError):
        so.ends_with("mlops", None)
