#!/bin/bash
# The Stack 데이터셋 중 Python 코드만 다운로드하는 스크립트

# 기본 설정
BASE_DIR=$(pwd)
DATA_DIR="${BASE_DIR}/data/raw"
LOG_DIR="${BASE_DIR}/logs"
CONFIG_FILE="${BASE_DIR}/config/download_config.json"

# 로그 디렉터리 생성
mkdir -p "$LOG_DIR"
mkdir -p "$DATA_DIR/python"

# 날짜 스탬프
DATE_STAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="${LOG_DIR}/download_python_${DATE_STAMP}.log"

# 로그 시작
echo "=== The Stack Python 데이터셋 다운로드 시작: $(date) ===" | tee -a "$LOG_FILE"
echo "- 데이터 저장 경로: $DATA_DIR/python" | tee -a "$LOG_FILE"
echo "- 설정 파일: $CONFIG_FILE" | tee -a "$LOG_FILE"

# 디스크 여유 공간 확인
DISK_SPACE=$(df -h . | awk 'NR==2 {print $4}')
echo "- 사용 가능한 디스크 공간: $DISK_SPACE" | tee -a "$LOG_FILE"

# 파일 수 설정
FILES_PER_LANG=100000

# 설정 파일 존재 시 해당 값 사용
if [ -f "$CONFIG_FILE" ]; then
    echo "- 설정 파일 로드 중..." | tee -a "$LOG_FILE"
    # jq 명령어가 있다면 이를 사용하여 설정 파일 파싱
    if command -v jq &> /dev/null; then
        if jq -e '.language_specific.python.files_per_language' "$CONFIG_FILE" &> /dev/null; then
            FILES_PER_LANG=$(jq -r '.language_specific.python.files_per_language' "$CONFIG_FILE")
        elif jq -e '.files_per_language' "$CONFIG_FILE" &> /dev/null; then
            FILES_PER_LANG=$(jq -r '.files_per_language' "$CONFIG_FILE")
        fi
    else
        echo "  jq 명령어를 찾을 수 없어 기본 설정을 사용합니다." | tee -a "$LOG_FILE"
    fi
fi

# 다운로드 명령 실행
echo "=== Python 데이터셋 다운로드 시작 (파일 수: $FILES_PER_LANG) ===" | tee -a "$LOG_FILE"

python -m src.data.download \
    --languages "python" \
    --files-per-language "$FILES_PER_LANG" \
    --output-dir "$DATA_DIR" \
    --config "$CONFIG_FILE" \
    --streaming | tee -a "$LOG_FILE"

# 결과 확인
if [ $? -eq 0 ]; then
    echo "=== Python 데이터셋 다운로드 완료: $(date) ===" | tee -a "$LOG_FILE"
    
    # 파일 크기 확인
    if [ -d "$DATA_DIR/python" ]; then
        SIZE=$(du -sh "$DATA_DIR/python" | awk '{print $1}')
        FILES=$(find "$DATA_DIR/python" -type f | wc -l)
        echo "- 다운로드 크기: $SIZE (파일 $FILES개)" | tee -a "$LOG_FILE"
    else
        echo "- 경고: 다운로드 디렉터리를 찾을 수 없습니다." | tee -a "$LOG_FILE"
    fi
else
    echo "=== Python 데이터셋 다운로드 실패: $(date) ===" | tee -a "$LOG_FILE"
fi

# 디스크 여유 공간 (다운로드 후)
DISK_SPACE=$(df -h . | awk 'NR==2 {print $4}')
echo "- 남은 디스크 공간: $DISK_SPACE" | tee -a "$LOG_FILE"