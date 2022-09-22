class File:
    def __init__(self):
        self.file  = []
    def addFile(self,x):
        self.file.append(x)
    def removeFile(self,x):
        self.file.remove(x)
    def tailleFile(self):
        return len(self.file)
