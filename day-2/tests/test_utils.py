from day_2.utils import is_invalid, find_invalid_codes

def test_is_invalid():
    assert is_invalid("3") == False
    assert is_invalid("11") == True

def test_find_invalid_codes():
    assert find_invalid_codes("11-22") == 33
