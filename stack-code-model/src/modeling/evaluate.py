#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
모델 평가 스크립트
"""

import os
import json
import argparse
import logging
from typing import Dict, Any, List, Optional, Tuple

import torch
import numpy as np
from transformers import AutoModelForCausalLM, AutoTokenizer
from datasets import load_dataset
import evaluate

from src.utils.logging_utils import setup_logging
from src.utils.io_utils import read_jsonl, ensure_directory, write_jsonl

logger = logging.getLogger(__name__)

class ModelEvaluator:
    """모델 평가 클래스"""
    
    def __init__(self, model, tokenizer, device=None):
        """
        Args:
            model: 평가할 모델
            tokenizer: 토크나이저
            device: 실행 장치
        """
        self.model = model
        self.tokenizer = tokenizer
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        self.model.eval()
        
        # 기본 평가 지표
        self.metrics = {
            "perplexity": evaluate.load("perplexity"),
            "bleu": evaluate.load("bleu")
        }
        
        logger.info(f"모델 평가 준비 완료 (장치: {self.device})")
    
    def evaluate_perplexity(self, dataset, text_field="content", batch_size=4) -> Dict[str, float]:
        """텍스트 데이터셋에 대한 PPL 계산"""
        logger.info("perplexity 계산 중...")
        
        results = self.metrics["perplexity"].compute(
            model_id=self.model.config._name_or_path,
            predictions=dataset[text_field],
            batch_size=batch_size,
            device=self.device
        )
        
        return {"perplexity": results["mean_perplexity"]}
    
    def evaluate_code_generation(
        self, 
        dataset, 
        prompt_field="prompt", 
        reference_field="completion",
        num_examples=100,
        max_length=256,
        temperature=0.8,
        top_p=0.95
    ) -> Dict[str, Any]:
        """코드 생성 품질 평가"""
        logger.info("코드 생성 평가 중...")
        
        # 결과 저장
        generations = []
        
        # 평가 결과
        exact_matches = 0
        bleu_scores = []
        
        # 랜덤 샘플링
        if num_examples < len(dataset):
            indices = np.random.choice(len(dataset), num_examples, replace=False)
            eval_samples = [dataset[idx] for idx in indices]
        else:
            eval_samples = dataset
        
        for i, sample in enumerate(eval_samples):
            prompt = sample[prompt_field]
            reference = sample[reference_field]
            
            # 모델 생성
            input_ids = self.tokenizer.encode(prompt, return_tensors="pt").to(self.device)
            
            with torch.no_grad():
                output = self.model.generate(
                    input_ids,
                    max_length=len(input_ids[0]) + max_length,
                    temperature=temperature,
                    top_p=top_p,
                    do_sample=temperature > 0,
                    pad_token_id=self.tokenizer.eos_token_id
                )
            
            generated_code = self.tokenizer.decode(output[0][len(input_ids[0]):], skip_special_tokens=True)
            
            # 정확한 일치 확인
            if generated_code.strip() == reference.strip():
                exact_matches += 1
            
            # BLEU 점수 계산
            bleu_result = self.metrics["bleu"].compute(
                predictions=[generated_code.strip()],
                references=[[reference.strip()]]
            )
            bleu_scores.append(bleu_result["bleu"])
            
            # 결과 저장
            generations.append({
                "prompt": prompt,
                "generated": generated_code,
                "reference": reference,
                "bleu": bleu_result["bleu"],
                "exact_match": generated_code.strip() == reference.strip()
            })
            
            if i % 10 == 0:
                logger.info(f"진행: {i}/{len(eval_samples)}")
        
        # 결과 집계
        results = {
            "exact_match_rate": exact_matches / len(eval_samples),
            "avg_bleu": sum(bleu_scores) / len(bleu_scores),
            "generations": generations
        }
        
        return results

def load_model_and_tokenizer(model_path: str) -> Tuple[AutoModelForCausalLM, AutoTokenizer]:
    """모델과 토크나이저 로드"""
    logger.info(f"모델과 토크나이저 로드: {model_path}")
    
    model = AutoModelForCausalLM.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    
    return model, tokenizer

def evaluate_model(args):
    """모델 평가 실행"""
    # 로깅 설정
    setup_logging(log_level=args.log_level)
    
    # 모델 및 토크나이저 로드
    model, tokenizer = load_model_and_tokenizer(args.model_path)
        # 데이터셋 로드
    logger.info(f"평가 데이터셋 로드: {args.test_file}")
    if args.test_file.endswith('.jsonl') or args.test_file.endswith('.jsonl.gz'):
        dataset = load_dataset('json', data_files=args.test_file)['train']
    else:
        dataset = load_dataset(args.test_file)
    
    logger.info(f"데이터셋 크기: {len(dataset)} 샘플")
    
    # 평가기 초기화
    evaluator = ModelEvaluator(model, tokenizer, device=args.device)
    
    # 결과 저장 디렉터리
    ensure_directory(args.output_dir)
    
    # 모델 설정 로드 (있는 경우)
    model_config = {}
    if args.config_file and os.path.exists(args.config_file):
        with open(args.config_file, 'r', encoding='utf-8') as f:
            model_config = json.load(f)
    
    eval_config = model_config.get("evaluation", {})
    
    # 평가 실행
    results = {}
    
    # 퍼플렉시티 계산 (텍스트 필드가 있는 경우)
    if args.text_field in dataset.column_names:
        try:
            ppl_results = evaluator.evaluate_perplexity(
                dataset, 
                text_field=args.text_field,
                batch_size=args.batch_size
            )
            results.update(ppl_results)
            logger.info(f"Perplexity: {ppl_results['perplexity']:.4f}")
        except Exception as e:
            logger.error(f"퍼플렉시티 계산 오류: {e}")
    
    # 코드 생성 평가 (프롬프트와 참조 필드가 있는 경우)
    if args.prompt_field in dataset.column_names and args.reference_field in dataset.column_names:
        try:
            generation_results = evaluator.evaluate_code_generation(
                dataset,
                prompt_field=args.prompt_field,
                reference_field=args.reference_field,
                num_examples=args.num_examples,
                max_length=eval_config.get("generation_max_length", 256),
                temperature=eval_config.get("temperature", 0.8),
                top_p=eval_config.get("top_p", 0.95)
            )
            
            # 생성 결과에서 메트릭만 추출
            for key, value in generation_results.items():
                if key != "generations":
                    results[key] = value
            
            logger.info(f"정확도(Exact Match): {generation_results['exact_match_rate']:.4f}")
            logger.info(f"평균 BLEU 점수: {generation_results['avg_bleu']:.4f}")
            
            # 생성 결과 저장
            generations_file = os.path.join(args.output_dir, "generations.jsonl")
            write_jsonl(generation_results["generations"], generations_file)
            logger.info(f"생성 결과 저장 완료: {generations_file}")
        except Exception as e:
            logger.error(f"코드 생성 평가 오류: {e}")
    
    # 전체 결과 저장
    results_file = os.path.join(args.output_dir, "evaluation_results.json")
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    logger.info(f"평가 결과 저장 완료: {results_file}")
    
    return results

def main():
    parser = argparse.ArgumentParser(description="코드 모델 평가 스크립트")
    
    # 필수 인자
    parser.add_argument("--model-path", type=str, required=True, help="평가할 모델 경로")
    parser.add_argument("--test-file", type=str, required=True, help="테스트 데이터 파일")
    parser.add_argument("--output-dir", type=str, required=True, help="결과 저장 디렉터리")
    
    # 평가 설정 인자
    parser.add_argument("--config-file", type=str, help="모델 설정 파일 경로")
    parser.add_argument("--text-field", type=str, default="content", help="텍스트 필드 이름")
    parser.add_argument("--prompt-field", type=str, default="prompt", help="프롬프트 필드 이름")
    parser.add_argument("--reference-field", type=str, default="completion", help="참조 필드 이름")
    parser.add_argument("--batch-size", type=int, default=8, help="평가 배치 크기")
    parser.add_argument("--num-examples", type=int, default=100, help="코드 생성 평가 예제 수")
    parser.add_argument("--device", type=str, default=None, help="실행 장치 (기본: 사용 가능한 GPU)")
    parser.add_argument("--log-level", type=str, default="INFO", help="로그 레벨")
    
    args = parser.parse_args()
    
    # 평가 실행
    evaluate_model(args)

if __name__ == "__main__":
    main()