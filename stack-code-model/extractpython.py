import os
import glob
import ast
import json
import re

# 입력 및 출력 디렉토리 설정
input_dir = "/workspace/FTEngineer/Engineer_FT-3/stack-code-model/data/raw/python"
output_dir = "/workspace/FTEngineer/Engineer_FT-3/stack-code-model/data/processed/python_code"
os.makedirs(output_dir, exist_ok=True)

# JSONL 파일 찾기
jsonl_files = glob.glob(os.path.join(input_dir, "*.jsonl"))
print(f"발견된 JSONL 파일: {len(jsonl_files)}개")

# 디버깅을 위한 카운터
total_lines = 0
parsed_lines = 0
python_entries = 0
extracted_files = 0
failed_parse = 0

# Python 코드 패턴 (간단한 휴리스틱)
python_patterns = [
    r'import\s+[a-zA-Z0-9_]+', 
    r'from\s+[a-zA-Z0-9_\.]+\s+import',
    r'def\s+[a-zA-Z0-9_]+\s*\(',
    r'class\s+[a-zA-Z0-9_]+',
    r'if\s+__name__\s*==\s*[\'"]__main__[\'"]'
]
compiled_patterns = [re.compile(pattern) for pattern in python_patterns]

# 가능한 코드 필드 목록
code_fields = ['content', 'code', 'source', 'raw', 'body', 'text']

# 첫 번째 파일 첫 라인 분석
if jsonl_files:
    try:
        with open(jsonl_files[0], 'r', encoding='utf-8', errors='ignore') as f:
            first_line = f.readline().strip()
            
            # 파싱 시도
            try:
                data = ast.literal_eval(first_line)
                print("첫 라인을 Python literal로 파싱 성공")
            except:
                try:
                    fixed_line = first_line.replace("'", '"')
                    data = json.loads(fixed_line)
                    print("첫 라인을 JSON으로 파싱 성공 (따옴표 변환 후)")
                except json.JSONDecodeError as e:
                    print(f"JSON 파싱 오류: {e}")
                    print(f"첫 500자: {first_line[:500]}")
                    exit(1)
            
            print("\n가능한 필드:")
            for key in data.keys():
                print(f"- {key}")
                
            # 코드 필드 탐지
            detected_field = None
            for field in code_fields:
                if field in data:
                    detected_field = field
                    if isinstance(data[field], str):
                        print(f"\n'{field}' 필드 내용 샘플: {data[field][:100]}...")
                    break
            
            if detected_field:
                print(f"\n코드 필드로 '{detected_field}'를 사용합니다.")
            else:
                print("코드 필드를 탐지할 수 없습니다.")
                exit(1)
    except Exception as e:
        print(f"첫 파일 분석 중 오류: {e}")
        exit(1)
else:
    print("JSONL 파일을 찾을 수 없습니다.")
    exit(1)

# 모든 파일 처리
for file_path in jsonl_files:
    file_extracted = 0
    print(f"\n처리 중: {os.path.basename(file_path)}")
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for i, line in enumerate(f):
                if not line.strip():
                    continue
                
                total_lines += 1
                
                try:
                    # 파싱 시도
                    try:
                        data = ast.literal_eval(line.strip())
                        parsed_lines += 1
                    except:
                        try:
                            fixed_line = line.replace("'", '"')
                            data = json.loads(fixed_line)
                            parsed_lines += 1
                        except:
                            failed_parse += 1
                            continue
                    
                    # 코드 필드가 있는지 확인
                    code = None
                    
                    # 'lang' 필드가 'python'인지 확인
                    is_python = False
                    if 'lang' in data and isinstance(data['lang'], str):
                        is_python = data['lang'].lower() == 'python'
                        if is_python:
                            python_entries += 1
                    
                    # 코드 필드에서 코드 추출
                    if detected_field in data and isinstance(data[detected_field], str):
                        code = data[detected_field].strip()
                        
                        # lang이 python이 아니더라도 Python 코드처럼 보이는지 확인
                        looks_like_python = False
                        if code:
                            for pattern in compiled_patterns:
                                if pattern.search(code):
                                    looks_like_python = True
                                    break
                            
                            # lang 필드가 python으로 명시되어 있거나 Python 코드처럼 보인다면 저장
                            if is_python or looks_like_python:
                                if len(code) > 10:  # 너무 짧은 코드는 제외
                                    filename = f"{os.path.basename(file_path).split('.')[0]}_{i}.py"
                                    output_path = os.path.join(output_dir, filename)
                                    
                                    with open(output_path, 'w', encoding='utf-8') as out_f:
                                        out_f.write(code)
                                    
                                    extracted_files += 1
                                    file_extracted += 1
                
                except Exception as e:
                    print(f"  라인 {i} 처리 중 오류: {e}")
                    continue
                    
        print(f"  {file_extracted}개 Python 파일 추출됨")
    except Exception as e:
        print(f"파일 {file_path} 처리 중 오류: {e}")

print("\n=== 처리 요약 ===")
print(f"총 라인 수: {total_lines}")
print(f"파싱 성공: {parsed_lines}")
print(f"파싱 실패: {failed_parse}")
print(f"Python 항목 (lang=python): {python_entries}")
print(f"추출된 Python 파일: {extracted_files}")
print(f"출력 디렉토리: {output_dir}")

# 추출된 파일이 적으면 샘플 추가
if extracted_files < 5:
    print("\n추출된 파일 수가 적어 샘플 Python 파일을 추가합니다...")
    samples = [
        """def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
""",
        """class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
        
person = Person("Alice", 30)
print(person.greet())
""",
        """import re

def extract_email(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    match = re.search(pattern, text)
    if match:
        return match.group(0)
    return None
    
email = extract_email("Contact us at info@example.com")
print(email)
"""
    ]
    
    for i, sample in enumerate(samples):
        with open(os.path.join(output_dir, f"sample_{i+1}.py"), 'w', encoding='utf-8') as f:
            f.write(sample)
        extracted_files += 1
    
    print(f"샘플 {len(samples)}개 추가됨. 최종 파일 수: {extracted_files}")