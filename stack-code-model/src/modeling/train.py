#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
모델 학습 스크립트
"""

import os
import json
import argparse
import logging
from typing import Dict, Any, Optional

import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    Trainer, 
    TrainingArguments,
    DataCollatorForLanguageModeling,
    set_seed
)
from datasets import load_dataset

from src.utils.logging_utils import setup_logging
from src.utils.io_utils import read_jsonl, ensure_directory

logger = logging.getLogger(__name__)

def load_config(config_path: str) -> Dict[str, Any]:
    """모델 설정 로드"""
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def train_model(args):
    """모델 학습 실행"""
    # 로깅 설정
    setup_logging(log_level=args.log_level)
    
    # 설정 로드
    logger.info(f"설정 로드: {args.config_file}")
    config = load_config(args.config_file)
    
    # 데이터 설정
    data_config = config.get("data", {})
    train_file = args.train_file or data_config.get("train_file")
    validation_file = args.validation_file or data_config.get("validation_file")
    
    if not train_file or not os.path.exists(train_file):
        raise ValueError(f"유효한 훈련 파일이 필요합니다: {train_file}")
    
    # 출력 디렉터리 생성
    output_dir = args.output_dir
    ensure_directory(output_dir)
    logger.info(f"출력 디렉터리: {output_dir}")
    
    # 토크나이저 로드 또는 사용
    if args.tokenizer_path:
        logger.info(f"토크나이저 로드: {args.tokenizer_path}")
        tokenizer = AutoTokenizer.from_pretrained(args.tokenizer_path)
    else:
        logger.warning("토크나이저가 지정되지 않았습니다. 기본 GPT-2 토크나이저를 사용합니다.")
        tokenizer = AutoTokenizer.from_pretrained("gpt2")
    
    # 데이터셋 로드
    logger.info("데이터셋 로드 중...")
    max_seq_length = data_config.get("max_seq_length", 1024)
    
    # HuggingFace datasets 라이브러리 사용
    dataset = load_dataset(
        'json', 
        data_files={
            'train': train_file, 
            'validation': validation_file if validation_file else train_file
        }
    )
    
    # 필요한 텍스트 필드 확인
    text_field = data_config.get("text_field", "content")
    
    # 토크나이징 함수
    def tokenize_function(examples):
        return tokenizer(
            examples[text_field], 
            truncation=True, 
            max_length=max_seq_length,
            padding="max_length"
        )
    
    # 데이터셋 토크나이징
    tokenized_datasets = dataset.map(
        tokenize_function,
        batched=True,
        num_proc=data_config.get("preprocessing_num_workers", 4),
        remove_columns=[col for col in dataset["train"].column_names if col != text_field]
    )
    
    # 모델 로드 또는 초기화
    if args.model_path:
        logger.info(f"모델 로드: {args.model_path}")
        model = AutoModelForCausalLM.from_pretrained(args.model_path)
    else:
        # 설정에 따라 모델 크기 선택
        model_size = config.get("model", {}).get("model_size", "base")
        model_mapping = {
            "small": "gpt2",
            "base": "gpt2-medium",
            "large": "gpt2-large",
            "xl": "gpt2-xl"
        }
        base_model = model_mapping.get(model_size, "gpt2-medium")
        
        logger.info(f"새 모델 초기화: {base_model} 기반")
        model = AutoModelForCausalLM.from_pretrained(base_model)
    
    # 데이터 콜레이터 설정
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False  # 자기회귀 모델이므로 MLM=False
    )
    
    # 훈련 설정
    train_config = config.get("training", {})
    training_args = TrainingArguments(
        output_dir=output_dir,
        overwrite_output_dir=True,
        
        # 학습 파라미터
        per_device_train_batch_size=train_config.get("micro_batch_size", 4),
        per_device_eval_batch_size=train_config.get("micro_batch_size", 4),
        gradient_accumulation_steps=train_config.get("gradient_accumulation_steps", 8),
        learning_rate=train_config.get("learning_rate", 5e-5),
        weight_decay=train_config.get("weight_decay", 0.01),
        max_grad_norm=train_config.get("max_grad_norm", 1.0),
        
        # 스케줄러
        num_train_epochs=train_config.get("num_train_epochs", 3),
        warmup_steps=train_config.get("warmup_steps", 10000),
        lr_scheduler_type=train_config.get("lr_scheduler", "cosine"),
        
        # 로깅 및 평가
        logging_dir=os.path.join(output_dir, "logs"),
        logging_steps=train_config.get("logging_steps", 100),
        evaluation_strategy=train_config.get("evaluation_strategy", "steps"),
        eval_steps=train_config.get("eval_steps", 500),
        save_steps=train_config.get("save_steps", 1000),
        save_total_limit=config.get("checkpoint", {}).get("save_total_limit", 3),
        
        # 기타 설정
        fp16=args.fp16,
        dataloader_num_workers=args.num_workers,
        seed=args.seed
    )
    
    # 훈련 객체 생성
    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["validation"]
    )
    
    # 학습 실행
    logger.info("모델 학습 시작...")
    train_result = trainer.train(resume_from_checkpoint=args.resume_from_checkpoint)
    
    # 최종 모델 저장
    logger.info(f"최종 모델 저장: {output_dir}")
    trainer.save_model(output_dir)
    tokenizer.save_pretrained(output_dir)
    
    # 훈련 지표 저장
    metrics = train_result.metrics
    trainer.log_metrics("train", metrics)
    trainer.save_metrics("train", metrics)
    trainer.save_state()
    
    logger.info("학습 완료!")
    return model, tokenizer

def main():
    parser = argparse.ArgumentParser(description="코드 모델 학습 스크립트")
    
    # 필수 인자
    parser.add_argument("--config-file", type=str, required=True, help="모델 설정 파일 경로")
    parser.add_argument("--output-dir", type=str, required=True, help="출력 디렉터리")
    
    # 선택적 인자
    parser.add_argument("--train-file", type=str, help="훈련 데이터 파일")
    parser.add_argument("--validation-file", type=str, help="검증 데이터 파일")
    parser.add_argument("--model-path", type=str, help="사전 훈련된 모델 경로")
    parser.add_argument("--tokenizer-path", type=str, help="토크나이저 경로")
    parser.add_argument("--resume-from-checkpoint", action="store_true", help="체크포인트에서 재개")
    parser.add_argument("--fp16", action="store_true", help="FP16 학습 사용")
    parser.add_argument("--num-workers", type=int, default=4, help="데이터 로더 워커 수")
    parser.add_argument("--seed", type=int, default=42, help="랜덤 시드")
    parser.add_argument("--log-level", type=str, default="INFO", help="로그 레벨")
    
    args = parser.parse_args()
    
    # 시드 설정
    set_seed(args.seed)
    
    # 학습 실행
    train_model(args)

if __name__ == "__main__":
    main()