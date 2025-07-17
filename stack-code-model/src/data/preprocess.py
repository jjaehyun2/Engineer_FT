#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The Stack 데이터셋 전처리 스크립트
"""

import os
import json
import argparse
import logging
from concurrent.futures import ProcessPoolExecutor
from src.utils.logging_utils import setup_logging
from src.features.code_analysis import extract_functions, analyze_code_structure
from src.features.docstring_extract import extract_docstrings

logger = logging.getLogger(__name__)

def preprocess_file(file_content, language):
    """단일 코드 파일 전처리"""
    processed_data = {
        "language": language,
        "original_size": len(file_content),
        "functions": [],
        "classes": [],
        "imports": [],
        "docstrings": {}
    }
    
    # 언어별 처리 로직
    if language == "python":
        processed_data["functions"] = extract_functions(file_content, language)
        processed_data["docstrings"] = extract_docstrings(file_content, language)
    elif language == "javascript":
        # JavaScript 처리 로직
        pass
    elif language == "java":
        # Java 처리 로직
        pass
    
    # 코드 구조 분석
    structure = analyze_code_structure(file_content, language)
    processed_data.update(structure)
    
    return processed_data

def process_language_data(input_dir, output_dir, language, max_files=None):
    """특정 언어 데이터 전처리
    
    Args:
        input_dir: 입력 디렉토리 경로
        output_dir: 출력 디렉토리 경로
        language: 처리할 언어
        max_files: 처리할 최대 파일 수 (None이면 모두 처리)
    """
    logger = logging.getLogger(__name__)
    logger.info(f"Processing {language} data")
    
    input_path = os.path.join(input_dir, language)
    output_path = os.path.join(output_dir, f"{language}_clean")
    os.makedirs(output_path, exist_ok=True)
    
    # 입력 디렉토리의 모든 파일 리스트 획득
    all_files = []
    for root, _, files in os.walk(input_path):
        for filename in files:
            all_files.append(os.path.join(root, filename))
    
    # 필요하면 파일 수 제한
    if max_files and len(all_files) > max_files:
        all_files = all_files[:max_files]
    
    logger.info(f"Found {len(all_files)} files to process in {language} dataset")
    
    # 진행 상황 추적
    file_count = len(all_files)
    processed_count = 0
    error_count = 0
    example_count = 0
    
    for input_file in all_files:
        logger.info(f"Processing file {processed_count+1}/{file_count}: {input_file}")
        
        try:
            # 파일 읽기
            with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
            
            file_examples = 0
            
            # 각 줄 처리
            for i, line in enumerate(lines):
                try:
                    line = line.strip()
                    if not line:
                        continue
                    
                    # JSON 파싱 시도
                    example = json.loads(line)
                    
                    # 필요한 필드 확인 및 추출
                    if 'content' in example:
                        code_content = example['content']
                        
                        # 코드가 비어있지 않은지 확인
                        if code_content.strip():
                            # 파일 이름 생성
                            base_filename = os.path.basename(input_file)
                            output_file = os.path.join(
                                output_path, 
                                f"{os.path.splitext(base_filename)[0]}_{i}.py"
                            )
                            
                            # 처리된 파일 저장
                            with open(output_file, 'w', encoding='utf-8') as out_f:
                                out_f.write(code_content)
                            
                            file_examples += 1
                            example_count += 1
                    
                except json.JSONDecodeError as e:
                    logger.debug(f"Error parsing JSON in file {input_file}, line {i+1}: {e}")
                    error_count += 1
                except Exception as e:
                    logger.debug(f"Error processing line {i+1} in file {input_file}: {e}")
                    error_count += 1
            
            logger.info(f"Extracted {file_examples} examples from file")
            processed_count += 1
            
            # 진행 상황 보고
            if processed_count % 10 == 0:
                logger.info(f"Progress: {processed_count}/{file_count} files, {example_count} total examples")
                
        except Exception as e:
            logger.warning(f"Error processing file {input_file}: {e}")
            error_count += 1
    
    logger.info(f"Completed processing {language}: {processed_count} files, {example_count} examples, {error_count} errors")
    return example_count

def main():
    parser = argparse.ArgumentParser(description="Preprocess The Stack dataset")
    parser.add_argument("--input-dir", default="data/raw",
                        help="Directory containing raw data")
    parser.add_argument("--output-dir", default="data/processed",
                        help="Directory to store processed data")
    parser.add_argument("--languages", nargs="+", default=["python"],
                        help="Languages to process (e.g., python javascript java)")
    parser.add_argument("--files-per-language", type=int, default=None,
                        help="Maximum number of files per language")
    
    args = parser.parse_args()
    setup_logging()
    
    for language in args.languages:
        process_language_data(
            args.input_dir, 
            args.output_dir, 
            language, 
            max_files=args.files_per_language
        )

if __name__ == "__main__":
    main()