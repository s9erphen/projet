import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from main import Ui_MainWindow
from main import QStackedWidget



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        self.ui.actionAjouter_tudiant.triggered.connect(self.show_ajouter_etudiant)

    def show_ajouter_etudiant(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        
    def open_new_window(self):
        # Create a new window
        new_window = QtWidgets.QMainWindow()

        # Set the central widget of the new window
        new_window.setCentralWidget(QtWidgets.QLabel("New Window"))

        # Show the new window
        new_window.show()


if __name__ == "__main__":
    import sys 
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())




