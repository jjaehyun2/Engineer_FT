#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
로깅 설정 유틸리티
"""

import os
import sys
import logging
from datetime import datetime

def setup_logging(
    log_level: str = "INFO",
    log_file: str = None,
    log_format: str = None
) -> logging.Logger:
    """
    로깅 시스템 설정
    
    Args:
        log_level: 로그 레벨 (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: 로그 파일 경로 (None이면 콘솔만 사용)
        log_format: 로그 포맷 문자열
        
    Returns:
        설정된 루트 로거
    """
    # 로그 레벨 설정
    level = getattr(logging, log_level.upper(), logging.INFO)
    
    # 기본 포맷
    if log_format is None:
        log_format = "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
        
    # 로그 핸들러 설정
    handlers = []
    
    # 콘솔 핸들러
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter(log_format))
    handlers.append(console_handler)
    
        # 파일 핸들러 (지정된 경우)
    if log_file:
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
            
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter(log_format))
        handlers.append(file_handler)
    
    # 로거 설정
    logging.basicConfig(
        level=level,
        format=log_format,
        handlers=handlers
    )
    
    # 타사 라이브러리 로깅 레벨 조정
    logging.getLogger("datasets").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("huggingface_hub").setLevel(logging.WARNING)
    
    return logging.getLogger()

def get_logger(name: str, log_level: str = None) -> logging.Logger:
    """
    특정 이름의 로거 가져오기
    
    Args:
        name: 로거 이름
        log_level: 로그 레벨 (None이면 기본값 사용)
        
    Returns:
        설정된 로거
    """
    logger = logging.getLogger(name)
    
    if log_level:
        level = getattr(logging, log_level.upper(), None)
        if level:
            logger.setLevel(level)
            
    return logger

def setup_file_logger(name: str, file_path: str = None) -> logging.Logger:
    """
    파일 로깅 설정이 추가된 로거 생성
    
    Args:
        name: 로거 이름
        file_path: 로그 파일 경로 (None이면 자동 생성)
        
    Returns:
        설정된 로거
    """
    logger = logging.getLogger(name)
    
    # 이미 핸들러가 설정된 경우 건너뛰기
    if logger.handlers:
        return logger
        
    # 파일 경로 자동 생성
    if file_path is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        file_path = f"{log_dir}/{name}_{timestamp}.log"
    
    # 포맷 설정
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
    )
    
    # 파일 핸들러 추가
    file_handler = logging.FileHandler(file_path)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # 콘솔 핸들러 추가
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    logger.setLevel(logging.INFO)
    logger.propagate = False  # 로그 전파 방지
    
    return logger

def log_execution_time(logger, start_time=None):
    """
    실행 시간 로깅을 위한 데코레이터
    
    사용법:
    @log_execution_time(logger)
    def my_function():
        ...
    """
    from functools import wraps
    from time import time
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = start_time or time()
            try:
                result = func(*args, **kwargs)
                elapsed = time() - start
                logger.info(f"{func.__name__} completed in {elapsed:.2f} seconds")
                return result
            except Exception as e:
                elapsed = time() - start
                logger.error(f"{func.__name__} failed after {elapsed:.2f} seconds: {e}")
                raise
        return wrapper
        
    return decorator