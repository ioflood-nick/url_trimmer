from main import url_cleaner

def test_strips_bracket():
    assert url_cleaner("[a]") == "a"

def test_strips_parenth():
    assert url_cleaner("(a)") == "a"
    
def test_strip_whitespace():
    assert url_cleaner("a b") == "ab"

def test_http_replace():
    assert url_cleaner("hxxps") == "https"