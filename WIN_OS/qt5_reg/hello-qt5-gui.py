import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from winreg import *
Registry = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
RawKey = OpenKey(Registry, r"SOFTWARE\Microsoft\WindowsUpdate\UX\Settings")
try:
     BranchReadinessLevel=QueryValueEx(RawKey, "BranchReadinessLevel")
     print ("BranchReadinessLevel found")
     print(str(BranchReadinessLevel))
except:
     print ("warning BranchReadinessLevel missing")
try:
     DeferFeatureUpdatesPeriodInDays=QueryValueEx(RawKey, "DeferFeatureUpdatesPeriodInDays")
     print ("DeferFeatureUpdatesPeriodInDays found")
     print(str(DeferFeatureUpdatesPeriodInDays))
except:
     print ("warning DeferFeatureUpdatesPeriodInDays missing")
try:
     DeferQualityUpdatesPeriodInDays=QueryValueEx(RawKey, "DeferQualityUpdatesPeriodInDays")
     print ("DeferQualityUpdatesPeriodInDays found")
     print(str(DeferQualityUpdatesPeriodInDays))
except:
     print ("warning DeferQualityUpdatesPeriodInDays missing")
try:
     ActiveHoursStart=QueryValueEx(RawKey, "ActiveHoursStart")
     print ("ActiveHoursStart found")
     print(str(ActiveHoursStart))
except:
     print ("warning ActiveHoursStart missing")
try:
     ActiveHoursEnd=QueryValueEx(RawKey, "ActiveHoursEnd")
     print ("ActiveHoursEnd found")
     print(str(ActiveHoursEnd))
except:
     print ("warning ActiveHoursEnd missing")

def window():
   app = QApplication(sys.argv)
   widget = QWidget()

   textLabel = QLabel(widget)
   textLabel1 = QLabel(widget)
   textLabel2 = QLabel(widget)
   textLabel3 = QLabel(widget)
   textLabel4 = QLabel(widget)
   textLabel5 = QLabel(widget)
   textLabel6 = QLabel(widget)
   textLabel.setText("Check registry update details!")
   textLabel1.setText("for security update setting")
   textLabel2.setText("BranchReadinessLevel: " + str (BranchReadinessLevel))
   textLabel3.setText("DeferFeatureUpdatesPeriodInDays: " + str (DeferFeatureUpdatesPeriodInDays))
   textLabel4.setText("DeferQualityUpdatesPeriodInDays: " + str (DeferQualityUpdatesPeriodInDays))
   textLabel5.setText("ActiveHoursStart: " + str (ActiveHoursStart))
   textLabel6.setText("ActiveHoursEnd: " + str (ActiveHoursEnd))
   textLabel.move(110,45)
   textLabel1.move(110,65)
   textLabel2.move(110,85)
   textLabel3.move(110,105)
   textLabel4.move(110,125)
   textLabel5.move(110,145)
   textLabel6.move(110,165)
   widget.setGeometry(50,50,500,250)
   widget.setWindowTitle("PyQt5 Example")
   widget.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   window()
