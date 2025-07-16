#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
설정 관리 유틸리티
"""

import os
import json
from typing import Dict, Any, Optional

def load_config(config_path: str) -> Dict[str, Any]:
    """
    JSON 설정 파일 로드
    
    Args:
        config_path: 설정 파일 경로
        
    Returns:
        설정 딕셔너리
    """
    if not os.path.exists(config_path):
        print(f"Warning: Config file {config_path} not found. Using defaults.")
        return {}
        
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading config from {config_path}: {e}")
        return {}

def save_config(config_data: Dict[str, Any], config_path: str) -> bool:
    """
    설정을 JSON 파일로 저장
    
    Args:
        config_data: 설정 딕셔너리
        config_path: 저장할 파일 경로
        
    Returns:
        성공 여부
    """
    try:
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        with open(config_path, 'w') as f:
            json.dump(config_data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving config to {config_path}: {e}")
        return False

def get_config_value(config: Dict[str, Any], key: str, default: Any = None) -> Any:
    """
    설정값 가져오기 (중첩된 키 지원)
    
    Args:
        config: 설정 딕셔너리
        key: 키 (점 구분, 예: "data.filters.quality_threshold")
        default: 기본값
        
    Returns:
        설정값 또는 기본값
    """
    if "." not in key:
        return config.get(key, default)
        
    parts = key.split(".")
    current = config
    
    for part in parts:
        if not isinstance(current, dict) or part not in current:
            return default
        current = current[part]
        
    return current

def merge_configs(base_config: Dict[str, Any], override_config: Dict[str, Any]) -> Dict[str, Any]:
    """
    두 설정 딕셔너리 병합 (override가 우선)
    
    Args:
        base_config: 기본 설정
        override_config: 덮어쓸 설정
        
    Returns:
        병합된 설정
    """
    result = base_config.copy()
    
    for key, value in override_config.items():
        if (
            key in result and 
            isinstance(result[key], dict) and 
            isinstance(value, dict)
        ):
            # 재귀적으로 중첩된 딕셔너리 병합
            result[key] = merge_configs(result[key], value)
        else:
            # 값 덮어쓰기
            result[key] = value
            
    return result

def get_env_config(prefix: str = "STACK_") -> Dict[str, Any]:
    """
    환경 변수에서 설정값 가져오기
    
    Args:
        prefix: 환경 변수 접두사
        
    Returns:
        환경 변수 기반 설정 딕셔너리
    """
    config = {}
    
    for key, value in os.environ.items():
        if key.startswith(prefix):
            config_key = key[len(prefix):].lower()
            
            # 중첩된 키 처리 (예: STACK_DATA_FILTER_QUALITY -> data.filter.quality)
            if "_" in config_key:
                parts = config_key.split("_")
                current = config
                
                for i, part in enumerate(parts[:-1]):
                    if part not in current:
                        current[part] = {}
                    current = current[part]
                    
                current[parts[-1]] = _convert_env_value(value)
            else:
                config[config_key] = _convert_env_value(value)
                
    return config

def _convert_env_value(value: str) -> Any:
    """환경 변수 값을 적절한 타입으로 변환"""
    # 불리언 변환
    if value.lower() in ("true", "yes", "1"):
        return True
    if value.lower() in ("false", "no", "0"):
        return False
        
    # 숫자 변환
    try:
        if "." in value:
            return float(value)
        else:
            return int(value)
    except ValueError:
        pass
        
    # 그 외에는 문자열로 처리
    return value