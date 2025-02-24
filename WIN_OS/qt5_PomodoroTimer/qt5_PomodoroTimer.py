import sys
import logging
#from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, Qt, QTime

# Define constants for Pomodoro work and break durations (in minutes)
POMODORO_DURATION = (25 * 60) 
SHORT_BREAK_DURATION = (5 * 60)

#logging control
logging.basicConfig(level=logging.INFO)  #disable debug
#logging.basicConfig(level=logging.DEBUG)  #enable debug
#test data (in seconds)
#_DURATION = (7 * 1) 
#SHORT_BREAK_DURATION = (2 * 1)

class PomodoroTimer(QWidget):
    def __init__(self):
        #super().__init__() or
        # Explicitly initialize the QWidget base class
        QWidget.__init__(self)

        self.init_ui()
        self.reset_timer()

    def init_ui(self):
        self.setWindowTitle("Pomodoro Timer: WORK!")
        self.setFixedSize(500, 150)

        # Create layout
        self.layout = QVBoxLayout(self)

        # Timer label
        self.timer_label = QLabel()
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.font = self.timer_label.font()
        self.font.setPointSize(32)
        self.timer_label.setFont(self.font)
        self.layout.addWidget(self.timer_label)

        # Button layout
        self.button_layout = QHBoxLayout()
        self.layout.addLayout(self.button_layout)

        # Start/Stop button
        self.start_stop_button = QPushButton("Start")
        self.start_stop_button.clicked.connect(self.start_stop_timer)
        self.button_layout.addWidget(self.start_stop_button)

        # Reset button
        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_timer)
        self.button_layout.addWidget(self.reset_button)

        # Timer object
        #exit()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

    def reset_timer(self):
        self.current_mode = POMODORO_DURATION
        self.current_duration = POMODORO_DURATION
        self.update_timer_label()
        self.timer.stop()
        self.start_stop_button.setText("Start")

    def start_stop_timer(self):
        if self.timer.isActive():
            self.timer.stop()
            self.start_stop_button.setText("Start")
        else:
            self.timer.start(1000)  # Update timer every second
            self.start_stop_button.setText("Stop")

    def update_timer(self):
        self.current_duration -= 1
        logging.debug (f"current_duration {self.current_duration}")
        self.update_timer_label()
        if self.current_duration <= 0:
            print (f"finished update : self.current_duration {self.current_duration}")
            #self.play_sound()  # Replace with your sound-playing function for Windows
            self.timer.stop()
            self.start_stop_button.setText("Start")
            self.handle_timer_end()

    def update_timer_label(self):
        minutes, seconds = divmod(self.current_duration, 60)
        self.timer_label.setText(f"{minutes:02d}:{seconds:02d}")

    def handle_timer_end(self):
        print (f"self.current_duration:{self.current_duration}")

        #check current MODE
        if self.current_mode == POMODORO_DURATION:
            self.current_mode = SHORT_BREAK_DURATION
            self.current_duration = SHORT_BREAK_DURATION
            self.setWindowTitle("Pomodoro Timer : REST!")
        else:
            # break finished, reset timer
            self.setWindowTitle("Pomodoro Timer : WORK!")
            self.reset_timer()

        self.update_timer_label()

if __name__ == "__main__":
    #print (f"args: {sys.argv}")
    app = QApplication(sys.argv) #pass args, needed by default for library
    #app.setApplicationName("qt5_PomodoroTimer")  # Set the desired application name
    window = PomodoroTimer()
    window.show()
    sys.exit(app.exec_())