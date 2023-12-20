import sys

from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QFormLayout,QMessageBox
from PyQt5.QtWidgets import QPushButton, QRadioButton, QHBoxLayout, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QPalette, QColor, QFont, QPixmap
from PyQt5.QtCore import Qt
from control.compress_control import Control_Compress

# Appel class Control_Compress
conpress = Control_Compress()
class Compress(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("TP6__KONPRES IMAJ & VIDEYO")
        self.setMinimumSize(600, 600)
        self.setMaximumSize(600, 700)
        self.img_button_executed = False
        self.test = False
        self.form()

    # creer un QHboxLayout
    def form(self):
        # QFormLayout 2 parties
        self.form = QFormLayout()
        # Ajouter des composants (Widget) ds le QFormLayout

        # Définir la taille de la police (font size)
        self.font = QFont()
        self.font.setPointSize(12)

        # Text
        self.label_text_head = QLabel("CHWAZI FICHYE OU VLE KOMPRESE A")
        self.set_lineedit_styles(self.label_text_head)
        self.form.addRow(self.label_text_head)

        # Bar
        self.label_bar = QLabel("_______________" * 8)
        self.set_lineedit_styles(self.label_bar)
        self.form.addRow(self.label_bar)

        # Ajouter un QVbox
        self.vb = QHBoxLayout()

        self.buton_img = QRadioButton("Imaj (.jpg, .png, .jpeg, .gif) ")
        self.buton_video = QRadioButton("Videyo (.mp4)")
        self.buton_img.clicked.connect(self.buton_checked)
        self.buton_video.clicked.connect(self.buton_checked)

        self.vb.addWidget(self.buton_img)
        self.vb.addWidget(self.buton_video)

        self.label_type = QLabel("TIP FICHYE      ")
        self.set_lineedit_styles(self.label_type)
        self.form.addRow(self.label_type, self.vb)

        # create button
        self.button = QPushButton("Chwazi fichye ou an")
        self.button.setEnabled(False)
        self.set_qpushbutton_styles(self.button)
        self.form.addRow(QLabel(""), self.button)

        self.take_file()
        self.image()
        self.setLayout(self.form)

    def buton_checked(self):

        if self.buton_img.isChecked():
            self.button_img()
            self.enableButton()
            self.button.setText("Chwazi fichye imaj ou an")
        elif self.buton_video.isChecked():
            self.button_video()
            self.enableButton()
            self.button.setText("Chwazi fichye videyo ou an")

    def enableButton(self):
        self.button.setEnabled(True)

    def desableButton(self):
        self.button.setEnabled(False)

    def button_img(self):
        self.button.clicked.connect(self.fileImg)

    def button_video(self):
        self.button.clicked.connect(self.fileVideo)

    def set_lineedit_styles(self, lineedit):
        # Définissez la couleur de fond
        lineedit.setStyleSheet("background-color: white;")
        # Définissez la couleur du texte
        lineedit.setStyleSheet("color: #4169E1;")

    def set_lineedit_styles2(self, lineedit):
        # Définissez la couleur de fond
        lineedit.setStyleSheet("background-color: white;")
        # Définissez la couleur du texte
        lineedit.setStyleSheet("color: red;")

    def fileImg(self):
        try:
            self.desableButton()
            self.buton_img.setCheckable(False)
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            self.fname_img, _ = QFileDialog.getOpenFileName(self, 'Ouvri Fichye', "",
                                                            "Fichye Imaj (*.jpg *.jpeg *.png *.gif)",
                                                            options=options)
            self.button.clicked.disconnect()
            if self.fname_img:
                self.label_link_.setText(self.fname_img)
                self.extension = self.fname_img[-3:]
                self.button_c.setEnabled(True)
                self.buton_img.setCheckable(True)
            else:
                print("L'opération a été annulée.")
                self.buton_img.setCheckable(True)
        except Exception as e:
            print(f"Une erreur s'est produite : {str(e)}")
        return self.fname_img

    def fileVideo(self):
        try:
            self.desableButton()
            self.buton_video.setCheckable(False)
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            self.fname_video, _ = QFileDialog.getOpenFileName(self, 'Ouvri Fichye', "", "Fichye Videyo (*.mp4 )",
                                                              options=options)
            self.button.clicked.disconnect()
            if self.fname_video:
                self.label_link_.setText(self.fname_video)
                self.extension = self.fname_video[-3:]
                self.button_c.setEnabled(True)
                self.buton_video.setCheckable(True)
            else :
                print("L'opération a été annulée.")
                self.buton_video.setCheckable(True)
        except Exception as e:
            print(f"Une erreur s'est produite : {str(e)}")

    def take_file(self):
        self.hboxlayout = QHBoxLayout()
        # Link
        self.label_link = QLabel("")
        self.label_link.setFont(self.font)
        self.set_lineedit_styles(self.label_link)
        self.hboxlayout.addWidget(self.label_link)

        # link__
        self.label_link_ = QLabel("-")
        self.set_lineedit_styles2(self.label_link_)
        self.hboxlayout.addWidget(self.label_link_)

        # button_compress
        self.button_c = QPushButton("Konprese")
        # ========== Action ===================
        self.button_c.clicked.connect(self.conpress_f)
        # -====================================
        self.button_c.setEnabled(False)
        self.hboxlayout.addWidget(self.button_c)
        self.button_c.setStyleSheet(
            '''
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FF831E, stop:1 #FF831E);
                border: 1px solid #FF831E;
                color: white;
                border-radius: 5px;
                padding: 5px;
                cursor : pointer;
            }

            QPushButton:hover {
                cursor : pointer;
                color: #FF831E;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FFFFFF, stop:1 #FFFFFF);
            }
            ''')

        self.form.addRow(self.hboxlayout)

    def image(self):
        self.vbox = QVBoxLayout()
        # img
        img = QLabel()
        img.setPixmap(QPixmap("compress.png"))
        self.vbox.addWidget(img)
        self.form.addRow(self.vbox)

    def set_qpushbutton_styles(self, button):
        # Utilisez le style CSS pour définir le fond avec un dégradé
        self.button.setStyleSheet(
            '''
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #6495ED, stop:1 #4169E1);
                border: 1px solid #1E90FF;
                color: white;
                border-radius: 5px;
                padding: 5px;
            }

            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #A234ED, stop:1 #2491ED);
            }
            ''')

    def compress_fichier(self, input_file):
        conpress.compress_file(input_file)

    def conpress_f(self):
        self.file = ""
        if self.extension == "mp4":
            self.compress_fichier(self.fname_video)
            self.file = self.fname_video
        else:
            self.compress_fichier(self.fname_img)
            self.file = self.fname_img
        self.showDialog()


    def showDialog(self):
        self.button_c.setEnabled(False)
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText(f"Fichye {self.file} Konprese avek sikse!")
        self.msg.setWindowTitle("Compress Succesfull")
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.show()
        self.label_link_.setText("-")

# ====================================================================
app = QApplication([])
layout = Compress()
layout.show()
sys.exit(app.exec_())
