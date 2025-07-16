#!/bin/bash
# 디스크 사용량 모니터링 스크립트

# 기본 설정
BASE_DIR=$(pwd)
DATA_DIR="${BASE_DIR}/data"
LOG_DIR="${BASE_DIR}/logs"

# 로그 디렉터리 생성
mkdir -p "$LOG_DIR"

# 모니터링 간격 (초)
INTERVAL=300  # 5분

# 날짜 스탬프
DATE_STAMP=$(date +"%Y%m%d")
LOG_FILE="${LOG_DIR}/disk_monitor_${DATE_STAMP}.log"

echo "=== 디스크 사용량 모니터링 시작: $(date) ===" | tee -a "$LOG_FILE"
echo "- 모니터링 간격: ${INTERVAL}초" | tee -a "$LOG_FILE"
echo "- 로그 파일: $LOG_FILE" | tee -a "$LOG_FILE"

# 초기 디스크 사용량 기록
echo "" | tee -a "$LOG_FILE"
echo "== 초기 디스크 사용량 ==" | tee -a "$LOG_FILE"
df -h | tee -a "$LOG_FILE"

echo "" | tee -a "$LOG_FILE"
echo "== 데이터 디렉터리 사용량 ==" | tee -a "$LOG_FILE"
if [ -d "$DATA_DIR" ]; then
    du -sh "$DATA_DIR"/* 2>/dev/null | tee -a "$LOG_FILE" || echo "디렉터리가 비어있습니다" | tee -a "$LOG_FILE"
else
    echo "데이터 디렉터리가 존재하지 않습니다" | tee -a "$LOG_FILE"
fi

# Ctrl+C 처리
trap "echo '모니터링 종료: $(date)' | tee -a $LOG_FILE; exit 0" INT

# 지속적 모니터링
echo "" | tee -a "$LOG_FILE"
echo "== 지속적 디스크 모니터링 시작 ==" | tee -a "$LOG_FILE"

while true; do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "" | tee -a "$LOG_FILE"
    echo "[$TIMESTAMP] 디스크 사용량:" | tee -a "$LOG_FILE"
    
    # 전체 디스크 사용량
    df -h | tee -a "$LOG_FILE"
    
    # 주요 디렉터리 사용량
    echo "" | tee -a "$LOG_FILE"
    echo "[$TIMESTAMP] 데이터 디렉터리 사용량:" | tee -a "$LOG_FILE"
    if [ -d "$DATA_DIR" ]; then
        for subdir in "$DATA_DIR"/*; do
            if [ -d "$subdir" ]; then
                SIZE=$(du -sh "$subdir" 2>/dev/null | awk '{print $1}')
                DIR=$(basename "$subdir")
                echo "- $DIR: $SIZE" | tee -a "$LOG_FILE"
                
                # 하위 디렉터리 확인
                if [ -d "$subdir" ]; then
                    for innerdir in "$subdir"/*; do
                        if [ -d "$innerdir" ]; then
                            INNER_SIZE=$(du -sh "$innerdir" 2>/dev/null | awk '{print $1}')
                            INNER_DIR=$(basename "$innerdir")
                            echo "  └─ $INNER_DIR: $INNER_SIZE" | tee -a "$LOG_FILE"
                        fi
                    done
                fi
            fi
        done
    else
        echo "데이터 디렉터리가 존재하지 않습니다" | tee -a "$LOG_FILE"
    fi
    
    # 간격 대기
    sleep $INTERVAL
done