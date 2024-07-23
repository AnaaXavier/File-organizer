import os

class Organize_files:
    def __init__(self, path):
        self.folder_path = path # gets the string with the path retrieved in the GUI
        self.directory_contents = os.listdir(self.folder_path) # returns a list of the files/folders of a directory
        
        self.folders_and_extensions = {
            "images": [".png", ".jpg"],
            "audios": [".mp3"],
            "pdfs": [".pdf"],
            "excel": [".xlsx"],
            "texts": [".txt"],
            "word files": [".docx"]
        }
        
    def categorize_files(self):
        # Initialize as false to track any non-organized folder
        self.organized = False
        
        for folder_file in self.directory_contents:
            self.file_name, self.file_extension = os.path.splitext(folder_file)
            
            # creates the full path, combining the folder and the file path
            self.file_path = os.path.join(self.folder_path, folder_file)
            
            
            for folder in self.folders_and_extensions:
                if self.file_extension in self.folders_and_extensions[folder]:
                    self.target_folder = os.path.join(self.folder_path, folder)
                    
                    if not os.path.exists(self.target_folder):
                        os.makedirs(self.target_folder)
                    
                    self.target_path = os.path.join(self.target_folder, folder_file)
                    
                    # moves to the folders using the corrected full path
                    os.rename(self.file_path, self.target_path)
                    
                    # after being organized, it'll be true and be returned
                    self.organized = True
                    
        return self.organized
