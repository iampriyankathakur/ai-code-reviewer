from src.analyzer import analyze_code

def test_analyze_code():
    report = analyze_code("data/sample_code.py")
    assert isinstance(report, list)
    assert any("Function" in r for r in report)
