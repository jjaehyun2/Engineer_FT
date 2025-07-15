import sys
print(f"Python 실행 경로: {sys.executable}")

try:
    import yaml
    print(f"PyYAML 버전: {yaml.__version__}")
    print(f"PyYAML 경로: {yaml.__file__}")
    
    # 간단한 YAML 파싱 테스트
    test_yaml = """
    name: Test
    version: 1.0
    dependencies:
        - python
        - yaml
    """
    
    parsed = yaml.safe_load(test_yaml)
    print(f"YAML 파싱 결과: {parsed}")
    
except ImportError as e:
    print(f"가져오기 오류: {e}")
except Exception as e:
    print(f"다른 오류 발생: {e}")