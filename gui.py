from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from external_widgets import SnippingWidget, CanvasWidget
import sys
import cv2
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('file:///C:/GeorgiaTech/Classes/CS%206492/WebMachine/samples_gui/web_machine_demo.html')

app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()

canvas_widget = CanvasWidget()

select_img = QtWidgets.QLabel()
select_img_map = QtGui.QPixmap('stand.jpg')
select_img.setPixmap(select_img_map)
select_img.setMask(select_img_map.mask())

result = QtWidgets.QLabel('Please select component')

snipper = SnippingWidget(select_img, result)

grab_btn=QtWidgets.QPushButton('Select')
def click_handler_g():
    snipper.start()
grab_btn.clicked.connect(click_handler_g)

replace_btn=QtWidgets.QPushButton('Replace')
def click_handler_r():
    canvas_widget.canvas.save('./user_input.png')
    driver.refresh()
    result.setText('Shape rule applied!')

    select_img_map = QtGui.QPixmap('stand.jpg')
    select_img.setPixmap(select_img_map)
    select_img.setMask(select_img_map.mask())

    canvas_widget.setPixmap(select_img_map)
    canvas_widget.setMask(select_img_map.mask())
    canvas_widget.canvas.fill(Qt.GlobalColor.white)
replace_btn.clicked.connect(click_handler_r)

layout = QtWidgets.QVBoxLayout()
layout.addWidget(grab_btn)
layout.addWidget(select_img)
layout.addWidget(replace_btn)
layout.addWidget(canvas_widget)
layout.addWidget(result, alignment=Qt.AlignmentFlag.AlignCenter)


w.setLayout(layout)
w.show()

sys.exit(app.exec_())