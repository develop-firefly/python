def get_file_extension(self, _filename):
    '''
    Method to get the file extension
    Input: Filename
    Output: File extension
    '''
    # Using the split method of class <str>
    # split the filename using '.' and capturing the last element of the return type class <list>
    self.file_ext = _filename.split('.')[-1]
    return self.file_ext
