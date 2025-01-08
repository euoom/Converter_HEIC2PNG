import os
from pillow_heif import open_heif
from PIL import Image

# 현재 실행 중인 파이썬 파일의 경로
base_dir = os.path.dirname(os.path.abspath(__file__))

def convert_heic_to_png(heic_path):
    """HEIC 파일을 PNG로 변환하여 동일 경로에 저장"""
    try:
        heif_image = open_heif(heic_path)
        image = Image.frombytes(heif_image.mode, heif_image.size, heif_image.data)

        # 파일 확장자 변경 (예: image.HEIC → image.PNG)
        png_path = os.path.splitext(heic_path)[0] + ".png"
        image.save(png_path, "PNG")
        print(f"변환 완료: {heic_path} → {png_path}")

    except Exception as e:
        print(f"변환 실패: {heic_path} | 오류: {e}")

# 현재 폴더부터 하위 폴더까지 .HEIC 파일 검색 및 변환
for root, _, files in os.walk(base_dir):
    for file in files:
        if file.lower().endswith(".heic"):
            heic_file_path = os.path.join(root, file)
            convert_heic_to_png(heic_file_path)

print("🔹 모든 HEIC → PNG 변환 완료!")
