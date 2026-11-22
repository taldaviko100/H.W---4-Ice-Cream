from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QPixmap

class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("About")
        self.setGeometry(150, 150, 460, 560)
        self.setStyleSheet("background-color: lightblue")

        self.name_label = QLabel("Tal Daviko", self)
        self.name_label.setGeometry(40, 25, 380, 45)
        self.name_label.setStyleSheet("font-size: 30px;" "font-weight: bold;" "color: #1E3A5F;")

        self.email_label = QLabel("Taldaviko100@gmail.com", self)
        self.email_label.setGeometry(40, 80, 380, 30)
        self.email_label.setStyleSheet("font-size: 17px;" "color: #475569;")

        image = QPixmap("picture.jpg").scaled(300, 300)

        self.my_picture = QLabel(self)
        self.my_picture.setGeometry(80, 135, 300, 300)
        self.my_picture.setPixmap(image)

        self.linkedin_label = QLabel('<a href="https://www.linkedin.com/in/tal-daviko-65309a38b/">My LinkedIn</a>',self)
        self.linkedin_label.setGeometry(80, 465, 300, 40)
        self.linkedin_label.setOpenExternalLinks(True)
        self.linkedin_label.setStyleSheet("font-size: 20px;")

        self.github_label = QLabel('<a href="https://github.com/taldaviko100/H.W---4-Ice-Cream">Project on GitHub</a>',self)
        self.github_label.setGeometry(80, 510, 340, 35)
        self.github_label.setOpenExternalLinks(True)
        self.github_label.setStyleSheet("font-size: 20px;")


if __name__ == '__main__':
    app = QApplication()
    window = AboutWindow()
    window.show()
    app.exec()