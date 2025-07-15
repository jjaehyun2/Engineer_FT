#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
데이터 품질 검사 스크립트
사용법: python quality_check.py --input ../processed/code_explanation/en/codesearchnet
"""

import os
import argparse
import logging
import json
import random
import numpy as np
from pathlib import Path
from datasets import load_from_disk
from concurrent.futures import ProcessPoolExecutor

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def setup_argparse():
    parser = argparse.ArgumentParser(description="Quality check for processed datasets")
    parser.add_argument("--input", type=str, required=True, help="Path to processed dataset")
    parser.add_argument("--output", type=str, help="Path to save quality report", default=None)
    parser.add_argument("--sample", type=int, default=100, help="Number of samples to check")
    return parser.parse_args()

def check_python_syntax(code):
    """Python 코드 구문 검사"""
    try:
        compile(code, '<string>', 'exec')
        return True
    except SyntaxError:
        return False

def check_duplicate_content(dataset, threshold=0.9):
    """중복 내용 검사 (간단한 구현)"""
    # 실제 구현에서는 더 효율적인 방법 필요
    seen_contents = set()
    duplicates = 0
    
    for example in dataset:
        content = example["input"] + example["output"]
        if content in seen_contents:
            duplicates += 1
        seen_contents.add(content)
    
    return duplicates

def check_instruction_consistency(dataset):
    """지시문 일관성 검사"""
    instruction_counts = {}
    
    for example in dataset:
        instruction = example["instruction"]
        category = example["category"]
        key = (instruction, category)
        
        if key not in instruction_counts:
            instruction_counts[key] = 0
        instruction_counts[key] += 1
    
    # 지시문 일관성 분석
    inconsistencies = sum(1 for count in instruction_counts.values() if count < 10)
    
    return inconsistencies, instruction_counts

def generate_quality_report(dataset_path, sample_size=100):
    """데이터셋 품질 보고서 생성"""
    logger.info(f"Generating quality report for {dataset_path}")
    
    dataset = load_from_disk(dataset_path)
    
    # 통계 수집
    total_examples = len(dataset)
    categories = {}
    languages = {}
    sources = {}
    
    input_lengths = []
    output_lengths = []
    
    # 샘플링
    sample_indices = random.sample(range(total_examples), min(sample_size, total_examples))
    python_syntax_errors = 0
    
    for i in sample_indices:
        example = dataset[i]
        
        # 카테고리, 언어, 소스 통계
        category = example.get("category", "unknown")
        language = example.get("language", "unknown")
        source = example.get("source", "unknown")
        
        categories[category] = categories.get(category, 0) + 1
        languages[language] = languages.get(language, 0) + 1
        sources[source] = sources.get(source, 0) + 1
        
        # 길이 통계
        input_lengths.append(len(example["input"]))
        output_lengths.append(len(example["output"]))
        
        # Python 코드 구문 검사 (코드 생성 데이터만)
        if category == "code_generation" and language == "python":
            if not check_python_syntax(example["output"]):
                python_syntax_errors += 1
    
    # 중복 검사
    duplicates = check_duplicate_content(dataset)
    
    # 지시문 일관성 검사
    inconsistencies, instruction_counts = check_instruction_consistency(dataset)
    
    # 보고서 생성
    report = {
        "dataset_path": str(dataset_path),
        "total_examples": total_examples,
        "statistics": {
            "categories": categories,
            "languages": languages,
            "sources": sources,
            "input_length": {
                "mean": np.mean(input_lengths),
                "min": min(input_lengths),
                "max": max(input_lengths),
                "p25": np.percentile(input_lengths, 25),
                "p50": np.percentile(input_lengths, 50),
                "p75": np.percentile(input_lengths, 75),
            },
            "output_length": {
                "mean": np.mean(output_lengths),
                "min": min(output_lengths),
                "max": max(output_lengths),
                "p25": np.percentile(output_lengths, 25),
                "p50": np.percentile(output_lengths, 50),
                "p75": np.percentile(output_lengths, 75),
            }
        },
        "quality_issues": {
            "python_syntax_errors": python_syntax_errors,
            "python_syntax_error_rate": python_syntax_errors / len([i for i in sample_indices if dataset[i].get("category") == "code_generation" and dataset[i].get("language") == "python"]) if python_syntax_errors > 0 else 0,
            "duplicates": duplicates,
            "duplicate_rate": duplicates / total_examples,
            "instruction_inconsistencies": inconsistencies,
        }
    }
    
    return report

def main():
    args = setup_argparse()
    
    input_path = Path(args.input)
    
    # 품질 보고서 생성
    report = generate_quality_report(input_path, args.sample)
    
    # 결과 출력
    logger.info(f"Quality Report Summary for {input_path}:")
    logger.info(f"Total examples: {report['total_examples']}")
    logger.info(f"Categories: {report['statistics']['categories']}")
    logger.info(f"Languages: {report['statistics']['languages']}")
    logger.info(f"Mean input length: {report['statistics']['input_length']['mean']:.2f}")
    logger.info(f"Mean output length: {report['statistics']['output_length']['mean']:.2f}")
    logger.info(f"Python syntax error rate: {report['quality_issues']['python_syntax_error_rate']:.2%}")
    logger.info(f"Duplicate rate: {report['quality_issues']['duplicate_rate']:.2%}")
    
    # 파일로 저장
    if args.output:
        output_path = Path(args.output)
        os.makedirs(output_path.parent, exist_ok=True)
        
        with open(output_path, 'w') as f:
            json.dump(report, f, indent=2)
        logger.info(f"Saved quality report to {output_path}")

if __name__ == "__main__":
    main()