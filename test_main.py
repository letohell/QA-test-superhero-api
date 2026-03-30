from main import get_highest_hero

def test_returns_string():
    result = get_highest_hero("Male", True)
    assert isinstance(result, str) or result is None

def test_male_with_job():
    result = get_highest_hero("Male", True)
    assert result is not None

def test_female_with_job():
    result = get_highest_hero("Female", True)
    assert result is not None

def test_female_without_job():
    result = get_highest_hero("Female", False)
    assert result is not None

def test_male_without_job():
    result = get_highest_hero("Male", False)
    assert result is not None