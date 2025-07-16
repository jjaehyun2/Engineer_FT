#!/bin/bash
# The Stack 데이터셋 전처리 스크립트

# 기본 설정
BASE_DIR=$(pwd)
INPUT_DIR="${BASE_DIR}/data/raw"
OUTPUT_DIR="${BASE_DIR}/data/processed"
LOG_DIR="${BASE_DIR}/logs"

# 로그 디렉터리 생성
mkdir -p "$LOG_DIR"
mkdir -p "$OUTPUT_DIR"

# 날짜 스탬프
DATE_STAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="${LOG_DIR}/preprocess_all_${DATE_STAMP}.log"

# 로그 시작
echo "=== The Stack 데이터셋 전처리 시작: $(date) ===" | tee -a "$LOG_FILE"
echo "- 입력 경로: $INPUT_DIR" | tee -a "$LOG_FILE"
echo "- 출력 경로: $OUTPUT_DIR" | tee -a "$LOG_FILE"

# 디스크 여유 공간 확인
DISK_SPACE=$(df -h . | awk 'NR==2 {print $4}')
echo "- 사용 가능한 디스크 공간: $DISK_SPACE" | tee -a "$LOG_FILE"

# 처리할 언어 디렉터리 확인
LANGUAGES=()
for dir in "$INPUT_DIR"/*; do
    if [ -d "$dir" ]; then
        lang=$(basename "$dir")
        LANGUAGES+=("$lang")
    fi
done

echo "- 처리할 언어: ${LANGUAGES[*]}" | tee -a "$LOG_FILE"

# 각 언어별로 전처리 실행
for lang in "${LANGUAGES[@]}"; do
    echo "" | tee -a "$LOG_FILE"
    echo "=== $lang 데이터셋 전처리 시작: $(date) ===" | tee -a "$LOG_FILE"
    
    # 언어별 로그 파일
    LANG_LOG_FILE="${LOG_DIR}/preprocess_${lang}_${DATE_STAMP}.log"
    
    # 전처리 명령 실행
    python -m src.data.preprocess \
        --input-dir "$INPUT_DIR" \
        --output-dir "$OUTPUT_DIR" \
        --languages "$lang" | tee -a "$LANG_LOG_FILE" "$LOG_FILE"
        
    # 결과 확인
    if [ $? -eq 0 ]; then
        echo "=== $lang 데이터셋 전처리 완료: $(date) ===" | tee -a "$LOG_FILE"
        
        # 출력 크기 확인
        output_path="${OUTPUT_DIR}/${lang}_clean"
        if [ -d "$output_path" ]; then
            SIZE=$(du -sh "$output_path" | awk '{print $1}')
            FILES=$(find "$output_path" -type f | wc -l)
            echo "- 출력 크기: $SIZE (파일 $FILES개)" | tee -a "$LOG_FILE"
        else
            echo "- 경고: 출력 디렉터리를 찾을 수 없습니다." | tee -a "$LOG_FILE"
        fi
    else
        echo "=== $lang 데이터셋 전처리 실패: $(date) ===" | tee -a "$LOG_FILE"
    fi
done

echo "" | tee -a "$LOG_FILE"
echo "=== The Stack 데이터셋 전처리 종료: $(date) ===" | tee -a "$LOG_FILE"

# 전처리 결과 요약
echo "" | tee -a "$LOG_FILE"
echo "=== 전처리 결과 요약 ===" | tee -a "$LOG_FILE"
for lang in "${LANGUAGES[@]}"; do
    output_path="${OUTPUT_DIR}/${lang}_clean"
    if [ -d "$output_path" ]; then
        SIZE=$(du -sh "$output_path" | awk '{print $1}')
        FILES=$(find "$output_path" -type f | wc -l)
        echo "- $lang: $SIZE (파일 $FILES개)" | tee -a "$LOG_FILE"
    else
        echo "- $lang: 전처리 실패 또는 비어있음" | tee -a "$LOG_FILE"
    fi
done

# 디스크 여유 공간 (전처리 후)
DISK_SPACE=$(df -h . | awk 'NR==2 {print $4}')
echo "- 남은 디스크 공간: $DISK_SPACE" | tee -a "$LOG_FILE"