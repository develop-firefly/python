# Import Pandas package
import pandas as pd


# Class definitions should use CamelCase convention based on pep-8 guidelines
class CustomPandas:
    # Initialize the class with the filename as only argument
    # The initialization method will identify the file extension and use appropriate pandas function to create dataframe
    # If the sheet name is not provided the first worksheet will be loaded to dataframe
    def __init__(self, _my_file_name, _sheet_name=0):
        self.my_filename = _my_file_name
        # If the file extension is xlsx, then read_excel function will be used
        # Following line identifies the extension of the input file name
        if self.my_filename.split('.')[-1] == 'xlsx':
            # Following line reads the multi sheet excel file
            self._file = pd.ExcelFile(_my_file_name)
            # If the exel file has only 1 worksheet, that will be loaded in to dataframe
            # Else, a user defined worksheet (must be in the workbook), will be loaded
            self.df = (pd.read_excel(self.my_filename, skiprows=0, keep_default_na=False) if self._file.sheet_names == 1
                       else pd.read_excel(self.my_filename, skiprows=0, keep_default_na=False, sheet_name=_sheet_name))
            # Following line creates the dataframe
            self.my_df = pd.DataFrame(self.df)
            # Following line provides the column / header names
            self.my_df_col_names = self.my_df.columns.values
            # Following line provides the number of rows in the dataframe
            self.my_df_row_count = self.my_df.shape[0]
            # Following line provide the number of columns in the dataframe
            self.my_df_col_count = self.my_df.shape[1]
            # Following line provides row and column counts of file as a tuple
            self.my_df_shape = self.my_df.shape
            # Following line provides a dictionary of col_idx and col_names
            self.my_df_col_idx_name = dict([(self.my_df.columns.get_loc(_), _) for _ in self.my_df_col_names])
            # Following line provides a dictionary of  col_names and col_idx
            self.my_df_col_name_idx = dict([(_, self.my_df.columns.get_loc(_)) for _ in self.my_df_col_names])

        # If the file extension is csv, then read_csv function will be used
        elif self.my_filename.split('.')[-1] == 'csv':
            self.df = pd.read_csv(self.my_filename, skiprows=0, keep_default_na=False)
            # Following line creates the dataframe
            self.my_df = pd.DataFrame(self.df)
            # Following line provides the column / header names
            self.my_df_col_names = self.my_df.columns.values
            # Following line provides the number of rows in the dataframe
            self.my_df_row_count = self.my_df.shape[0]
            # Following line provide the number of columns in the dataframe
            self.my_df_col_count = self.my_df.shape[1]
            # Following line provides row and column counts of file as a tuple
            self.my_df_shape = self.my_df.shape
            # Following line provides a dictionary of col_idx and col_names
            self.my_df_col_idx_name = dict([(self.my_df.columns.get_loc(_), _) for _ in self.my_df_col_names])
            # Following line provides a dictionary of  col_names and col_idx
            self.my_df_col_name_idx = dict([(_, self.my_df.columns.get_loc(_)) for _ in self.my_df_col_names])

        # Additionally, there are different file extensions with corresponding pandas functions
        # which can be used to extend this method
