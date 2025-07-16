#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The Stack 데이터셋 다운로드 스크립트
"""

import os
import argparse
import logging
from datasets import load_dataset
from src.utils.config import load_config
from src.utils.logging_utils import setup_logging

logger = logging.getLogger(__name__)

def download_language_dataset(language, max_files=None, output_dir="data/raw", 
                             use_streaming=True):
    """지정된 언어의 The Stack 데이터셋 다운로드"""
    os.makedirs(f"{output_dir}/{language}", exist_ok=True)
    logger.info(f"Downloading {language} dataset to {output_dir}/{language}")
    
    try:
        # 스트리밍 또는 전체 다운로드 모드
        if use_streaming:
            dataset = load_dataset("bigcode/the-stack", f"data/{language}", 
                                   split="train", streaming=True)
            
            # 파일별로 저장
            count = 0
            for idx, example in enumerate(dataset):
                if max_files and count >= max_files:
                    break
                
                # 최소 크기 필터링 (작은 파일 제외)
                if len(example["content"]) < 100:
                    continue
                
                # JSONL 형식으로 저장
                with open(f"{output_dir}/{language}/chunk_{count//1000:04d}.jsonl", "a") as f:
                    f.write(f"{example}\n")
                
                count += 1
                if count % 1000 == 0:
                    logger.info(f"Downloaded {count} {language} files")
        else:
            # 전체 다운로드 (메모리 많이 필요)
            dataset = load_dataset("bigcode/the-stack", f"data/{language}", split="train")
            if max_files:
                dataset = dataset.select(range(min(max_files, len(dataset))))
            
            # 디스크에 저장
            dataset.save_to_disk(f"{output_dir}/{language}")
            logger.info(f"Saved {len(dataset)} {language} files")
            
        logger.info(f"Download completed for {language}")
        return True
    
    except Exception as e:
        logger.error(f"Error downloading {language} dataset: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Download The Stack dataset by language")
    parser.add_argument("--languages", nargs="+", default=["python"],
                        help="Languages to download (e.g., python javascript java)")
    parser.add_argument("--files-per-language", type=int, default=500000,
                        help="Maximum number of files per language")
    parser.add_argument("--output-dir", default="data/raw",
                        help="Directory to store downloaded data")
    parser.add_argument("--config", default="config/download_config.json",
                        help="Path to configuration file")
    parser.add_argument("--streaming", action="store_true",
                        help="Use streaming mode for download")
    
    args = parser.parse_args()
    
    # 설정 파일 로드
    config = load_config(args.config) if os.path.exists(args.config) else {}
    
    # 인수로 지정된 설정이 있으면 우선 적용
    languages = args.languages or config.get("languages", ["python"])
    files_per_language = args.files_per_language or config.get("files_per_language", 500000)
    output_dir = args.output_dir or config.get("output_dir", "data/raw")
    use_streaming = args.streaming if args.streaming else config.get("use_streaming", True)
    
    setup_logging()
    
    for language in languages:
        download_language_dataset(
            language, 
            max_files=files_per_language,
            output_dir=output_dir,
            use_streaming=use_streaming
        )

if __name__ == "__main__":
    main()