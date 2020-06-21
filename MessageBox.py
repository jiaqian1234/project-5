from PyQt5.QtWidgets import QMessageBox
def showMessageBox( message, no_critical = False):
    msg = QMessageBox()
    if no_critical:
        msg.setIcon(QMessageBox.Warning)
       #msg.setTitle('Warning')
    else:
        msg.setIcon(QMessageBox.Critical)
       #msg.setTitle('Error')
    msg.setText(message)
    msg.exec_()