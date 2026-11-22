from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.temperatures = []
        self.revenues = []
        self.selected_file = ""

        self.setWindowTitle("Ice Cream Sales")
        self.resize(1000, 700)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.main_layout = QVBoxLayout(central_widget)

        self.title_label = QLabel("Ice Cream Sales")
        self.title_label.setObjectName("title")
        self.main_layout.addWidget(self.title_label)

        self.load_button = QPushButton("Load ice cream file")
        self.load_button.clicked.connect(self.load_file)
        self.main_layout.addWidget(self.load_button)

        self.file_label = QLabel("No file selected")
        self.main_layout.addWidget(self.file_label)

        self.figure = Figure(layout="constrained")
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.axes = self.figure.add_subplot(111)

        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.main_layout.addWidget(self.toolbar)
        self.main_layout.addWidget(self.canvas)

        self.update_graph()

    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select ice cream data", "", "CSV files (*.csv)")
        if file_name:
            self.selected_file = file_name
            self.file_label.setText(file_name)

    def update_graph(self):
        self.axes.clear()

        self.axes.plot([0, 1, 2], [0, 1, 4])

        self.axes.set_title("Temporary Graph")
        self.axes.set_xlabel("X")
        self.axes.set_ylabel("Y")
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication()

    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()
    app.exec()