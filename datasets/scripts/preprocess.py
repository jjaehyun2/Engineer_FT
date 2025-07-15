#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
데이터셋 전처리 스크립트
사용법: python preprocess.py --config ../configs/preprocessing_config.yaml
"""

import os
import re
import argparse
import yaml
import logging
import json
from pathlib import Path
from datasets import load_from_disk, Dataset
from concurrent.futures import ProcessPoolExecutor

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def setup_argparse():
    parser = argparse.ArgumentParser(description="Preprocess datasets for ENGINEER_FT project")
    parser.add_argument("--config", type=str, required=True, help="Path to preprocessing configuration file")
    return parser.parse_args()

def clean_code(code, config):
    """코드 정제 함수"""
    # 불필요한 주석 제거
    if config.get("remove_comments", True):
        code = re.sub(r'#.*?\n', '\n', code)
    
    # 연속된 빈 줄 제거
    if config.get("normalize_whitespace", True):
        code = re.sub(r'\n\s*\n', '\n\n', code)
    
    # 특수 문자 처리
    if config.get("handle_special_chars", True):
        code = code.replace('\t', '    ')  # 탭을 스페이스로 변환
    
    return code.strip()

def clean_explanation(text, config):
    """설명 정제 함수"""
    # HTML 태그 제거
    if config.get("remove_html", True):
        text = re.sub(r'<.*?>', '', text)
    
    # 특수 문자 정리
    if config.get("clean_special_chars", True):
        text = re.sub(r'[^\w\s.,;:()\[\]{}\'\"+-/*=<>!?]', ' ', text)
    
    # 연속된 공백 제거
    if config.get("normalize_whitespace", True):
        text = re.sub(r'\s+', ' ', text)
    
    return text.strip()

def process_codesearchnet(dataset_path, output_path, config):
    """CodeSearchNet 데이터셋 처리"""
    logger.info(f"Processing CodeSearchNet dataset from {dataset_path}")
    
    dataset = load_from_disk(dataset_path)
    
    def convert_format(example):
        code = clean_code(example["code"], config)
        docstring = clean_explanation(example["docstring"], config)
        
        # 너무 짧은 코드나 설명은 필터링
        if len(code) < config.get("min_code_length", 50) or len(docstring) < config.get("min_explanation_length", 100):
            return None
        
        return {
            "instruction": "Explain the following code in detail",
            "input": code,
            "output": docstring,
            "category": "code_explanation",
            "language": example.get("language", "unknown"),
            "source": "codesearchnet"
        }
    
    # 데이터 변환 및 필터링
    processed_data = []
    for example in dataset:
        converted = convert_format(example)
        if converted:
            processed_data.append(converted)
    
    # 결과 저장
    output_dataset = Dataset.from_list(processed_data)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    output_dataset.save_to_disk(output_path)
    logger.info(f"Saved processed dataset to {output_path} with {len(processed_data)} examples")

def process_humaneval(dataset_path, output_path, config):
    """HumanEval 데이터셋 처리"""
    logger.info(f"Processing HumanEval dataset from {dataset_path}")
    
    dataset = load_from_disk(dataset_path)
    
    def convert_format(example):
        # HumanEval 형식에 맞게 변환
        prompt = clean_explanation(example["prompt"], config)
        canonical_solution = clean_code(example["canonical_solution"], config)
        
        # 너무 짧은 문제나 해결책은 필터링
        if len(prompt) < config.get("min_prompt_length", 50) or len(canonical_solution) < config.get("min_solution_length", 50):
            return None
        
        return {
            "instruction": prompt,
            "input": "",
            "output": canonical_solution,
            "category": "code_generation",
            "language": "python",
            "source": "humaneval"
        }
    
    # 데이터 변환 및 필터링
    processed_data = []
    for example in dataset:
        converted = convert_format(example)
        if converted:
            processed_data.append(converted)
    
    # 결과 저장
    output_dataset = Dataset.from_list(processed_data)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    output_dataset.save_to_disk(output_path)
    logger.info(f"Saved processed dataset to {output_path} with {len(processed_data)} examples")

def main():
    args = setup_argparse()
    
    with open(args.config, 'r') as file:
        config = yaml.safe_load(file)
    
    raw_dir = Path(config.get("raw_dir", "../raw"))
    processed_dir = Path(config.get("processed_dir", "../processed"))
    
    # CodeSearchNet 처리
    if config.get("process_codesearchnet", True):
        dataset_path = raw_dir / "code_explanation" / "codesearchnet"
        output_path = processed_dir / "code_explanation" / "en" / "codesearchnet"
        process_codesearchnet(dataset_path, output_path, config)
    
    # HumanEval 처리
    if config.get("process_humaneval", True):
        dataset_path = raw_dir / "code_generation" / "humaneval"
        output_path = processed_dir / "code_generation" / "en" / "humaneval"
        process_humaneval(dataset_path, output_path, config)
    
    logger.info("Preprocessing completed!")

if __name__ == "__main__":
    main()