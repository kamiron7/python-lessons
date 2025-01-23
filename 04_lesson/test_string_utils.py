import pytest
from StringUtils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


@pytest.mark.positive_test
@pytest.mark.parametrize('string, result', [
    ("skypro", "Skypro"),
    ("Skypro", "Skypro"),
    ("", ""),
    ("123", "123")
])
def test_capitilize_positive(utils, string, result):
    assert utils.capitilize(string) == result


@pytest.mark.negative_test
@pytest.mark.parametrize('string', [
    None,
    123,
    ["skypro"],
    {"key": "value"}
])
def test_capitilize_negative(utils, string):
    with pytest.raises(AttributeError):
        utils.capitilize(string)


@pytest.mark.positive_test
@pytest.mark.parametrize('string, result', [
    ("   skypro", "skypro"),
    ("skypro", "skypro"),
    ("   ", ""),
    ("", "")
])
def test_trim_positive(utils, string, result):
    assert utils.trim(string) == result


@pytest.mark.negative_test
@pytest.mark.parametrize('string', [
    None,
    123,
    ["   skypro"],
    {"key": "value"}
])
def test_trim_negative(utils, string):
    with pytest.raises(AttributeError):
        utils.trim(string)


@pytest.mark.positive_test
@pytest.mark.parametrize('string, delimeter, result', [
    ("a,b,c,d", ",", ["a", "b", "c", "d"]),
    ("1:2:3", ":", ["1", "2", "3"]),
    ("", ",", []),
    ("skypro", ",", ["skypro"])
])
def test_to_list_positive(utils, string, delimeter, result):
    assert utils.to_list(string, delimeter) == result


@pytest.mark.negative_test
@pytest.mark.parametrize('string, delimeter', [
    (None, ","),
    (123, ","),
    (["a,b,c"], ",")
])
def test_to_list_negative(utils, string, delimeter):
    with pytest.raises((AttributeError, TypeError)):
        utils.to_list(string, delimeter)


@pytest.mark.positive_test
@pytest.mark.parametrize('string, symbol, result', [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("", "S", False)
])
def test_contains_positive(utils, string, symbol, result):
    assert utils.contains(string, symbol) == result


@pytest.mark.negative_test
@pytest.mark.parametrize('string, symbol', [
    (None, "S"),
    ("SkyPro", None),
    (123, "S"),
    ("SkyPro", 123)
])
def test_contains_negative(utils, string, symbol):
    with pytest.raises((AttributeError, TypeError)):
        utils.contains(string, symbol)


@pytest.mark.positive_test
@pytest.mark.parametrize('string, symbol, result', [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("SkyPro", "X", "SkyPro"),
    ("", "S", "")
])
def test_delete_symbol_positive(utils, string, symbol, result):
    assert utils.delete_symbol(string, symbol) == result


@pytest.mark.negative_test
@pytest.mark.parametrize('string, symbol', [
    (None, "S"),
    ("SkyPro", None),
    (123, "S"),
    ("SkyPro", 123)
])
def test_delete_symbol_negative(utils, string, symbol):
    with pytest.raises((AttributeError, TypeError)):
        utils.delete_symbol(string, symbol)


@pytest.mark.positive_test
@pytest.mark.parametrize('string, symbol, result', [
    ("SkyPro", "S", True),
    ("SkyPro", "P", False),
    ("", "S", False)
])
def test_starts_with(utils, string, symbol, result):
    assert utils.starts_with(string, symbol) == result


@pytest.mark.positive_test
@pytest.mark.parametrize('string, symbol, result', [
    ("SkyPro", "o", True),
    ("SkyPro", "y", False),
    ("", "o", False)
])
def test_end_with(utils, string, symbol, result):
    assert utils.end_with(string, symbol) == result


@pytest.mark.positive_test
@pytest.mark.parametrize('string, result', [
    ("", True),
    (" ", True),
    ("SkyPro", False)
])
def test_is_empty(utils, string, result):
    assert utils.is_empty(string) == result


@pytest.mark.positive_test
@pytest.mark.parametrize('lst, joiner, result', [
    ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
    (["Sky", "Pro"], ", ", "Sky, Pro"),
    (["Sky", "Pro"], "-", "Sky-Pro"),
    ([], ", ", "")
])
def test_list_to_string(utils, lst, joiner, result):
    assert utils.list_to_string(lst, joiner) == result
