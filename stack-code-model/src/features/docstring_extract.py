#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
코드에서 문서 문자열(docstring) 추출 및 분석
"""

import ast
import re
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

def extract_docstrings(code_content: str, language: str) -> Dict[str, Any]:
    """
    코드에서 문서 문자열(docstrings) 추출
    
    Args:
        code_content: 코드 내용
        language: 프로그래밍 언어
        
    Returns:
        추출된 문서 문자열 정보
    """
    docstrings = {
        "module": None,
        "classes": {},
        "functions": {},
        "quality_score": 0.0
    }
    
    if language == "python":
        try:
            tree = ast.parse(code_content)
            
            # 모듈 수준 문서 문자열
            module_docstring = ast.get_docstring(tree)
            if module_docstring:
                docstrings["module"] = _clean_docstring(module_docstring)
                
            # 클래스 및 함수 문서 문자열
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    class_docstring = ast.get_docstring(node)
                    if class_docstring:
                        docstrings["classes"][node.name] = _clean_docstring(class_docstring)
                        
                elif isinstance(node, ast.FunctionDef):
                    func_docstring = ast.get_docstring(node)
                    if func_docstring:
                        docstrings["functions"][node.name] = _clean_docstring(func_docstring)
                        
            # 문서 품질 점수 계산
            docstrings["quality_score"] = _calculate_docstring_quality(docstrings, code_content)
            
        except SyntaxError:
            logger.warning("Syntax error while parsing Python code for docstrings")
        except Exception as e:
            logger.warning(f"Error extracting Python docstrings: {e}")
            
    elif language == "javascript":
        # JavaScript 주석 추출 (JSDoc 스타일)
        jsdoc_pattern = r"/\*\*\s*([\s\S]*?)\s*\*/"
        
        for match in re.finditer(jsdoc_pattern, code_content):
            comment = match.group(1)
            # 간단한 분석: 주석 다음에 오는 함수/클래스 이름 추출
            following_code = code_content[match.end():match.end()+200]  # 주석 이후 200자 분석
            
            if "class" in following_code[:following_code.find("{")] if "{" in following_code else "":
                class_match = re.search(r"class\s+(\w+)", following_code)
                if class_match:
                    class_name = class_match.group(1)
                    docstrings["classes"][class_name] = _clean_docstring(comment)
            elif "function" in following_code[:following_code.find("{")] if "{" in following_code else "":
                func_match = re.search(r"function\s+(\w+)", following_code)
                if func_match:
                    func_name = func_match.group(1)
                    docstrings["functions"][func_name] = _clean_docstring(comment)
                    
        docstrings["quality_score"] = len(docstrings["classes"]) + len(docstrings["functions"])
        
    elif language == "java":
        # Java 주석 추출 (JavaDoc 스타일)
        javadoc_pattern = r"/\*\*\s*([\s\S]*?)\s*\*/"
        
        for match in re.finditer(javadoc_pattern, code_content):
            comment = match.group(1)
            following_code = code_content[match.end():match.end()+200]
            
            if "class" in following_code[:following_code.find("{")] if "{" in following_code else "":
                class_match = re.search(r"class\s+(\w+)", following_code)
                if class_match:
                    class_name = class_match.group(1)
                    docstrings["classes"][class_name] = _clean_docstring(comment)
            elif re.search(r"(public|private|protected)\s+\w+\s+\w+\s*\(", following_code):
                func_match = re.search(r"(public|private|protected)\s+\w+\s+(\w+)\s*\(", following_code)
                if func_match:
                    func_name = func_match.group(2)
                    docstrings["functions"][func_name] = _clean_docstring(comment)
    
    return docstrings

def _clean_docstring(docstring: str) -> str:
    """문서 문자열 정리"""
    # 여러 줄 주석에서 각 줄 시작 부분의 * 제거
    docstring = re.sub(r"^\s*\*", "", docstring, flags=re.MULTILINE)
    
    # 앞뒤 공백 제거
    docstring = docstring.strip()
    
    # 들여쓰기 일관성 조정
    lines = docstring.split("\n")
    if len(lines) > 1:
        # 최소 들여쓰기 찾기
        min_indent = min((len(line) - len(line.lstrip())) for line in lines[1:] if line.strip())
        
        # 들여쓰기 제거
        docstring = lines[0] + "\n" + "\n".join(line[min_indent:] if line.strip() else line for line in lines[1:])
        
    return docstring

def _calculate_docstring_quality(docstrings: Dict[str, Any], code_content: str) -> float:
    """문서 문자열 품질 점수 계산"""
    # 기본 점수
    score = 0.0
    
    # 모듈 문서 문자열이 있으면 +0.2
    if docstrings["module"]:
        score += 0.2
        
    # 클래스 문서화 비율
    class_pattern = r"class\s+\w+"
    total_classes = len(re.findall(class_pattern, code_content))
    documented_classes = len(docstrings["classes"])
    
    if total_classes > 0:
        score += 0.3 * (documented_classes / total_classes)
        
    # 함수 문서화 비율
    function_pattern = r"def\s+\w+"
    total_functions = len(re.findall(function_pattern, code_content))
    documented_functions = len(docstrings["functions"])
    
    if total_functions > 0:
        score += 0.5 * (documented_functions / total_functions)
        
    # 문서 문자열 품질 (길이 기반 간단 추정)
    avg_length = 0
    total_docs = (1 if docstrings["module"] else 0) + documented_classes + documented_functions
    
    if total_docs > 0:
        total_length = (len(docstrings["module"] or "")
                       + sum(len(doc) for doc in docstrings["classes"].values())
                       + sum(len(doc) for doc in docstrings["functions"].values()))
        avg_length = total_length / total_docs
        
        # 평균 길이 점수 (0-50자: 0.0, 50-100자: 0.1, 100자 이상: 0.2)
        if avg_length > 100:
            score += 0.2
        elif avg_length > 50:
            score += 0.1
            
    return min(1.0, score)  # 최대 1.0

def parse_docstring_structure(docstring: str) -> Dict[str, Any]:
    """문서 문자열 구조 분석 (예: 매개변수, 반환값 등)"""
    structure = {
        "description": "",
        "params": [],
        "returns": None,
        "examples": []
    }
    
    if not docstring:
        return structure
        
    # 기본 설명 추출
    parts = docstring.split("\n\n")
    if parts:
        structure["description"] = parts[0]
    
    # 매개변수 추출 (다양한 형식 지원)
    param_patterns = [
        r"@param\s+(\w+)\s+(.*)",  # @param name description
        r"Parameters:\s*\n\s*(\w+)\s*:\s*(.*)",  # Parameters: \n  name: description
        r"Args:\s*\n\s*(\w+)\s*:\s*(.*)",  # Args: \n  name: description
        r":param\s+(\w+):\s*(.*)"  # :param name: description
    ]
    
    for pattern in param_patterns:
        for match in re.finditer(pattern, docstring, re.MULTILINE):
            name = match.group(1)
            desc = match.group(2)
            structure["params"].append({"name": name, "description": desc.strip()})
    
    # 반환값 추출
    return_patterns = [
        r"@returns?\s+(.*)",
        r"Returns:\s*(.*)",
        r":returns?:\s*(.*)"
    ]
    
    for pattern in return_patterns:
        match = re.search(pattern, docstring, re.MULTILINE)
        if match:
            structure["returns"] = match.group(1).strip()
            break
    
    # 예제 추출
    example_patterns = [
        r"Examples?:\s*\n```[\s\S]*?```",
        r"@example\s*\n```[\s\S]*?```"
    ]
    
    for pattern in example_patterns:
        for match in re.finditer(pattern, docstring, re.MULTILINE):
            example = match.group(0)
            structure["examples"].append(example)
    
    return structure