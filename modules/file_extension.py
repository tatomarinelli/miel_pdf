class Fext:
    def __init__ (self):
        self.extensions = [
                    ".pdf",
                    ".doc",
                    ".docx",
                    ".xls",
                    ".xlsx",
                    ".ppt",
                    ".pptx",
                    ".txt",

                    #Images
                    ".jpg",
                    ".jpeg",
                    ".png",

                    ".nb" #Wolfram
                    ]

    def GetFileExt(self):
        return self.extensions
