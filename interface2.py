from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog , QTextEdit
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("Interface2.ui", self)

		# Define our widgets
		self.button = self.findChild(QPushButton, "open_image")
		self.label = self.findChild(QLabel, "label_image")
		self.label1 = self.findChild(QLabel, "name_label")
		self.textedit = self.findChild(QTextEdit, "name_field")
		self.button1 = self.findChild(QPushButton, "ok_button")
        



		# Click The Dropdown Box
		self.button1.clicked.connect(self.clicker1)
		self.button.clicked.connect(self.clicker)
						
		# Show The App
		self.show()
	
	def clicker1(self):
		self.label1.setText(f'Hello There {self.textedit.toPlainText()}')
		self.textedit.setPlainText("")

	def clicker(self):
		fname = QFileDialog.getOpenFileName(self, "Open File", "c:\\gui\\images", "All Files (*);;PNG Files (*.png);;Jpg Files (*.jpg)")

		# Open The Image
		if fname:
			self.pixmap = QPixmap(fname[0])
			# Add Pic to label
			self.label.setPixmap(self.pixmap)

    

# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()