import os
from PyQt5 import QtWidgets, QtGui
from pydub import AudioSegment

class AudioConverter(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Audio Converter')
        self.setGeometry(100, 100, 300, 150)

        self.file_path = None

        self.file_label = QtWidgets.QLabel(self)
        self.file_label.setGeometry(20, 20, 260, 20)
        self.file_label.setText('Select an audio file to convert:')

        self.browse_button = QtWidgets.QPushButton(self)
        self.browse_button.setGeometry(20, 50, 100, 30)
        self.browse_button.setText('Browse...')
        self.browse_button.clicked.connect(self.browse_file)

        self.convert_button = QtWidgets.QPushButton(self)
        self.convert_button.setGeometry(140, 50, 100, 30)
        self.convert_button.setText('Convert')
        self.convert_button.clicked.connect(self.convert_file)

    def browse_file(self):
        self.file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Select File')
        self.file_label.setText('Selected file: ' + os.path.basename(self.file_path))

    def convert_file(self):
        if not self.file_path:
            return
        file_name, file_ext = os.path.splitext(self.file_path)
        output_format, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Select Output File', file_name, filter='Audio files (*.mp3 *.wav *.aiff *.flac *.ogg)')
        if not output_format:
            return
        sound = AudioSegment.from_file(self.file_path, format=file_ext[1:])
        sound.export(output_format, format=output_format.split('.')[-1])

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    converter = AudioConverter()
    converter.show()
    app.exec_()
