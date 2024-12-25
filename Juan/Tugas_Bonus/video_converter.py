from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog
import cv2
import os

class Ui_Form(object):
    def __init__(self):
        self.video_path = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(459, 206)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
 
        self.label_status = QtWidgets.QLabel(parent=Form)
        self.label_status.setObjectName("label_status")
        self.gridLayout.addWidget(self.label_status, 0, 0, 1, 1)
 
        self.button_select_video = QtWidgets.QPushButton(parent=Form)
        self.button_select_video.setObjectName("button_select_video")
        self.gridLayout.addWidget(self.button_select_video, 1, 0, 1, 1)
 
        self.button_convert = QtWidgets.QPushButton(parent=Form)
        self.button_convert.setObjectName("button_convert")
        self.gridLayout.addWidget(self.button_convert, 2, 0, 1, 1)
 
        self.progress_bar = QtWidgets.QProgressBar(parent=Form)
        self.progress_bar.setProperty("value", 0)  
        self.progress_bar.setObjectName("progress_bar")
        self.gridLayout.addWidget(self.progress_bar, 3, 0, 1, 1)

        self.button_select_video.clicked.connect(self.select_video)
        self.button_convert.clicked.connect(self.start_conversion) 

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Video Converter"))
        self.label_status.setText(_translate("Form", "                                                           Pilih Video Anda"))
        self.button_select_video.setText(_translate("Form", "Pilih Video"))
        self.button_convert.setText(_translate("Form", "Mulai Konversi"))

    def select_video(self):
        file, _ = QFileDialog.getOpenFileName(None, "Pilih Video", "", "Video Files (*.mp4 *.avi *.mov);;All Files (*)")
        if file:
            self.video_path = file
            self.label_status.setText(f"Video dipilih: {os.path.basename(file)}")
            print(f"Video yang dipilih: {file}")
        else:
            self.label_status.setText("Tidak ada video yang dipilih!")
            print("Tidak ada video yang dipilih!")

    def convert_video_to_images(self, video_path):
        cap = cv2.VideoCapture(video_path)
    
        if not cap.isOpened():
            self.label_status.setText("Gagal membuka video!")
            print("Gagal membuka video!")
            return
    
        fps = cap.get(cv2.CAP_PROP_FPS)  
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_count = 0
        success, frame = cap.read()
    
        frame_interval = int(fps / 1)  
    
        self.progress_bar.setValue(0)
    
        total_images = total_frames // frame_interval  
    
        images_saved = 0
    
        while success:
            if frame_count % frame_interval == 0:
                img_name = f"frame_{frame_count}.png"
                cv2.imwrite(img_name, frame)  
                print(f"Menulis gambar: {img_name}")
            
                images_saved += 1
            
                progress = int((images_saved / total_images) * 100)
                self.progress_bar.setValue(progress)
        
            frame_count += 1
            success, frame = cap.read()

        cap.release()
        self.label_status.setText("                                                           Konversi selesai!")

    def start_conversion(self):
        if self.video_path:
            self.convert_video_to_images(self.video_path)
        else:
            self.label_status.setText("Tidak ada video yang dipilih!")
            print("Tidak ada video yang dipilih!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
