import sys
import cv2
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog,QMessageBox
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi


class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        loadUi('GUI_pr1.ui', self)
        self.image = None
        self.nguonVideo.clicked.connect(self.loadClick)

    @pyqtSlot()
    def loadClick(self):
        print('da click')
        # self.loadImage('demo.jpg')
        # options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        # fnames, _ =QFileDialog.getOpenFileNames(self,'Open File','C:\\',"Image Open (*.jpg);; PNG(*.png);;JPEG (*.jpeg)",options=options)
        fname, _ = QFileDialog.getOpenFileName(self, 'Choose File', 'C:\\', "AllVideo (*)")
        if fname:
            self.loadImage(fname)
            # print(fname)
            # ten nguon
            self.loadNguon(fname)
            # tenVideo
            self.tenVideo(str(fname))
        # print(s)

    def loadImage(self, fname):
        # self.image = cv2.imread(fname,1)
        self.image2 = cv2.imread(fname,1)
        print('da loat')
        self.displayImage(fname)

    def displayImage(self, fname):
        qformat = QImage.Format_Indexed8
        if len(self.image2.shape) == 3:
            if (self.image2.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(self.image2, self.image2.shape[1], self.image2.shape[0], self.image2.strides[0], qformat)
        img = img.rgbSwapped()
        self.lbVideoGoc.setPixmap(QtGui.QPixmap.fromImage(img))
        #self.lbVideoGoc.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.lbVideoGoc.setScaledContents(True)
        print('da hien thi')

    def loadNguon(self,fname):
        self.lineEditLinkVd.setText(fname)

    def tenVideo(self, fname):
        if fname.rfind('/') > -1:
            self.nameVd.setText(fname[fname.rfind('/') + 1:len(fname)])
        else:
            QMessageBox.show("chua chon")

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = GUI()
    window.setWindowTitle('Project1')
    window.show()
    sys.exit(app.exec_())
