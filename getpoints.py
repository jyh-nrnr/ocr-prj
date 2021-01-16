import cv2 
import pytesseract
import numpy as np

class GetPoints(object):
    oldx = oldy = -1 # 좌표 기본값 설
    Px = [0, 0, 0, 0]
    Py = [0, 0, 0, 0]
    count_num = 0 
    
    def __init__(self, file_name):
        self.file_name = "file_name"

    def savePoints(self, _src):
        def get_point(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN: # 왼쪽이 눌러지면 실행
                self.oldx, self.oldy = x, y # 마우스가 눌렀을 때 좌표 저장, 띄워진 영상에서의 좌측 상단 기준
                cv2.circle(_src, (x,y), 2, (0,0,255), -1)
                self.count_num += 1

                if self.count_num   == 1: self.Px[0], self.Py[0] = x, y 
                elif self.count_num == 2: self.Px[1], self.Py[1] = x, y
                elif self.count_num == 3: self.Px[2], self.Py[2] = x, y
                elif self.count_num == 4: self.Px[3], self.Py[3] = x, y

        cv2.imshow('image', _src)
        cv2.setMouseCallback('image', get_point, _src)
        
        while(1):
            cv2.imshow('image', _src)
            k = cv2.waitKey(1) & 0xFF 
            if k == 27: 
                break

        min_x, max_x = min(self.Px), max(self.Px)
        min_y, max_y = min(self.Py), max(self.Py)

        f = open(self.file_name+"txt", 'w')
        f.write(str(min_x)+"\n"); f.write(str(max_x)+"\n"); f.write(str(min_y)+"\n"); f.write(str(max_y)+"\n")
        f.close()

    def loadPoints(self):
        f = open(self.file_name+"txt", 'r')
        lines = f.readlines()
        return int(lines[0]), int(lines[1]), int(lines[2]), int(lines[3])