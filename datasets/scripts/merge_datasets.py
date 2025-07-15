#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
데이터셋 병합 스크립트
사용법: python merge_datasets.py --config ../configs/dataset_splits.yaml
"""

import os
import argparse
import yaml
import logging
import json
import random
from pathlib import Path
from datasets import load_from_disk, concatenate_datasets, Dataset

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def setup_argparse():
    parser = argparse.ArgumentParser(description="Merge and split datasets for ENGINEER_FT project")
    parser.add_argument("--config", type=str, required=True, help="Path to dataset splits configuration")
    return parser.parse_args()

def load_and_sample_dataset(dataset_path, max_samples=None, language=None, random_seed=42):
    """데이터셋을 로드하고 필요시 샘플링"""
    logger.info(f"Loading dataset from {dataset_path}")
    
    try:
        dataset = load_from_disk(dataset_path)
        
        # 언어 필터링 (필요시)
        if language:
            dataset = dataset.filter(lambda x: x.get("language") == language)
            logger.info(f"Filtered to {len(dataset)} examples for language {language}")
        
        # 샘플링 (필요시)
        if max_samples and max_samples < len(dataset):
            # 샘플링 시 랜덤 시드 설정
            rng = random.Random(random_seed)
            indices = rng.sample(range(len(dataset)), max_samples)
            dataset = dataset.select(indices)
            logger.info(f"Sampled {max_samples} examples")
        
        return dataset
    
    except Exception as e:
        logger.error(f"Error loading dataset from {dataset_path}: {e}")
        return None

def merge_datasets(dataset_configs, processed_dir):
    """설정에 따라 데이터셋 병합"""
    all_datasets = []
    
    for config in dataset_configs:
        path = processed_dir / config["path"]
        max_samples = config.get("max_samples")
        language = config.get("language")
        
        dataset = load_and_sample_dataset(path, max_samples, language)
        if dataset:
            all_datasets.append(dataset)
    
    if not all_datasets:
        logger.error("No valid datasets found for merging")
        return None
    
    # 모든 데이터셋 병합
    merged_dataset = concatenate_datasets(all_datasets)
    logger.info(f"Merged dataset has {len(merged_dataset)} examples")
    
    return merged_dataset

def split_dataset(dataset, train_ratio=0.8, val_ratio=0.1, test_ratio=0.1, random_seed=42):
    """데이터셋을 훈련/검증/테스트로 분할"""
    # 비율 검증
    assert abs(train_ratio + val_ratio + test_ratio - 1.0) < 1e-10, "Split ratios must sum to 1"
    
    # 셔플
    dataset = dataset.shuffle(seed=random_seed)
    
    # 분할 인덱스 계산
    n_samples = len(dataset)
    n_train = int(n_samples * train_ratio)
    n_val = int(n_samples * val_ratio)
    
    train_dataset = dataset.select(range(n_train))
    val_dataset = dataset.select(range(n_train, n_train + n_val))
    test_dataset = dataset.select(range(n_train + n_val, n_samples))
    
    logger.info(f"Split dataset into: {len(train_dataset)} train, {len(val_dataset)} validation, {len(test_dataset)} test examples")
    
    return {
        "train": train_dataset,
        "validation": val_dataset,
        "test": test_dataset
    }

def save_to_jsonl(dataset, output_path):
    """데이터셋을 JSONL 형식으로 저장"""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        for example in dataset:
            json_str = json.dumps(example, ensure_ascii=False)
            f.write(json_str + '\n')
    
    logger.info(f"Saved {len(dataset)} examples to {output_path}")

def main():
    args = setup_argparse()
    
    with open(args.config, 'r') as file:
        config = yaml.safe_load(file)
    
    processed_dir = Path(config.get("processed_dir", "../processed"))
    final_dir = Path(config.get("final_dir", "../final"))
    
    # 데이터셋 설정 가져오기
    dataset_configs = config.get("datasets", [])
    if not dataset_configs:
        logger.error("No dataset configurations found")
        return
    
    # 데이터셋 병합
    merged_dataset = merge_datasets(dataset_configs, processed_dir)
    if not merged_dataset:
        return
    
    # 데이터셋 분할
    split_ratios = config.get("split_ratios", {})
    train_ratio = split_ratios.get("train", 0.8)
    val_ratio = split_ratios.get("validation", 0.1)
    test_ratio = split_ratios.get("test", 0.1)
    
    splits = split_dataset(
        merged_dataset,
        train_ratio=train_ratio,
        val_ratio=val_ratio,
        test_ratio=test_ratio,
        random_seed=config.get("random_seed", 42)
    )
    
    # JSONL 형식으로 저장
    save_to_jsonl(splits["train"], final_dir / "train.jsonl")
    save_to_jsonl(splits["validation"], final_dir / "validation.jsonl")
    save_to_jsonl(splits["test"], final_dir / "test.jsonl")
    
    logger.info("Dataset merging and splitting completed!")

if __name__ == "__main__":
    main()