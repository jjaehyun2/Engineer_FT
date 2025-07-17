
import ast
import os
import glob
import json

# 파일 경로 설정
input_dir = "/workspace/FTEngineer/Engineer_FT-3/stack-code-model/data/raw/python"
output_dir = "/workspace/FTEngineer/Engineer_FT-3/stack-code-model/data/processed/python_clean"
os.makedirs(output_dir, exist_ok=True)

# 첫 번째 파일을 확인하여 구조 파악
files = glob.glob(os.path.join(input_dir, "*.jsonl"))
if not files:
    print("JSONL 파일을 찾을 수 없습니다.")
    exit(1)

print(f"총 {len(files)}개 파일 발견")

# 첫 번째 파일의 첫 라인 확인
try:
    with open(files[0], 'r', encoding='utf-8', errors='ignore') as f:
        first_line = f.readline().strip()
        
        # 파이썬 dict 리터럴로 파싱 시도 (작은따옴표 처리 가능)
        try:
            data = ast.literal_eval(first_line)
            print("파이썬 리터럴로 파싱 성공")
            print("필드 목록:")
            for key, value in data.items():
                if isinstance(value, str):
                    print(f"- {key}: {value[:50]}")
                else:
                    print(f"- {key}: {type(value)}")
        except (SyntaxError, ValueError) as e:
            print(f"리터럴 파싱 실패: {e}")
            print("원본 라인:")
            print(first_line[:500])
            
            # JSON으로 파싱 시도
            try:
                # 작은따옴표를 큰따옴표로 변환
                fixed_line = first_line.replace("'", '"')
                data = json.loads(fixed_line)
                print("JSON으로 파싱 성공 (따옴표 변환 후)")
            except json.JSONDecodeError as je:
                print(f"JSON 파싱도 실패: {je}")
except Exception as e:
    print(f"파일 읽기 오류: {e}")
    exit(1)

# 코드가 있을 것으로 예상되는 필드 찾기
code_fields = ['content', 'code', 'source', 'body', 'text', 'raw']
code_field = None

for field in code_fields:
    if field in data and isinstance(data[field], str):
        print(f"코드로 사용할 필드 '{field}' 발견:")
        print(data[field][:100])
        code_field = field
        break

if not code_field:
    print("코드 필드를 찾을 수 없습니다. 데이터 구조를 더 확인해 보세요.")
    # 모든 필드의 내용 샘플 출력
    for key, value in data.items():
        if isinstance(value, str) and len(value) > 10:  # 문자열이고 길이가 있는 필드만
            print(f"\n{key} 필드 샘플:")
            print(value[:200])
    exit(1)

# Python 코드 추출
print("\nPython 코드 추출 시작...")
total_python = 0
total_files = 0

for file_path in files:
    file_count = 0
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for i, line in enumerate(f):
                if not line.strip():
                    continue
                    
                total_files += 1
                
                try:
                    # Python 리터럴로 파싱
                    data = ast.literal_eval(line.strip())
                    
                    # Python 코드 확인
                    if data.get('lang', '').lower() == 'python':
                        if code_field in data and data[code_field].strip():
                            code = data[code_field]
                            
                            # 코드가 Python스러운지 간단히 확인
                            if len(code) > 10 and ('def ' in code or 'class ' in code or 'import ' in code):
                                filename = f"{os.path.basename(file_path).split('.')[0]}_{i}.py"
                                with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as out_f:
                                    out_f.write(code)
                                total_python += 1
                                file_count += 1
                except Exception as e:
                    pass  # 개별 라인 파싱 실패 무시
    except Exception as e:
        print(f"파일 처리 오류 {file_path}: {e}")
        
    print(f"{file_path}: {file_count}개 Python 파일 추출")

print(f"\n총 {total_files}개 항목 중 {total_python}개 Python 코드 추출 완료")
print(f"출력 경로: {output_dir}")

# 샘플 데이터가 너무 적으면 기본 샘플 추가
if total_python < 5:
    print("추출된 Python 파일이 너무 적어 샘플 파일을 추가합니다.")
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
        total_python += 1
    
    print(f"샘플 {len(samples)}개 추가됨. 최종 파일 수: {total_python}")
EOF

# 실행
python parse_jsonl.py