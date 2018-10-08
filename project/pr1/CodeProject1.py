import sys
#------------import opencv------------
import cv2
import  numpy as np
# car_cascade = cv2.CascadeClassifier('cars.xml')
#-----------import for GUI-------------
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog,QMessageBox
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi


class GUI(QMainWindow):
    soframe=0
    clickStart =0;
    videoname=0
    # khởi tạo cái giá trị ban đầu
    def __init__(self):
        super(GUI, self).__init__()
        loadUi('GUI_pr1.ui', self)
        self.image = None
        # self.lbVideoGoc.setText("Press the Start button to start with the camera!")
        self.nguonVideo.clicked.connect(self.loadClick)
        self.btStart.clicked.connect(self.loadVideo)
        self.btFinish.clicked.connect(self.finishConnect)
        self.car_cascade = cv2.CascadeClassifier('cars.xml')


    @pyqtSlot()
    #hàm xử lí các sự kiện
    def loadClick(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Choose File', 'C:\\', "AllVideo (*)")
        if fname:
            self.tenNguon(fname) # set path tới videe
            self.tenVideo(str(fname)) # lấy tên video.nếu dùng camera trà về là camera
            self.videoname=fname
            self.lbVideoGoc.setText('Press the "Start" button to start!')
            # if self.clickStart > 0:
            #     print(self.clickStart)
            #     self.loadVideo(fname)
            # else:
            #     self.clickedStart()

    #loadVideo
    def loadVideo(self):
        self.soframe = 0
        fname =self.videoname
        self.tenVideo(str(fname))
        # if fname =='':
        #     pass
        # else:
        self.capture = cv2.VideoCapture(fname)
        # self.capture=set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        # self.capture=set(cv2.CAP_PROP_FRAME_WIDTH,640)
        # ----
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(15)
    #chia video thành cá frame
    def update_frame(self):
        res,self.image=self.capture.read()
        self.soframe+=1
        self.image=cv2.flip(self.image,1)
        self.displayImage(self.image, 1)
        self.updateSoFrame()
        detectObj = self.detectObject(self.image)
        self.displayImage(detectObj,2)

    #đếm số frame
    def updateSoFrame(self):
        self.soFrame.setText(str(self.soframe))

    #hàm nhận dạng
    def detectObject(self,img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # detect cars in the video
        cars= self.car_cascade.detectMultiScale(gray,1.9,3)
        for (x,y,w,h) in cars:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

        return img

    #hieetn thị video: video gốc ở lbVideoGoc,Video sau nhận dạng ở lbVideoSau
    def displayImage(self,image2,window):
        qformat = QImage.Format_Indexed8
        if len(image2.shape) == 3:
            if (image2.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(image2,image2.shape[1],image2.shape[0],image2.strides[0],qformat)
        img = img.rgbSwapped()
        if window ==1:
            self.lbVideoGoc.setPixmap(QtGui.QPixmap.fromImage(img))
        if window ==2:
            self.lbVideoSau.setPixmap(QtGui.QPixmap.fromImage(img))
        # self.lbVideoGoc.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.lbVideoGoc.setScaledContents(True)
        self.lbVideoSau.setScaledContents(True)
    #ten path dan den video
    def tenNguon(self,fname):
        self.lineEditLinkVd.setText(fname)

    #ten video
    def tenVideo(self,fname):
        if fname=='0':
            self.nameVd.setText('Camera')
        if fname.rfind('/') > -1:
            self.nameVd.setText(fname[fname.rfind('/') + 1:len(fname)])

    #thoat
    def finishConnect(self):
        exit(app.exec_())


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = GUI()
    window.setWindowTitle('Project1')
    window.show()
    sys.exit(app.exec_())