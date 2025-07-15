#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
데이터셋 다운로드 스크립트
사용법: python download_data.py --config ../configs/download_config.yaml
"""

import os
import argparse
import yaml
import logging
from datasets import load_dataset
import requests
from pathlib import Path
import zipfile
import tarfile
import shutil

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def setup_argparse():
    parser = argparse.ArgumentParser(description="Download datasets for ENGINEER_FT project")
    parser.add_argument("--config", type=str, required=True, help="Path to download configuration file")
    return parser.parse_args()

def download_huggingface_dataset(dataset_name, subset=None, split=None, output_dir=None):
    """HuggingFace 데이터셋 다운로드"""
    logger.info(f"Downloading {dataset_name} dataset from HuggingFace...")
    try:
        dataset = load_dataset(dataset_name, subset, split=split)
        
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            dataset.save_to_disk(output_dir)
            
        logger.info(f"Successfully downloaded {dataset_name} to {output_dir}")
        return dataset
    except Exception as e:
        logger.error(f"Error downloading {dataset_name}: {e}")
        return None

def download_github_repo(repo_url, output_dir):
    """GitHub 리포지토리 다운로드"""
    logger.info(f"Cloning repository: {repo_url}")
    try:
        os.system(f"git clone {repo_url} {output_dir}")
        logger.info(f"Successfully cloned {repo_url} to {output_dir}")
        return True
    except Exception as e:
        logger.error(f"Error cloning {repo_url}: {e}")
        return False

def main():
    args = setup_argparse()
    
    with open(args.config, 'r') as file:
        config = yaml.safe_load(file)
    
    base_dir = Path(config.get("base_output_dir", "../raw"))
    os.makedirs(base_dir, exist_ok=True)
    
    # HuggingFace 데이터셋 다운로드
    for dataset_info in config.get("huggingface_datasets", []):
        name = dataset_info["name"]
        subset = dataset_info.get("subset")
        split = dataset_info.get("split")
        category = dataset_info.get("category", "")
        
        output_dir = base_dir / category / name.replace("/", "_")
        download_huggingface_dataset(name, subset, split, output_dir)
    
    # GitHub 리포지토리 다운로드
    for repo_info in config.get("github_repos", []):
        url = repo_info["url"]
        name = url.split("/")[-1].replace(".git", "")
        category = repo_info.get("category", "")
        
        output_dir = base_dir / category / f"github_{name}"
        download_github_repo(url, output_dir)
    
    logger.info("All downloads completed!")

if __name__ == "__main__":
    main()