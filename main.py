from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from edit_color_func import editColorSpace
from edit_color_func import advancedEditColor
import cv2 as cv
import numpy as np
#--------------------------------------------------------------------------------

# program description :

# Streaming using webcam in real life and make track bar to edit color space (HSV) using OpenCV library.

# note: this program is a GUI version of edit_color_func.py

#--------------------------------------------------------------------------------

# Copyright: WALID HASSAN

#--------------------------------------------------------------------------------
# function description :

# main function to run the program

# create the GUI of the program using PyQt5 library
#--------------------------------------------------------------------------------
# parameters : None
def main():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle('Edit Color Space')
    window.setGeometry(100, 100, 800, 600)
    window.setMinimumSize(800, 600)
    window.setMaximumSize(800, 600)
    window.setStyleSheet('background-color: #ffffff;')
    # create a label in top center position of window
    titleLabel = QLabel(window)
    titleLabel.setText('welcome to the Willyx program')
    titleLabel.setAlignment(Qt.AlignCenter)
    titleLabel.setStyleSheet('font-size: 30px; font-weight: bold; color: #000000;')
    titleLabel.setGeometry(0, 40, 800, 50)
    # note label
    noteLabel = QLabel(window)
    noteLabel.setText('Note: This program will use your webcam to edit color space ')
    noteLabel.setAlignment(Qt.AlignCenter)
    noteLabel.setStyleSheet('font-size: 20px; font-weight: bold; color: #000000;')
    noteLabel.setGeometry(0, 100, 800, 50)
    # note2 label
    note2Label = QLabel(window)
    note2Label.setText('and to close the webcam, press ESC button')
    note2Label.setAlignment(Qt.AlignCenter)
    note2Label.setStyleSheet('font-size: 20px; font-weight: bold; color: #000000;')
    note2Label.setGeometry(0, 140, 800, 50)
    # create AND button
    andBtn = QPushButton(window)
    andBtn.setText('Edit Color Space (AND)')
    andBtn.setStyleSheet('background-color: #50C878; color: #ffffff; font-size: 20px; font-weight: bold;')
    andBtn.setGeometry(200, 200, 400, 50)
    # create OR button
    orBtn = QPushButton(window)
    orBtn.setText('Edit Color Space (OR)')
    orBtn.setStyleSheet('background-color: #000000; color: #ffffff; font-size: 20px; font-weight: bold;')
    orBtn.setGeometry(200, 300, 400, 50)
    # create advanced button
    advancedBtn = QPushButton(window)
    advancedBtn.setText('Advanced (AND)')
    advancedBtn.setStyleSheet('background-color: #325ea8; color: #ffffff; font-size: 20px; font-weight: bold;')
    advancedBtn.setGeometry(200, 400, 400, 50)
    # create exit button
    exitBtn = QPushButton(window)
    exitBtn.setText('Exit')
    exitBtn.setStyleSheet('background-color: #C70039; color: #ffffff; font-size: 20px; font-weight: bold;')
    exitBtn.setGeometry(200, 500, 400, 50)
    # connect buttons to functions
    andBtn.clicked.connect(lambda:editColorSpace('and'))
    orBtn.clicked.connect(lambda:editColorSpace('or'))
    exitBtn.clicked.connect(lambda: exit_btn(app))
    advancedBtn.clicked.connect(advancedEditColor)
    # show window
    window.show()
    app.exec_()
# --------------------------------------------------------------------------------
def exit_btn(app):
    # pop up a message box to confirm exit
    msg = QMessageBox()
    msg.setWindowTitle('Exit')
    msg.setText('Are you sure you want to exit?')
    msg.setIcon(QMessageBox.Question)
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msg.setDefaultButton(QMessageBox.No)
    # get the result of message box
    result = msg.exec_()
    if result == QMessageBox.Yes:
        app.quit()
    else:
        pass
# --------------------------------------------------------------------------------
# run main function  
if __name__ == '__main__':
    main()


