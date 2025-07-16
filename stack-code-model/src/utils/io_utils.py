#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
입출력 유틸리티 함수
"""

import os
import json
import gzip
import shutil
import tempfile
from typing import Dict, List, Any, Union, Iterator

def read_jsonl(file_path: str, limit: int = None) -> List[Dict[str, Any]]:
    """
    JSONL 파일 읽기
    
    Args:
        file_path: 파일 경로
        limit: 최대 읽을 항목 수
        
    Returns:
        JSON 객체 리스트
    """
    result = []
    
    # gzip 압축 확인
    is_gzipped = file_path.endswith('.gz')
    opener = gzip.open if is_gzipped else open
    
    with opener(file_path, 'rt', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if limit and i >= limit:
                break
                
            try:
                item = json.loads(line.strip())
                result.append(item)
            except json.JSONDecodeError:
                print(f"Warning: Invalid JSON at line {i+1}")
                
    return result

def write_jsonl(items: List[Dict[str, Any]], file_path: str, compress: bool = False) -> bool:
    """
    JSONL 파일 쓰기
    
    Args:
        items: JSON 객체 리스트
        file_path: 파일 경로
        compress: gzip 압축 여부
        
    Returns:
        성공 여부
    """
    # 디렉터리 생성
    os.makedirs(os.path.dirname(os.path.abspath(file_path)), exist_ok=True)
    
    # 파일 확장자 조정
    if compress and not file_path.endswith('.gz'):
        file_path += '.gz'
    
    try:
        opener = gzip.open if compress else open
        with opener(file_path, 'wt', encoding='utf-8') as f:
            for item in items:
                f.write(json.dumps(item) + '\n')
        return True
    except Exception as e:
        print(f"Error writing JSONL: {e}")
        return False

def stream_jsonl(file_path: str) -> Iterator[Dict[str, Any]]:
    """
    JSONL 파일 스트리밍 읽기 (대용량 파일용)
    
    Args:
        file_path: 파일 경로
        
    Yields:
        JSON 객체
    """
    # gzip 압축 확인
    is_gzipped = file_path.endswith('.gz')
    opener = gzip.open if is_gzipped else open
    
    with opener(file_path, 'rt', encoding='utf-8') as f:
        for i, line in enumerate(f):
            try:
                yield json.loads(line.strip())
            except json.JSONDecodeError:
                print(f"Warning: Invalid JSON at line {i+1}")

def append_jsonl(item: Dict[str, Any], file_path: str, compress: bool = False) -> bool:
    """
    JSONL 파일에 단일 항목 추가
    
    Args:
        item: JSON 객체
        file_path: 파일 경로
        compress: gzip 압축 여부
        
    Returns:
        성공 여부
    """
    # 디렉터리 생성
    os.makedirs(os.path.dirname(os.path.abspath(file_path)), exist_ok=True)
    
    # 압축 파일 처리 (gzip은 직접 추가 불가능하므로 임시 파일 사용)
    if compress or file_path.endswith('.gz'):
        # 현재 파일이 있으면 읽기
        existing_data = []
        if os.path.exists(file_path):
            existing_data = list(stream_jsonl(file_path))
            
        # 새 항목 추가
        existing_data.append(item)
        
        # 다시 쓰기
        return write_jsonl(existing_data, file_path, compress=True)
    else:
        # 비압축 파일은 직접 추가 가능
        try:
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(json.dumps(item) + '\n')
            return True
        except Exception as e:
            print(f"Error appending to JSONL: {e}")
            return False

def safe_write(data: Union[str, bytes], file_path: str, mode: str = 'w') -> bool:
    """
    안전한 파일 쓰기 (임시 파일 사용)
    
    Args:
        쓸 데이터
        file_path: 대상 파일 경로
        mode: 파일 모드 ('w' or 'wb')
        
    Returns:
        성공 여부
    """
    # 디렉터리 생성
    os.makedirs(os.path.dirname(os.path.abspath(file_path)), exist_ok=True)
    
    # 임시 파일에 쓰기
    try:
        temp_fd, temp_path = tempfile.mkstemp(dir=os.path.dirname(file_path))
        try:
            with os.fdopen(temp_fd, mode) as f:
                f.write(data)
            
            # 기존 파일 백업 (있는 경우)
            if os.path.exists(file_path):
                backup_path = file_path + '.bak'
                try:
                    shutil.copy2(file_path, backup_path)
                except Exception as e:
                    print(f"Warning: Failed to create backup: {e}")
            
            # 임시 파일을 실제 파일로 이동
            shutil.move(temp_path, file_path)
            return True
        finally:
            # 임시 파일이 남아있으면 삭제
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    except Exception as e:
        print(f"Error writing file safely: {e}")
        return False

def ensure_directory(path: str) -> bool:
    """
    디렉터리 존재 확인 및 생성
    
    Args:
        path: 디렉터리 경로
        
    Returns:
        성공 여부
    """
    try:
        os.makedirs(path, exist_ok=True)
        return True
    except Exception as e:
        print(f"Error creating directory {path}: {e}")
        return False

def get_file_size(file_path: str) -> int:
    """
    파일 크기 확인 (바이트 단위)
    
    Args:
        file_path: 파일 경로
        
    Returns:
        파일 크기 (바이트)
    """
    try:
        return os.path.getsize(file_path)
    except Exception:
        return 0

def count_lines(file_path: str) -> int:
    """
    파일 라인 수 계산
    
    Args:
        file_path: 파일 경로
        
    Returns:
        라인 수
    """
    # gzip 압축 확인
    is_gzipped = file_path.endswith('.gz')
    opener = gzip.open if is_gzipped else open
    
    try:
        with opener(file_path, 'rt', encoding='utf-8') as f:
            return sum(1 for _ in f)
    except Exception as e:
        print(f"Error counting lines in {file_path}: {e}")
        return 0