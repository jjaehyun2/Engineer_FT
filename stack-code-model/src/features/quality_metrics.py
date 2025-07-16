#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
코드 품질 메트릭 계산 유틸리티
"""

import re
import math
from typing import Dict, Any

def calculate_code_quality(example: Dict[str, Any], language: str) -> float:
    """
    코드 품질 점수 계산
    
    Args:
        example: 전처리된 코드 예제
        language: 프로그래밍 언어
        
    Returns:
        0.0-1.0 범위의 품질 점수
    """
    # 기본 품질 점수
    quality_score = 0.0
    max_score = 0.0
    
    # 1. 문서화 점수 (가중치: 0.4)
    doc_score = _calculate_documentation_score(example)
    quality_score += 0.4 * doc_score
    max_score += 0.4
    
    # 2. 복잡도 점수 (가중치: 0.2)
    complexity_score = _calculate_complexity_score(example)
    quality_score += 0.2 * complexity_score
    max_score += 0.2
    
    # 3. 코드 구조 점수 (가중치: 0.2)
    structure_score = _calculate_structure_score(example, language)
    quality_score += 0.2 * structure_score
    max_score += 0.2
    
    # 4. 메타데이터 품질 (가중치: 0.1)
    meta_score = _calculate_meta_score(example)
    quality_score += 0.1 * meta_score
    max_score += 0.1
    
    # 5. 언어별 특화 점수 (가중치: 0.1)
    lang_score = _calculate_language_specific_score(example, language)
    quality_score += 0.1 * lang_score
    max_score += 0.1
    
    # 정규화 (필요한 경우)
    if max_score > 0:
        quality_score = quality_score / max_score
        
    return quality_score

def _calculate_documentation_score(example: Dict[str, Any]) -> float:
    """문서화 품질 점수"""
    # 문서 문자열이 없는 경우
    if "docstrings" not in example:
        return 0.0
        
    docstrings = example["docstrings"]
    functions = example.get("functions", [])
    
    # 함수가 없는 경우
    if not functions:
        return 0.0
        
    # 모듈 수준 문서 (0.2)
    module_doc_score = 0.2 if docstrings.get("module") else 0.0
    
    # 함수 문서화 비율 (0.6)
    func_doc_count = len(docstrings.get("functions", {}))
    func_count = len(functions)
    func_doc_ratio = func_doc_count / func_count if func_count > 0 else 0
    func_doc_score = 0.6 * func_doc_ratio
    
    # 문서 품질 (0.2)
    doc_quality = docstrings.get("quality_score", 0.0)
    doc_quality_score = 0.2 * doc_quality
    
    return module_doc_score + func_doc_score + doc_quality_score

def _calculate_complexity_score(example: Dict[str, Any]) -> float:
    """복잡도 기반 품질 점수 (낮은 복잡도 = 높은 점수)"""
    # 복잡도 지표
    complexity = example.get("complexity", 10)  # 기본값 10
    
    # 코드 크기
    line_count = example.get("line_count", 100)
    
    # 상대적 복잡도 (코드 크기 대비)
    relative_complexity = complexity / (line_count / 10) if line_count > 0 else complexity
    
    # 복잡도 점수 변환 (0-1 범위, 낮을수록 좋음)
    # 상대적 복잡도 5 이하면 만점, 20 이상이면 최저점
    if relative_complexity <= 5:
        return 1.0
    elif relative_complexity >= 20:
        return 0.0
    else:
        return 1.0 - ((relative_complexity - 5) / 15)

def _calculate_structure_score(example: Dict[str, Any], language: str) -> float:
    """코드 구조 품질 점수"""
    # 구조 점수 초기화
    structure_score = 0.5  # 기본 점수
    
    # 함수 및 클래스 존재 여부
    functions = example.get("functions", [])
    classes = example.get("classes", [])
    
    # 함수가 있으면 +0.2
    if functions:
        structure_score += 0.2
        
        # 함수 크기 평가 (작은 함수 = 좋은 구조)
        if isinstance(functions[0], dict) and "code" in functions[0]:
            avg_func_lines = sum(len(f.get("code", "").split("\n")) for f in functions) / len(functions) if functions else 0
            if avg_func_lines < 15:  # 15줄 미만은 좋은 함수 크기
                structure_score += 0.1
            elif avg_func_lines > 50:  # 50줄 초과는 큰 함수
                structure_score -= 0.1
                
    # 클래스가 있으면 +0.1
    if classes:
        structure_score += 0.1
        
    # 임포트 구성
    imports = example.get("imports", [])
    if imports:
        # 다양한 라이브러리 사용 = 복잡한 기능 구현 가능성
        structure_score += min(0.1, len(set(imports)) * 0.02)  # 최대 0.1
        
    # 코드 크기가 너무 크거나 작은 경우 조정
    line_count = example.get("line_count", 0)
    if line_count < 10:  # 너무 작은 코드
        structure_score *= 0.5
    elif line_count > 1000:  # 너무 큰 코드
        structure_score *= 0.7
        
    # 언어별 특화 점수
    if language == "python":
        # Python의 경우 메서드 이름 컨벤션 확인
        if functions and all(f["name"].islower() for f in functions if isinstance(f, dict) and "name" in f):
            structure_score += 0.1
            
    return min(1.0, structure_score)  # 최대 1.0

def _calculate_meta_score(example: Dict[str, Any]) -> float:
    """메타데이터 기반 품질 점수"""
    meta_score = 0.0
    
    # GitHub 별점 (있는 경우)
    stars = example.get("stars", 0)
    if stars > 0:
        # 별점 점수 (최대 0.5)
        if stars >= 100:
            meta_score += 0.5
        elif stars >= 10:
            meta_score += 0.3
        else:
            meta_score += 0.1
    
    # 저장소 경로 정보
    path = example.get("path", "")
    if path:
        # 테스트 코드는 일반적으로 품질이 좋음
        if "test" in path.lower():
            meta_score += 0.2
        
        # 예제 코드도 일반적으로 품질이 좋음
        if "example" in path.lower():
            meta_score += 0.1
            
        # 문서 디렉터리의 코드
        if "doc" in path.lower():
            meta_score += 0.1
    
    # 라이선스 정보 (오픈 소스 = 더 많은 검토 가능성)
    repo = example.get("repo", "")
    if repo:
        # 유명 조직의 저장소
        well_known_orgs = ["google", "microsoft", "facebook", "apache", "mozilla", "aws", "amazon"]
        if any(org in repo.lower() for org in well_known_orgs):
            meta_score += 0.2
    
    return min(1.0, meta_score)  # 최대 1.0

def _calculate_language_specific_score(example: Dict[str, Any], language: str) -> float:
    """언어별 특화 품질 점수"""
    lang_score = 0.5  # 기본 점수
    
    content = ""
    functions = example.get("functions", [])
    for func in functions:
        if isinstance(func, dict) and "code" in func:
            content += func["code"]
    
    if not content:
        content = example.get("content", "")
    
    if language == "python":
        # PEP 8 관련 휴리스틱
        if content:
            # 들여쓰기 일관성 (4칸 또는 탭)
            indentation = re.findall(r"^\s+", content, re.MULTILINE)
            if indentation:
                if all(len(i) % 4 == 0 for i in indentation):
                    lang_score += 0.1
                
            # 명명 규칙
            snake_case_vars = len(re.findall(r"\b[a-z][a-z0-9_]*\b", content))
            camel_case_vars = len(re.findall(r"\b[a-z][a-zA-Z0-9]*[A-Z]", content))
            
            if snake_case_vars > camel_case_vars:  # Python은 snake_case 선호
                lang_score += 0.1
                
            # f-string 사용 (현대적 Python)
            if "f\"" in content or "f'" in content:
                lang_score += 0.1
                
            # 타입 힌트 사용 (현대적 Python)
            if "->" in content or ": " in content:
                lang_score += 0.1
    
    elif language == "javascript":
        # JavaScript 품질 휴리스틱
        if content:
            # 세미콜론 일관성
            semicolons = content.count(";")
            lines = content.count("\n") + 1
            
            if semicolons > lines * 0.7 or semicolons < lines * 0.3:
                # 일관적으로 사용하거나 일관적으로 사용하지 않음
                lang_score += 0.1
                
            # ES6+ 기능 사용
            modern_features = [
                "=>",  # 화살표 함수
                "const ",  # const 키워드
                "let ",  # let 키워드
                "...",  # 스프레드/레스트 연산자
                "class ",  # 클래스
                "async ",  # async/await
                "await "
            ]
            
            modern_score = sum(0.05 for feature in modern_features if feature in content)
            lang_score += min(0.2, modern_score)  # 최대 0.2
            
            # 명명 규칙 (JavaScript는 camelCase 선호)
            snake_case_vars = len(re.findall(r"\b[a-z][a-z0-9_]*_[a-z0-9_]+\b", content))
            camel_case_vars = len(re.findall(r"\b[a-z][a-zA-Z0-9]*[A-Z]", content))
            
            if camel_case_vars > snake_case_vars:
                lang_score += 0.1
    
    elif language == "java":
        # Java 품질 휴리스틱
        if content:
            # 클래스 명명 규칙 (PascalCase)
            pascal_case_classes = len(re.findall(r"class\s+[A-Z][a-zA-Z0-9]*", content))
            if pascal_case_classes > 0:
                lang_score += 0.1
                
            # 메서드 명명 규칙 (camelCase)
            camel_case_methods = len(re.findall(r"\s[a-z][a-zA-Z0-9]*\(", content))
            if camel_case_methods > 0:
                lang_score += 0.1
                
            # 접근 제한자 사용
            access_modifiers = ["public", "private", "protected"]
            if any(modifier in content for modifier in access_modifiers):
                lang_score += 0.1
                
            # 예외 처리
            if "try" in content and "catch" in content:
                lang_score += 0.1
    
    return min(1.0, lang_score)  # 최대 1.0