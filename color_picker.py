import pyqtgraph as pg
from PySide6 import QtWidgets


def change(btn):
    print("change", btn.color())


def done(btn):
    print("done", btn.color())


app = QtWidgets.QApplication([])
win = QtWidgets.QMainWindow()
btn1 = pg.ColorButton()
win.setCentralWidget(btn1)
win.show()
win.setWindowTitle('pyqtgraph example: ColorButton')

btn1.sigColorChanging.connect(change)
btn1.sigColorChanged.connect(done)

app.exec()
