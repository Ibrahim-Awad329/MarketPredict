# backend/test_example.py

def test_project_runs():
    """اختبار بسيط ان كل حاجة تمام"""
    assert True == True

def test_math():
    """اختبار رياضيات"""
    result = 2 + 2
    assert result == 4

def test_string():
    """اختبار نص"""
    name = "MarketPredict"
    assert "Market" in name
