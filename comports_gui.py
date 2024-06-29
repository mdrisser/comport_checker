import sys
import serial.tools.list_ports

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QFont


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Active COM Ports')
        self.setGeometry(100, 100, 320, 210)

        ports = []

        for port in serial.tools.list_ports.comports():
            ports.append(port.name)
            
        if(len(ports) == 0):
            label = QLabel("No COM ports currently in use.")
        else:
            portStr = ""
            
            for port in ports:
                portStr += f"{port.device}: {port.description}\n"
            
            label = QLabel(portStr)

        # place the widget on the window
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

        # show the window
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())