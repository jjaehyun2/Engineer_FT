#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
코드 분석 및 기능 추출 유틸리티
"""

import ast
import re
import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

def extract_functions(code_content: str, language: str) -> List[Dict[str, Any]]:
    """
    코드에서 함수 추출
    
    Args:
        code_content: 코드 내용
        language: 프로그래밍 언어
        
    Returns:
        함수 정보 목록
    """
    functions = []
    
    if language == "python":
        try:
            tree = ast.parse(code_content)
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    function_info = {
                        "name": node.name,
                        "start_line": node.lineno,
                        "end_line": node.end_lineno,
                        "args": [arg.arg for arg in node.args.args],
                        "docstring": ast.get_docstring(node) or "",
                        "code": _get_function_code(code_content, node)
                    }
                    functions.append(function_info)
        except SyntaxError:
            logger.warning("Syntax error while parsing Python code")
        except Exception as e:
            logger.warning(f"Error extracting Python functions: {e}")
            
    elif language == "javascript":
        # JavaScript 함수 추출 로직
        # 정규식 기반 간단 구현 (완전하지 않음)
        function_patterns = [
            # 일반 함수 선언
            r"function\s+(\w+)\s*\(([^)]*)\)\s*\{",
            # 화살표 함수
            r"(const|let|var)\s+(\w+)\s*=\s*(\([^)]*\)|[^=]+)?\s*=>\s*\{",
            # 메서드 선언
            r"(\w+)\s*\(([^)]*)\)\s*\{"
        ]
        
        for pattern in function_patterns:
            for match in re.finditer(pattern, code_content):
                # 간략 정보만 추출 (실제로는 더 정확한 파싱 필요)
                functions.append({
                    "name": match.group(1) if "=>" not in pattern else match.group(2),
                    "start_position": match.start(),
                    "raw_match": match.group(0)
                })
                
    elif language == "java":
        # Java 함수 추출 로직
        # 정규식 기반 간단 구현 (더 정교한 파서 필요)
        method_pattern = r"(?:public|private|protected)?\s+(?:static\s+)?(?:\w+(?:<[^>]+>)?)\s+(\w+)\s*\(([^)]*)\)\s*(?:throws\s+\w+(?:\s*,\s*\w+)*)?\s*\{"
        
        for match in re.finditer(method_pattern, code_content):
            functions.append({
                "name": match.group(1),
                "parameters": match.group(2),
                "start_position": match.start()
            })
    
    return functions

def analyze_code_structure(code_content: str, language: str) -> Dict[str, Any]:
    """
    코드 구조 분석
    
    Args:
        code_content: 코드 내용
        language: 프로그래밍 언어
        
    Returns:
        구조 정보 딕셔너리
    """
    structure = {
        "line_count": code_content.count("\n") + 1,
        "char_count": len(code_content),
        "imports": [],
        "classes": [],
        "complexity": _estimate_complexity(code_content, language),
        "domain": _classify_domain(code_content, language)
    }
    
    if language == "python":
        try:
            tree = ast.parse(code_content)
            
            # 임포트 추출
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for name in node.names:
                        structure["imports"].append(name.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        for name in node.names:
                            structure["imports"].append(f"{node.module}.{name.name}")
                
                # 클래스 추출
                elif isinstance(node, ast.ClassDef):
                    class_info = {
                        "name": node.name,
                        "methods": [method.name for method in node.body 
                                   if isinstance(method, ast.FunctionDef)],
                        "docstring": ast.get_docstring(node) or ""
                    }
                    structure["classes"].append(class_info)
                    
        except Exception as e:
            logger.warning(f"Error analyzing Python code structure: {e}")
    
    # JavaScript/Java 코드 구조 분석은 여기에 추가
    
    return structure

def _get_function_code(code_content: str, node: ast.FunctionDef) -> str:
    """함수 노드에서 원본 코드 추출"""
    lines = code_content.split("\n")
    if hasattr(node, "end_lineno"):
        return "\n".join(lines[node.lineno-1:node.end_lineno])
    else:
        # end_lineno가 없는 경우, 다른 방법으로 추출 필요
        return "\n".join(lines[node.lineno-1:])

def _estimate_complexity(code_content: str, language: str) -> int:
    """코드 복잡도 추정 (간단히)"""
    if language == "python":
        try:
            tree = ast.parse(code_content)
            visitor = ComplexityVisitor()
            visitor.visit(tree)
            return visitor.complexity
        except:
            # 파싱 실패 시 간단 추정
            return code_content.count("if") + code_content.count("for") + code_content.count("while")
    else:
        # 다른 언어는 간단한 휴리스틱 사용
        loops = code_content.count("for") + code_content.count("while")
        conditions = code_content.count("if") + code_content.count("switch")
        return loops + conditions

def _classify_domain(code_content: str, language: str) -> str:
    """코드 도메인 분류"""
    # 도메인별 키워드
    domain_keywords = {
        "algorithms": ["sort", "search", "algorithm", "tree", "graph", "dynamic programming"],
        "web": ["http", "html", "css", "api", "rest", "url", "request", "response"],
        "data": ["dataframe", "pandas", "numpy", "csv", "json", "data", "analysis"],
        "system": ["file", "process", "thread", "socket", "network", "system"],
        "ml": ["model", "train", "predict", "accuracy", "neural", "regression"]
    }
    
    # 각 도메인별 점수 계산
    domain_scores = {domain: 0 for domain in domain_keywords}
    lower_content = code_content.lower()
    
    for domain, keywords in domain_keywords.items():
        for keyword in keywords:
            count = lower_content.count(keyword)
            domain_scores[domain] += count
    
    # 최고 점수 도메인 반환
    max_domain = max(domain_scores.items(), key=lambda x: x[1])
    return max_domain[0] if max_domain[1] > 0 else "general"

# 복잡도 분석용 AST 방문자
class ComplexityVisitor(ast.NodeVisitor):
    def __init__(self):
        self.complexity = 1  # 기본 복잡도 1
        
    def visit_If(self, node):
        self.complexity += 1
        self.generic_visit(node)
        
    def visit_For(self, node):
        self.complexity += 1
        self.generic_visit(node)
        
    def visit_While(self, node):
        self.complexity += 1
        self.generic_visit(node)
        
    def visit_Try(self, node):
        self.complexity += 1
        self.generic_visit(node)