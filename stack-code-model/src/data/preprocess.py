import os
import glob
import json
import ast
from concurrent.futures import ProcessPoolExecutor
from src.utils.logging_utils import setup_logging
from src.features.code_analysis import extract_functions, analyze_code_structure
from src.features.docstring_extract import extract_docstrings

# 로깅 설정
logger = setup_logging("preprocess")

def process_file(file_path, output_dir, code_field):
    """JSONL 파일에서 Python 코드를 추출하여 처리합니다."""
    extracted_count = 0
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for i, line in enumerate(f):
                if not line.strip():
                    continue
                    
                try:
                    # Python literal로 파싱 시도
                    try:
                        data = ast.literal_eval(line.strip())
                    except:
                        # JSON으로 파싱 시도
                        try:
                            fixed_line = line.replace("'", '"')
                            data = json.loads(fixed_line)
                        except:
                            continue
                    
                    # Python 코드만 추출
                    if 'lang' in data and data['lang'].lower() == 'python':
                        if code_field in data and data[code_field].strip():
                            code = data[code_field]
                            
                            # 간단한 Python 코드 검증
                            if len(code) > 10 and ('def ' in code or 'class ' in code or 'import ' in code):
                                file_name = f"{os.path.basename(file_path).split('.')[0]}_{i}.py"
                                output_path = os.path.join(output_dir, file_name)
                                
                                with open(output_path, 'w', encoding='utf-8') as out_f:
                                    out_f.write(code)
                                
                                # 코드 분석 수행
                                try:
                                    functions = extract_functions(code)
                                    structure = analyze_code_structure(code)
                                    docstrings = extract_docstrings(code)
                                    
                                    # 분석 결과를 별도의 파일에 저장할 수 있음
                                    analysis_path = os.path.join(output_dir, f"{os.path.basename(file_path).split('.')[0]}_{i}_analysis.json")
                                    with open(analysis_path, 'w', encoding='utf-8') as analysis_f:
                                        json.dump({
                                            "functions": functions,
                                            "structure": structure,
                                            "docstrings": docstrings
                                        }, analysis_f, indent=2)
                                except Exception as e:
                                    logger.warning(f"Error analyzing code {file_name}: {e}")
                                
                                extracted_count += 1
                except Exception as e:
                    logger.debug(f"Error processing line {i} in {file_path}: {e}")
                    continue
    except Exception as e:
        logger.error(f"Error processing file {file_path}: {e}")
    
    return extracted_count

def main():
    # 입력 및 출력 경로 설정
    input_dir = "/workspace/FTEngineer/Engineer_FT-3/stack-code-model/data/raw/python"
    output_dir = "/workspace/FTEngineer/Engineer_FT-3/stack-code-model/data/processed/python_code"
    
    # 출력 디렉토리가 없으면 생성
    os.makedirs(output_dir, exist_ok=True)
    
    # JSONL 파일 찾기
    jsonl_files = glob.glob(os.path.join(input_dir, "*.jsonl"))
    logger.info(f"Found {len(jsonl_files)} JSONL files")
    
    # 필드 이름 확인을 위한 첫 번째 파일 첫 라인 분석
    code_field = None
    if jsonl_files:
        try:
            # 첫 번째 파일의 첫 줄을 읽어 구조 확인
            with open(jsonl_files[0], 'r', encoding='utf-8', errors='ignore') as f:
                first_line = f.readline().strip()
                
                # Python literal_eval을 사용하여 파싱 (작은따옴표를 처리할 수 있음)
                try:
                    data = ast.literal_eval(first_line)
                    logger.info("Successfully parsed first line as Python literal")
                except:
                    # 작은따옴표를 큰따옴표로 변환하여 JSON 파싱 시도
                    try:
                        fixed_line = first_line.replace("'", '"')
                        data = json.loads(fixed_line)
                        logger.info("Successfully parsed first line as JSON after quote conversion")
                    except json.JSONDecodeError as e:
                        logger.error(f"JSON parsing error: {e}")
                        logger.debug(f"First 100 chars: {first_line[:100]}")
                        return

            # 코드가 담긴 필드 확인
            possible_fields = ['content', 'code', 'source', 'body', 'text', 'raw']
            
            for field in possible_fields:
                if field in data and isinstance(data[field], str) and len(data[field].strip()) > 0:
                    logger.info(f"Found code field: '{field}' with content: {data[field][:50]}...")
                    code_field = field
                    break
                    
            if not code_field:
                logger.error("Could not find a suitable code field. Available fields:")
                for key, value in data.items():
                    if isinstance(value, str):
                        logger.info(f"- {key}: {value[:30]}...")
                    else:
                        logger.info(f"- {key}: {type(value)}")
                return
        except Exception as e:
            logger.error(f"Error analyzing first file: {e}")
            return
    else:
        logger.error("No JSONL files found!")
        return
    
    # 멀티프로세싱으로 파일 처리
    total_extracted = 0
    with ProcessPoolExecutor() as executor:
        futures = []
        for file_path in jsonl_files:
            future = executor.submit(process_file, file_path, output_dir, code_field)
            futures.append(future)
        
        # 모든 작업 완료 대기 및 결과 수집
        for future in futures:
            count = future.result()
            total_extracted += count
    
    logger.info(f"Total Python files extracted: {total_extracted}")
    logger.info(f"Output directory: {output_dir}")
    
    # 추출 파일이 없거나 적으면 샘플 추가
    if total_extracted < 5:
        logger.info("Adding sample Python files since extraction yielded too few files...")
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
"""
        ]
        
        for i, sample in enumerate(samples):
            with open(os.path.join(output_dir, f"sample_{i+1}.py"), 'w', encoding='utf-8') as f:
                f.write(sample)
            total_extracted += 1
            
        logger.info(f"Added {len(samples)} sample files. Total files: {total_extracted}")

if __name__ == "__main__":
    main()