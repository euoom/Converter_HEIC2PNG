# HEIC to PNG Converter 🔄📷

## 📌 개요
이 스크립트는 현재 폴더 및 **하위 모든 폴더**에서 `.HEIC` 이미지를 찾아 **동일한 위치에 `.PNG`로 변환**하는 파이썬 프로그램입니다.

## 🚀 사용 방법
### 0. **먼저 설치가 필요한 사항**
- python
- git (없을 경우 직접 다운받아도 문제없음)

### 1️. **필요 패키지 설치**
```bash
python -m venv venv
venv\Scripts\activate  # 윈도우
source venv/Scripts/activate  # 리눅스
pip install pillow pillow-heif
```

### 2. **프로젝트 다운로드**
``` bash
git clone https://github.com/euoom/Converter_HEIC2PNG.git
```

### 3. **실행**
``` bash
python convert_heic2png.py
```
