from main import url_cleaner

def test_strips_bracket():
    assert url_cleaner("[a]") == "a"