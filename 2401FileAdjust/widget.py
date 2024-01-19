from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox
import pandas as pd 

'''
Error:
1.
Q: No module name 'pandas'
A: pip install pandas
'''


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CSV data arrangement")

        button_data = QPushButton("Get data")
        button_data.clicked.connect(self.button_clicked_get_data)

        # Set up the layouts
        layout = QVBoxLayout()
        layout.addWidget(button_data)
        self.setLayout(layout)

    #Get data
    def button_clicked_get_data(self):
        sourceData = pd.read_csv('./Source.csv', sep=',')
        print(sourceData)