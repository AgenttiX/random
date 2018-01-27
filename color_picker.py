import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

app = QtGui.QApplication([])
win = QtGui.QMainWindow()
btn = pg.ColorButton()
win.setCentralWidget(btn)
win.show()
win.setWindowTitle('pyqtgraph example: ColorButton')

def change(btn):
    print("change", btn.color())
def done(btn):
    print("done", btn.color())

btn.sigColorChanging.connect(change)
btn.sigColorChanged.connect(done)

app.exec()

