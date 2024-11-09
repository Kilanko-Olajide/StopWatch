import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                             QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import QTimer, QTime, Qt



class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("00:00:00.0", self)
        self.time = QTime(0, 0, 0, 0)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.restart_button = QPushButton("Restart", self)
        self.timer = QTimer(self)



        self.initUI()
    def initUI(self):
        self.setWindowTitle("Stopwatch")
        self.setGeometry(650, 350, 600, 200)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        
        self.setLayout(vbox)
        self.label.setAlignment(Qt.AlignCenter)


        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.restart_button)

        vbox.addLayout(hbox)

        self.setStyleSheet("""
                        QLabel, QPushButton{
                           padding: 15px;
                           font-weight: bold;

                           }
                        QPushButton{font-size: 50px;
                           }
                        QLabel{font-size: 150px;
                           background-color: hsl(150, 70%, 85%);
                          }
                           """)
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.restart_button.clicked.connect(self.restart)
        self.timer.timeout.connect(self.correct_display)

    def start(self):
        self.timer.start(10)
    def stop(self):
        self.timer.stop()
    def restart(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.label.setText(self.format_time(self.time))
    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"
    def correct_display(self):
        self.time = self.time.addMSecs(10)
        self.label.setText(self.format_time(self.time))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = Stopwatch()
    clock.show()
    sys.exit(app.exec_())
