#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
코드 데이터 변환 유틸리티
"""

import os
import re
import json
import gzip
import logging
from typing import Dict, Any, List, Optional, Callable, Union

from src.utils.logging_utils import get_logger
from src.utils.io_utils import read_file, ensure_directory, write_file

logger = get_logger(__name__)

def extract_docstring_from_python(code: str) -> Dict[str, str]:
    """
    Python 코드에서 docstring 추출
    
    Args:
        code: Python 코드
        
    Returns:
        {"docstring": 추출된 docstring, "code": docstring을 제외한 코드}
    """
    import ast
    from ast import NodeVisitor
    
    class DocstringExtractor(NodeVisitor):
        def __init__(self):
            self.docstrings = []
            self.first_docstring = None
        
        def visit_Module(self, node):
            # 모듈 수준 docstring 체크
            if (node.body and isinstance(node.body[0], ast.Expr) and
                    isinstance(node.body[0].value, ast.Str)):
                self.first_docstring = node.body[0].value.s
            self.generic_visit(node)
        
        def visit_ClassDef(self, node):
            # 클래스 수준 docstring 체크
            if (node.body and isinstance(node.body[0], ast.Expr) and
                    isinstance(node.body[0].value, ast.Str)):
                self.docstrings.append(node.body[0].value.s)
            self.generic_visit(node)
        
        def visit_FunctionDef(self, node):
            # 함수 수준 docstring 체크
            if (node.body and isinstance(node.body[0], ast.Expr) and
                    isinstance(node.body[0].value, ast.Str)):
                self.docstrings.append(node.body[0].value.s)
            self.generic_visit(node)
    
    try:
        tree = ast.parse(code)
        extractor = DocstringExtractor()
        extractor.visit(tree)
        
        # 첫 번째 docstring을 메인 docstring으로 사용
        main_docstring = extractor.first_docstring or (extractor.docstrings[0] if extractor.docstrings else "")
        
        # docstring 제거
        if extractor.first_docstring:
            lines = code.split('\n')
            in_docstring = False
            docstring_lines = []
            clean_lines = []
            
            for i, line in enumerate(lines):
                # 매우 간단한 docstring 감지 (개선 필요)
                if '"""' in line or "'''" in line:
                    if not in_docstring:
                        in_docstring = True
                        docstring_lines.append(line)
                        continue
                    else:
                        in_docstring = False
                        docstring_lines.append(line)
                        continue
                
                if in_docstring:
                    docstring_lines.append(line)
                else:
                    clean_lines.append(line)
            
            clean_code = '\n'.join(clean_lines)
        else:
            clean_code = code
            
        return {
            "docstring": main_docstring.strip(),
            "code": clean_code.strip()
        }
    except Exception as e:
        logger.error(f"Python docstring 추출 오류: {e}")
        return {"docstring": "", "code": code}

def extract_comments_from_javascript(code: str) -> Dict[str, str]:
    """
    JavaScript 코드에서 주석 추출
    
    Args:
        code: JavaScript 코드
        
    Returns:
        {"comments": 추출된 주석, "code": 주석을 제외한 코드}
    """
    # 블록 주석 패턴
    block_comment_pattern = r'/\*\*?\s*([\s\S]*?)\s*\*/'
    
    # 행 주석 패턴
    line_comment_pattern = r'//\s*(.*)'
    
    # 주석 추출
    block_comments = re.findall(block_comment_pattern, code)
    
    # 처음 나오는 주석을 문서 주석으로 가정
    main_comment = block_comments[0].strip() if block_comments else ""
    
    # 코드에서 주석 제거
    clean_code = re.sub(block_comment_pattern, '', code)
    clean_code = re.sub(line_comment_pattern, '', clean_code)
    
    return {
        "comments": main_comment,
        "code": clean_code.strip()
    }

def extract_javadoc_from_java(code: str) -> Dict[str, str]:
    """
    Java 코드에서 JavaDoc 추출
    
    Args:
        code: Java 코드
        
    Returns:
        {"javadoc": 추출된 JavaDoc, "code": JavaDoc을 제외한 코드}
    """
    # JavaDoc 패턴 (/** ... */)
    javadoc_pattern = r'/\*\*\s*([\s\S]*?)\s*\*/'
    
    # 처음 나오는 JavaDoc 추출
    javadocs = re.findall(javadoc_pattern, code)
    main_javadoc = javadocs[0].strip() if javadocs else ""
    
    # JavaDoc 제거
    clean_code = re.sub(javadoc_pattern, '', code)
    
    return {
        "javadoc": main_javadoc,
        "code": clean_code.strip()
    }

def create_prompt_completion_pair(
    code_doc: Dict[str, str],
    language: str,
    prompt_template: Optional[str] = None
) -> Dict[str, str]:
    """
    코드와 문서화로부터 프롬프트-완성 쌍 생성
    
    Args:
        code_doc: 코드와 문서화를 포함하는 딕셔너리
        language: 프로그래밍 언어
        prompt_template: 프롬프트 템플릿 (없으면 기본값 사용)
        
    Returns:
        {"prompt": 생성된 프롬프트, "completion": 기대되는 완성}
    """
    # 언어별 필드 매핑
    lang_mapping = {
        "python": {"doc_field": "docstring", "code_field": "code"},
        "javascript": {"doc_field": "comments", "code_field": "code"},
        "java": {"doc_field": "javadoc", "code_field": "code"}
    }
    
    mapping = lang_mapping.get(language.lower(), {"doc_field": "docstring", "code_field": "code"})
    doc = code_doc.get(mapping["doc_field"], "")
    code = code_doc.get(mapping["code_field"], "")
    
    # 문서화가 없는 경우
    if not doc:
        return None
    
    # 기본 프롬프트 템플릿
    if not prompt_template:
        prompt_template = "주어진 {language} 코드에 대한 문서를 작성해주세요:\n\n{code}\n\n문서:"
    
    # 프롬프트 생성
    prompt = prompt_template.format(language=language, code=code)
    completion = doc
    
    return {
        "prompt": prompt,
        "completion": completion
    }

def transform_to_instruct_format(
    input_file: str,
    output_file: str,
    language: str,
    mode: str = "code_to_doc",
    max_samples: Optional[int] = None
) -> int:
    """
    코드 파일을 지시 형식으로 변환
    
    Args:
        input_file: 입력 파일 경로
        output_file: 출력 파일 경로
        language: 프로그래밍 언어
        mode: 변환 모드 ("code_to_doc" 또는 "doc_to_code")
        max_samples: 처리할 최대 샘플 수
        
    Returns:
        성공적으로 변환된 샘플 수
    """
    logger.info(f"파일 변환: {input_file} -> {output_file}")
    logger.info(f"언어: {language}, 모드: {mode}")
    
    # 입력 파일 확인
    if not os.path.exists(input_file):
        logger.error(f"입력 파일을 찾을 수 없음: {input_file}")
        return 0
    
    # 출력 디렉터리 생성
    ensure_directory(os.path.dirname(output_file))
    
    # 언어별 추출 함수 선택
    extractors = {
        "python": extract_docstring_from_python,
        "javascript": extract_comments_from_javascript,
        "java": extract_javadoc_from_java
    }
    
    extractor = extractors.get(language.lower())
    if not extractor:
        logger.error(f"지원되지 않는 언어: {language}")
        return 0
    
    # 데이터 로드
    samples = []
    if input_file.endswith('.jsonl') or input_file.endswith('.jsonl.gz'):
        # JSONL 형식
        open_func = gzip.open if input_file.endswith('.gz') else open
        with open_func(input_file, 'rt', encoding='utf-8') as f:
            for line in f:
                samples.append(json.loads(line))
    else:
        # 단일 코드 파일로 가정
        code = read_file(input_file)
        samples = [{"content": code}]
    
    # 최대 샘플 수 제한
    if max_samples and max_samples < len(samples):
        samples = samples[:max_samples]
    
    # 변환 결과
    transformed = []
    success_count = 0
    
    # 변환 처리
    for i, sample in enumerate(samples):
        try:
            if "content" not in sample:
                logger.warning(f"항목 {i}에 'content' 필드가 없습니다. 건너뜁니다.")
                continue
            
            code = sample["content"]
            
            # 코드와 문서 추출
            code_doc = extractor(code)
            
            # 변환 모드에 따라 프롬프트-완성 쌍 생성
            if mode == "code_to_doc":
                # 코드에서 문서화 생성
                result = create_prompt_completion_pair(code_doc, language)
            elif mode == "doc_to_code":
                # 문서화에서 코드 생성 (방향 반대)
                doc_field = {"python": "docstring", "javascript": "comments", "java": "javadoc"}.get(language.lower(), "docstring")
                code_field = "code"
                
                # doc_to_code를 위한 프롬프트 템플릿
                template = f"다음 {language} 문서를 기반으로 코드를 작성해주세요:\n\n{{code}}\n\n코드:"
                
                # 코드와 문서 교환하여 생성
                reversed_doc_code = {doc_field: code_doc[code_field], code_field: code_doc[doc_field]}
                result = create_prompt_completion_pair(reversed_doc_code, language, template)
            else:
                logger.error(f"지원되지 않는 변환 모드: {mode}")
                continue
            
            if result:
                # 메타데이터 추가
                result["language"] = language
                result["mode"] = mode
                transformed.append(result)
                success_count += 1
            
            # 진행 상황 로깅
            if (i + 1) % 100 == 0:
                            logger.info(f"진행: {i+1}/{len(samples)} ({success_count} 성공)")
        except Exception as e:
            logger.error(f"항목 {i} 처리 중 오류 발생: {str(e)}")
    
    # 결과 저장
    open_func = gzip.open if output_file.endswith('.gz') else open
    with open_func(output_file, 'wt', encoding='utf-8') as f:
        for item in transformed:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')
    
    logger.info(f"변환 완료: {success_count}/{len(samples)} 항목 성공")
    logger.info(f"결과 저장: {output_file}")
    
    return success_count

def extract_functions_from_file(
    file_path: str,
    language: str
) -> List[Dict[str, str]]:
    """
    파일에서 함수 추출
    
    Args:
        file_path: 코드 파일 경로
        language: 프로그래밍 언어
        
    Returns:
        함수 정보 목록
    """
    code = read_file(file_path)
    
    if language.lower() == "python":
        return extract_python_functions(code)
    elif language.lower() == "javascript":
        return extract_javascript_functions(code)
    elif language.lower() == "java":
        return extract_java_methods(code)
    else:
        logger.error(f"지원되지 않는 언어: {language}")
        return []

def extract_python_functions(code: str) -> List[Dict[str, str]]:
    """Python 코드에서 함수 추출"""
    import ast
    
    functions = []
    
    try:
        tree = ast.parse(code)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # 함수 소스 코드 추출
                func_lines = code.splitlines()[node.lineno-1:node.end_lineno]
                func_code = '\n'.join(func_lines)
                
                # docstring 확인
                docstring = ast.get_docstring(node)
                
                functions.append({
                    "name": node.name,
                    "code": func_code,
                    "docstring": docstring or "",
                    "start_line": node.lineno,
                    "end_line": node.end_lineno
                })
    except Exception as e:
        logger.error(f"Python 함수 추출 오류: {str(e)}")
    
    return functions

def extract_javascript_functions(code: str) -> List[Dict[str, str]]:
    """JavaScript 코드에서 함수 추출"""
    # 간단한 정규식 기반 추출 (완벽하지 않음, 필요시 파서 라이브러리 사용 권장)
    function_pattern = r'(\/\*\*[\s\S]*?\*\/)?\s*(function\s+(\w+)\s*\([^)]*\)\s*{[\s\S]*?})'
    method_pattern = r'(\/\*\*[\s\S]*?\*\/)?\s*((\w+)\s*:\s*function\s*\([^)]*\)\s*{[\s\S]*?})'
    arrow_pattern = r'(\/\*\*[\s\S]*?\*\/)?\s*(const\s+(\w+)\s*=\s*\([^)]*\)\s*=>\s*{[\s\S]*?})'
    
    functions = []
    
    # 일반 함수
    for comment, func, name in re.findall(function_pattern, code):
        functions.append({
            "name": name,
            "code": func,
            "comments": comment,
            "type": "function"
        })
    
    # 메서드
    for comment, func, name in re.findall(method_pattern, code):
        functions.append({
            "name": name,
            "code": func,
            "comments": comment,
            "type": "method"
        })
    
    # 화살표 함수
    for comment, func, name in re.findall(arrow_pattern, code):
        functions.append({
            "name": name,
            "code": func,
            "comments": comment,
            "type": "arrow_function"
        })
    
    return functions

def extract_java_methods(code: str) -> List[Dict[str, str]]:
    """Java 코드에서 메서드 추출"""
    # JavaDoc과 메서드 추출을 위한 정규식
    method_pattern = r'(\/\*\*[\s\S]*?\*\/)?[\s\n]*((?:public|protected|private|static|\s)+[\w\<\>\[\]]+\s+(\w+)\s*\([^\)]*\)(?:\s*throws\s+[\w\s,]+)?)\s*{[\s\S]*?}'
    
    functions = []
    
    for javadoc, signature, name in re.findall(method_pattern, code):
        # 메서드 본문 추출
        start_idx = code.find(signature)
        if start_idx >= 0:
            open_braces = 0
            body_start = code.find('{', start_idx)
            
            # 괄호 짝 맞추기로 메서드 본문 끝 찾기
            i = body_start
            while i < len(code):
                if code[i] == '{':
                    open_braces += 1
                elif code[i] == '}':
                    open_braces -= 1
                    if open_braces == 0:
                        break
                i += 1
            
            if i < len(code):
                method_code = code[start_idx:i+1]
                
                functions.append({
                    "name": name,
                    "code": method_code,
                    "javadoc": javadoc,
                    "signature": signature
                })
    
    return functions

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="코드 데이터 변환 유틸리티")
    
    parser.add_argument("--input-file", type=str, required=True, help="입력 파일 경로")
    parser.add_argument("--output-file", type=str, required=True, help="출력 파일 경로")
    parser.add_argument("--language", type=str, required=True, help="프로그래밍 언어")
    parser.add_argument("--mode", type=str, default="code_to_doc", 
                        choices=["code_to_doc", "doc_to_code"], help="변환 모드")
    parser.add_argument("--max-samples", type=int, help="처리할 최대 샘플 수")
    parser.add_argument("--log-level", type=str, default="INFO", help="로그 레벨")
    
    args = parser.parse_args()
    
    # 로깅 설정
    logging.basicConfig(
        level=getattr(logging, args.log_level.upper(), None),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # 변환 실행
    transform_to_instruct_format(
        input_file=args.input_file,
        output_file=args.output_file,
        language=args.language,
        mode=args.mode,
        max_samples=args.max_samples
    )

if __name__ == "__main__":
    main()