from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont

class MovieInfoWindow(QDialog):
    def __init__(self, movie_name, description, image_path, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"{movie_name} - ინფორმაცია")
        self.setFixedSize(600, 400)
        self.setStyleSheet("background-color: rgb(50, 50, 50); color: white;")
        
        layout = QHBoxLayout(self)
        
        image_label = QLabel()
        image_label.setFixedSize(250, 350)
        image_label.setScaledContents(True)
        image_label.setPixmap(QPixmap(image_path))
        
        text_layout = QVBoxLayout()
        
        title = QLabel(movie_name)
        title.setFont(QFont("", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        
        desc = QLabel(description)
        desc.setFont(QFont("", 12))
        desc.setWordWrap(True)
        desc.setStyleSheet("padding: 10px")
        
        text_layout.addWidget(title)
        text_layout.addWidget(desc)
        text_layout.addStretch()
        
        layout.addWidget(image_label)
        layout.addLayout(text_layout)