import cv2 
import pytesseract
import numpy as np
import getpoints

## 포인트 뽑아서 저장하는 법
# 1. 파일을 읽는다, 똑같은 파일을 복사해낸다
src = cv2.imread("sample1.jpeg")
dst = src.copy() 

# 2. 관심 영역을 도출해냄. GetPoints() 안에 파일명을 입력한다
points = getpoints.GetPoints("lincence")

# 3. savePoints()에 관심 영역을 도출한 이미지를 입력하고 코드를 실행한다. 실행하면 이미지가 뜨고, 관심영역의 네 꼭지점을 차례로 클릭한다. 네개 다 뽑아내고 나면 esc를 누른다. 누르고나면 자동으로 네 포인트가 저장된다
points.savePoints(dst)

## 뽑아진 포인트 꺼내오는 법
# 1. 저장된 네 포인트를 불러온다 
load_points = getpoints.GetPoints("lincence") # -> 위에 있던 points를 써도 됨. 파일만 불러오는 기능도 있다는걸 보여주려고 일부러 새로 판거임
min_x, max_x, min_y, max_y = load_points.loadPoints()

# 2. 포인트를 가지고 원본 이미지에서 관심 영역만 잘라낸다
roi = src[min_y : max_y, min_x : max_x]
roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

# 3. 잘라진 관심 영역 확인
cv2.imshow('image2', roi)
cv2.waitKey(0)

# 4. Tesseract로 읽어들인다
print("Test result : "+pytesseract.image_to_string(roi, lang = 'kor'))
