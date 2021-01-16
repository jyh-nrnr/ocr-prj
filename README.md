# Tesseract와 Opencv를 활용해 번호판에서 번호 위치를 명시하고, 글자를 읽어들이기

## 배경
- 엉엉 Tesseract가 무료로 OCR 써보기엔 좋은데 글자 위치 return이 안돼 ㅠㅠ
- 그래서 opencv로 글자 읽을 위치 지정해주면 그 위치에서 글씨 읽을 수 있게 만듦
- 혹시 위치가 여러 개일 수도 있고 하니 파일명 입력해서 위치 저장하고, 다시 불러올 수 있게 만듦

## 사용 환경
- Mac OS Big Sur 버전 11.1
- Python 3.8.5
- 

## 패키지 리스트

## 환경설정
1. 가상환경 생성 후 실행
    ~~~
    python3 -m venv ocr-prj 
    ~~~
    source ocr-prj/bin/activate 
    ~~~
2. 필요 패키지 설치 (위 패키지 리스트 참조)
    ~~~
    pip3 install opencv-python 
    ~~~
3. Tesseract 설치
    ~~~
    brew install tesseract
    ~~~
    pip3 install pytesseract
    ~~~

