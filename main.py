import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import QFont
from organizer_logic import Organize_files

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("File Organizer")
        self.setFixedSize(400, 150)
        
        self.path_display = QLineEdit()
        self.path_display.setPlaceholderText("Choose a folder")
        
        self.select_folder_btn = QPushButton("Select Folder")
        self.select_folder_btn.setFixedSize(90, 30)
        self.select_folder_btn.setFont(QFont("Arial", 10))
        
        self.organize_files_btn = QPushButton("Organize")
        self.organize_files_btn.setFixedSize(120, 40)
        self.organize_files_btn.setFont(QFont("Arial", 12))
        
        self.hlayout = QHBoxLayout()
        self.hlayout.addWidget(self.select_folder_btn)
        self.hlayout.addWidget(self.path_display)
        self.hlayout.setAlignment(Qt.AlignCenter)
        
        self.vlayout = QVBoxLayout()
        self.vlayout.addItem(QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.vlayout.addLayout(self.hlayout)
        self.vlayout.addItem(QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.vlayout.addWidget(self.organize_files_btn, alignment=Qt.AlignCenter)
        
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.vlayout)
        self.setCentralWidget(self.central_widget)
        
        self.select_folder_btn.clicked.connect(self.select_folder_and_organize)
        self.organize_files_btn.clicked.connect(self.validate_organization)
        
        self.folder_path = ""
        
    def select_folder_and_organize(self):
        self.folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        
        if self.folder_path:
            self.path_display.setText(self.folder_path)
            
            self.file_organizer = Organize_files(self.folder_path)
    
    def validate_organization(self):
        if self.folder_path == "" or not self.folder_path:
            QMessageBox.information(self, "Error", "No folder found.")
            return
        
        # verifies if it has attributes
        if hasattr(self, 'file_organizer'):
            organized = self.file_organizer.categorize_files() # organized is the attribute returned from the class
        
            if organized:
                QMessageBox.information(self, "Success", "Files have been organized!")
                
            else:
                QMessageBox.information(self, "Info", "All files are already organized.")
            
        else:
            QMessageBox.information(self, "Error", "Invalid file formats or file organizer not found.")

        # resets both display and the folder path
        self.path_display.clear()
        self.folder_path = ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    program = Main()
    program.show()
    sys.exit(app.exec())