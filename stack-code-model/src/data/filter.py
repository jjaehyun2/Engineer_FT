#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
전처리된 데이터에서 고품질 코드 필터링
"""

import os
import json
import argparse
import logging
from src.utils.logging_utils import setup_logging
from src.features.quality_metrics import calculate_code_quality

logger = logging.getLogger(__name__)

def is_quality_code(example, language, min_quality_score=0.6):
    """코드 품질 평가"""
    # 기본 품질 지표
    has_docstrings = len(example.get("docstrings", {})) > 0
    has_functions = len(example.get("functions", [])) > 0
    stars = example.get("stars", 0)
    
    # 함수가 없는 경우는 저품질로 판단
    if not has_functions:
        return False
    
    # 품질 점수 계산
    quality_score = calculate_code_quality(example, language)
    
    # 품질 기준 적용
    if language == "python":
        # Python은 문서화 중요시
        return (quality_score >= min_quality_score and 
                (has_docstrings or stars >= 5))
    elif language == "javascript":
        # JavaScript는 별도 기준
        return (quality_score >= min_quality_score - 0.1 and 
                (has_functions or stars >= 3))
    else:
        # 기본 기준
        return quality_score >= min_quality_score

def filter_by_domain(examples, target_domains=None, balance=True):
    """도메인별 필터링 및 균형 조정"""
    if not target_domains:
        target_domains = ["algorithms", "web", "data", "system", "general"]
        
    domain_counts = {domain: 0 for domain in target_domains}
    domain_limits = {domain: 100000 for domain in target_domains}  # 도메인별 한도
    
    filtered_examples = []
    
    for example in examples:
        domain = example.get("domain", "general")
        if domain not in domain_counts:
            domain = "general"
            
        # 균형 조정 활성화된 경우
        if balance:
            if domain_counts[domain] < domain_limits[domain]:
                filtered_examples.append(example)
                domain_counts[domain] += 1
        else:
            filtered_examples.append(example)
    
    return filtered_examples

def filter_dataset(input_dir, output_dir, language, quality_threshold=0.6, max_files=None):
    """데이터셋 필터링 실행"""
    logger.info(f"Filtering {language} dataset with quality threshold {quality_threshold}")
    
    input_path = f"{input_dir}/{language}_clean"
    output_path = f"{output_dir}/by_language/{language}"
    
    os.makedirs(output_path, exist_ok=True)
    
    files_processed = 0
    files_selected = 0
    
    for chunk_file in sorted(os.listdir(input_path)):
        if not chunk_file.endswith('.jsonl'):
            continue
            
        quality_examples = []
        
        with open(f"{input_path}/{chunk_file}", 'r') as f:
            for line in f:
                try:
                    example = json.loads(line.strip())
                    files_processed += 1
                    
                    if is_quality_code(example, language, quality_threshold):
                        quality_examples.append(example)
                        files_selected += 1
                        
                    if files_processed % 1000 == 0:
                        logger.info(f"Processed {files_processed} files, selected {files_selected}")
                        
                    if max_files and files_selected >= max_files:
                        break
                        
                except Exception as e:
                    logger.warning(f"Error processing line: {e}")
                    
        # 도메인 균형 맞추기
        balanced_examples = filter_by_domain(quality_examples)
        
        # 결과 저장
        output_file = f"{output_path}/{chunk_file}"
        with open(output_file, 'w') as f_out:
            for example in balanced_examples:
                f_out.write(json.dumps(example) + "\n")
                
        if max_files and files_selected >= max_files:
            break
            
    logger.info(f"Filtering completed for {language}. "
                f"Processed {files_processed}, selected {files_selected} files.")
    return files_selected

def combine_filtered_datasets(input_dir, output_dir, languages):
    """필터링된 데이터셋 결합"""
    os.makedirs(f"{output_dir}/final_dataset", exist_ok=True)
    
    total_files = 0
    for idx, language in enumerate(languages):
        input_path = f"{input_dir}/by_language/{language}"
        if not os.path.exists(input_path):
            logger.warning(f"Input path {input_path} does not exist, skipping")
            continue
            
        language_files = 0
        for chunk_file in sorted(os.listdir(input_path)):
            if not chunk_file.endswith('.jsonl'):
                continue
                
            # 결합된 파일 생성
            output_file = f"{output_dir}/final_dataset/combined_{idx}_{language}_{chunk_file}"
            os.system(f"cp {input_path}/{chunk_file} {output_file}")
            
            # 파일 수 계산
            with open(f"{input_path}/{chunk_file}", 'r') as f:
                file_count = sum(1 for _ in f)
                language_files += file_count
                
        total_files += language_files
        logger.info(f"Added {language_files} {language} files to combined dataset")
        
    logger.info(f"Combined dataset created with {total_files} total files")
    return total_files

def main():
    parser = argparse.ArgumentParser(description="Filter processed Stack dataset")
    parser.add_argument("--input-dir", default="data/processed",
        help="Directory containing processed data")
    parser.add_argument("--output-dir", default="data/filtered",
        help="Directory to store filtered data")
    parser.add_argument("--languages", nargs="+", default=["python"],
        help="Languages to filter")
    parser.add_argument("--quality-threshold", type=float, default=0.6,
        help="Minimum quality score threshold")
    parser.add_argument("--max-files", type=int, default=None,
        help="Maximum files per language to select")
    parser.add_argument("--combine", action="store_true",
        help="Combine filtered datasets")
    
    args = parser.parse_args()
    setup_logging()
    
    for language in args.languages:
        filter_dataset(
            args.input_dir,
            args.output_dir,
            language,
            quality_threshold=args.quality_threshold,
            max_files=args.max_files
        )
        
    if args.combine:
        combine_filtered_datasets(args.output_dir, args.output_dir, args.languages)

if __name__ == "__main__":
    main()