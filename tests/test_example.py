def test_example():
    assert 1 == 1

def test_youtube(page):
    page.goto("https://youtube.com")
    assert "YouTube" in page.title()