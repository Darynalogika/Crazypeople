from PyQt5.QtCore import*
from PyQt5.QtWidgets import*



app=QApplication([])
window=QWidget()

window.resize(400,200)

def winner():
    victory_win=QMessageBox()
    victory_win.setText("Ти переміг")
    victory_win.exec_()

def loser():
    loser_win=QMessageBox()
    loser_win.setText("Ти програв")
    loser_win.exec_()
window.setWindowTitle("Title")

label=QLabel("Хто робить з одної людини дві?")

rbtn_1=QRadioButton("маньяк")
rbtn_2=QRadioButton("психіатр")
rbtn_3=QRadioButton("дзеркало")
rbtn_4=QRadioButton("книга")

row1=QHBoxLayout()
row2=QHBoxLayout()

col=QVBoxLayout()

row1.addWidget(rbtn_1,alignment=Qt.AlignCenter)
row1.addWidget(rbtn_2,alignment=Qt.AlignCenter)
row2.addWidget(rbtn_3,alignment=Qt.AlignCenter)
row2.addWidget(rbtn_4,alignment=Qt.AlignCenter)

col.addWidget(label,alignment=Qt.AlignCenter)
col.addLayout(row1)
col.addLayout(row2)

window.setLayout(col)

rbtn_1.clicked.connect(loser)
rbtn_2.clicked.connect(loser)
rbtn_3.clicked.connect(winner)
rbtn_4.clicked.connect(loser)

window.show()
app.exec_()

