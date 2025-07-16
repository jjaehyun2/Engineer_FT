#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
모델 추론 스크립트
"""

import os
import json
import argparse
import logging
from typing import Dict, Any, List, Optional, Union

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from src.utils.logging_utils import setup_logging
from src.utils.io_utils import read_jsonl, ensure_directory, write_jsonl

logger = logging.getLogger(__name__)

class CodeGenerator:
    """코드 생성 클래스"""
    
    def __init__(
        self, 
        model_path: str, 
        device: Optional[str] = None,
        config_file: Optional[str] = None
    ):
        """
        Args:
            model_path: 모델 경로
            device: 실행 장치
            config_file: 설정 파일 경로
        """
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        logger.info(f"모델 로드: {model_path} (장치: {self.device})")
        
        # 모델 및 토크나이저 로드
        self.model = AutoModelForCausalLM.from_pretrained(model_path)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        
        # 모델을 장치로 이동
        self.model.to(self.device)
        self.model.eval()
        
        # 설정 로드
        self.config = {}
        if config_file and os.path.exists(config_file):
            with open(config_file, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        
        # 생성 파라미터 기본값 설정
        self.generation_config = self.config.get("inference", {})
        
        logger.info("코드 생성기 초기화 완료")
    
    def generate(
        self, 
        prompt: str,
        max_new_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        top_k: Optional[int] = None,
        num_return_sequences: int = 1,
        stop_tokens: Optional[List[str]] = None
    ) -> List[str]:
        """
        코드 생성
        
        Args:
            prompt: 생성 시작 프롬프트
            max_new_tokens: 최대 새 토큰 수
            temperature: 샘플링 온도
            top_p: 핵 샘플링 확률
            top_k: 상위 k 샘플링
            num_return_sequences: 반환할 시퀀스 수
            stop_tokens: 생성 중단 토큰 목록
        
        Returns:
            생성된 코드 목록
        """
        # 기본값 설정
        max_new_tokens = max_new_tokens or self.generation_config.get("max_new_tokens", 256)
        temperature = temperature or self.generation_config.get("temperature", 0.8)
        top_p = top_p or self.generation_config.get("top_p", 0.95)
        top_k = top_k or self.generation_config.get("top_k", 50)
        
        # 입력 인코딩
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt").to(self.device)
        
        # 생성 파라미터
        gen_kwargs = {
            "max_new_tokens": max_new_tokens,
            "do_sample": temperature > 0,
            "num_return_sequences": num_return_sequences,
            "pad_token_id": self.tokenizer.eos_token_id,
        }
        
        # 샘플링 파라미터 (온도가 0보다 큰 경우에만 적용)
        if temperature > 0:
            gen_kwargs.update({
                "temperature": temperature,
                "top_p": top_p,
                "top_k": top_k,
                "repetition_penalty": self.generation_config.get("repetition_penalty", 1.2),
                "no_repeat_ngram_size": self.generation_config.get("no_repeat_ngram_size", 3),
            })
        
        # 생성
        with torch.no_grad():
            output_sequences = self.model.generate(
                input_ids=input_ids,
                **gen_kwargs
            )
        
        # 토큰을 텍스트로 디코딩
        generations = []
        for sequence in output_sequences:
            # 입력 프롬프트 제외하고 디코딩
            generated_text = self.tokenizer.decode(
                sequence[len(input_ids[0]):], 
                skip_special_tokens=True,
                clean_up_tokenization_spaces=True
            )
            
            # 중단 토큰 처리
            if stop_tokens:
                for stop_token in stop_tokens:
                    if stop_token in generated_text:
                        generated_text = generated_text.split(stop_token)[0]
            
            generations.append(generated_text)
        
        return generations
    
    def process_file(
        self, 
        input_file: str, 
        output_file: str, 
        prompt_field: str = "prompt",
        max_samples: Optional[int] = None,
        **generation_kwargs
    ) -> List[Dict[str, Any]]:
        """
        파일에서 프롬프트를 읽어 코드 생성 후 결과 저장
        
        Args:
            input_file: 입력 파일 경로 (JSONL)
            output_file: 출력 파일 경로 (JSONL)
            prompt_field: 입력에서 프롬프트 필드 이름
            max_samples: 처리할 최대 샘플 수
            generation_kwargs: 추가 생성 옵션
            
        Returns:
            생성된 결과 목록
        """
        logger.info(f"입력 파일 처리: {input_file}")
        
        # 입력 파일 읽기
        inputs = read_jsonl(input_file)
        
        # 최대 샘플 수 제한
        if max_samples and max_samples < len(inputs):
            inputs = inputs[:max_samples]
        
        results = []
        for i, item in enumerate(inputs):
            if i % 10 == 0:
                logger.info(f"처리 중: {i}/{len(inputs)}")
            
            if prompt_field not in item:
                logger.warning(f"항목 {i}에 프롬프트 필드({prompt_field})가 없습니다. 건너뜁니다.")
                continue
            
            prompt = item[prompt_field]
            
            try:
                # 코드 생성
                generations = self.generate(prompt, **generation_kwargs)
                
                # 결과 저장
                result = item.copy()  # 원본 항목 복사
                result["generated"] = generations[0] if len(generations) == 1 else generations
                results.append(result)
            except Exception as e:
                logger.error(f"항목 {i} 처리 중 오류 발생: {e}")
        
        # 결과 저장
        if output_file:
            write_jsonl(results, output_file)
            logger.info(f"생성 결과 저장 완료: {output_file}")
        
        return results

def main():
    parser = argparse.ArgumentParser(description="코드 생성 추론 스크립트")
    
    # 모델 및 설정
    parser.add_argument("--model-path", type=str, required=True, help="모델 경로")
    parser.add_argument("--config-file", type=str, help="모델 설정 파일 경로")
    parser.add_argument("--device", type=str, default=None, help="실행 장치 (기본: 사용 가능한 GPU)")
    
    # 입력 방식 선택
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("--prompt", type=str, help="직접 프롬프트 입력")
    input_group.add_argument("--input-file", type=str, help="입력 파일 경로 (JSONL)")
    
    # 출력 설정
    parser.add_argument("--output-file", type=str, help="출력 파일 경로 (JSONL)")
    
    # 생성 설정
    parser.add_argument("--max-new-tokens", type=int, default=None, help="최대 새 토큰 수")
    parser.add_argument("--temperature", type=float, default=None, help="샘플링 온도")
    parser.add_argument("--top-p", type=float, default=None, help="핵 샘플링 확률")
    parser.add_argument("--top-k", type=int, default=None, help="상위 k 샘플링")
    parser.add_argument("--num-return-sequences", type=int, default=1, help="반환할 시퀀스 수")
    
    # 파일 처리 옵션
    parser.add_argument("--prompt-field", type=str, default="prompt", help="프롬프트 필드 이름")
    parser.add_argument("--max-samples", type=int, default=None, help="처리할 최대 샘플 수")
    
    # 기타 설정
    parser.add_argument("--log-level", type=str, default="INFO", help="로그 레벨")
    
    args = parser.parse_args()
    
    # 로깅 설정
    setup_logging(log_level=args.log_level)
    
    # 코드 생성기 초기화
    generator = CodeGenerator(
        model_path=args.model_path,
        device=args.device,
        config_file=args.config_file
    )
    
    # 생성 설정 추출
    generation_kwargs = {
        "max_new_tokens": args.max_new_tokens,
        "temperature": args.temperature,
        "top_p": args.top_p,
        "top_k": args.top_k,
        "num_return_sequences": args.num_return_sequences
    }
    
    # 유효한 값만 필터링
    generation_kwargs = {k: v for k, v in generation_kwargs.items() if v is not None}
    
    # 입력 방식에 따라 처리
    if args.prompt:
        # 직접 프롬프트로 생성
        generations = generator.generate(args.prompt, **generation_kwargs)
        
        print("\n=== 생성 결과 ===")
        for i, generation in enumerate(generations):
            print(f"\n--- 결과 {i+1} ---")
            print(generation)
        
        # 출력 파일이 있으면 저장
        if args.output_file:
            results = [{"prompt": args.prompt, "generated": generations}]
            write_jsonl(results, args.output_file)
            logger.info(f"생성 결과 저장 완료: {args.output_file}")
    
    else:
        # 파일에서 입력 처리
        if not args.output_file:
            # 출력 파일 이름 자동 생성
            base_dir = os.path.dirname(args.input_file)
            base_name = os.path.basename(args.input_file)
            name_parts = os.path.splitext(base_name)
            args.output_file = os.path.join(base_dir, f"{name_parts[0]}_generated{name_parts[1]}")
        
        # 입력 파일 처리
        results = generator.process_file(
            input_file=args.input_file,
            output_file=args.output_file,
            prompt_field=args.prompt_field,
            max_samples=args.max_samples,
            **generation_kwargs
        )
        
        logger.info(f"총 {len(results)}개 항목 처리 완료")

if __name__ == "__main__":
    main()