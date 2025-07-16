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
    """언어별 데이터셋 전처리"""
    logger.info(f"Processing {language} data")
    
    os.makedirs(f"{output_dir}/{language}_clean", exist_ok=True)
    
    files_processed = 0
    input_path = f"{input_dir}/{language}"
    
    # 파일 형식에 따라 다르게 처리
    if os.path.isdir(input_path) and not os.path.exists(f"{input_path}/dataset_info.json"):
        # 일반 파일 디렉토리인 경우
        for chunk_file in sorted(os.listdir(input_path)):
            if not chunk_file.endswith('.jsonl'):
                continue
                
            output_file = f"{output_dir}/{language}_clean/{chunk_file}"
            
            with open(f"{input_path}/{chunk_file}", 'r') as f_in, \
                open(output_file, 'w') as f_out:
                
                for line in f_in:
                    try:
                        example = json.loads(line.strip())
                        content = example.get("content", "")
                        
                        if not content or len(content) < 100:
                            continue
                            
                        processed = preprocess_file(content, language)
                        processed["repo"] = example.get("repo", "")
                        processed["path"] = example.get("path", "")
                        processed["stars"] = example.get("stars", 0)
                        
                        f_out.write(json.dumps(processed) + "\n")
                        
                        files_processed += 1
                        if files_processed % 1000 == 0:
                            logger.info(f"Processed {files_processed} {language} files")
                            
                        if max_files and files_processed >= max_files:
                            break
                            
                    except Exception as e:
                        logger.warning(f"Error processing file: {e}")
                        continue
                        
            if max_files and files_processed >= max_files:
                break
    else:
        # Hugging Face datasets 형식으로 저장된 경우
        from datasets import load_from_disk
        
        try:
            dataset = load_from_disk(input_path)
            logger.info(f"Loaded dataset with {len(dataset)} examples")
            
            with ProcessPoolExecutor() as executor:
                batch_size = 1000
                for i in range(0, len(dataset), batch_size):
                    if max_files and i >= max_files:
                        break
                        
                    end_idx = min(i + batch_size, len(dataset))
                    batch = dataset[i:end_idx]
                    
                    # 병렬 처리
                    futures = []
                    for example in batch:
                        future = executor.submit(
                            preprocess_file, 
                            example["content"], 
                            language
                        )
                        futures.append((future, example))
                    
                    # 결과 저장
                    output_file = f"{output_dir}/{language}_clean/chunk_{i//batch_size:04d}.jsonl"
                    with open(output_file, 'w') as f_out:
                        for future, example in futures:
                            try:
                                processed = future.result()
                                processed["repo"] = example.get("repo", "")
                                processed["path"] = example.get("path", "")
                                processed["stars"] = example.get("stars", 0)
                                
                                f_out.write(json.dumps(processed) + "\n")
                                
                                files_processed += 1
                            except Exception as e:
                                logger.warning(f"Error in parallel processing: {e}")
                    
                    logger.info(f"Processed batch {i//batch_size}, total: {files_processed}")
                    
        except Exception as e:
            logger.error(f"Error loading dataset from disk: {e}")
    
    logger.info(f"Completed processing {files_processed} {language} files")
    return files_processed

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