# Import Pandas package
import pandas as pd


# Class definitions should use CamelCase convention based on pep-8 guidelines
class CustomPandas:
    # Initialize the class with the filename as only argument
    # The initialization method will identify the file extension and use appropriate pandas function to create dataframe
    # If the sheet name is not provided the first worksheet will be loaded to dataframe
    def __init__(self, _my_file_name: str, _sheet_name=0):
        self.my_filename = _my_file_name
        # If the file extension is xlsx, then read_excel function will be used
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


    def add_col_at_end(self, _col_name: str):
        '''
        Method to add a new column at the end of the dataframe
        Input Argument is a Column name of user choice
        '''
        # The following statement checks if the user provided column name already exists in the dataframe or not
        # The new column will only be added if it does not exist already
        if _col_name not in self.my_df.columns:
            # shape returns a tuple of (row count, column count)
            return self.my_df.insert(self.my_df.shape[-1], _col_name, '', True)
        # Else the new column name will not be added to the dataframe
        else:
            print(f'Column :- "{_col_name}" is already present in the Dataframe, skipping addition...', end='\n')


    def add_col_by_idx(self, position: int, _col_name: str):
        '''
        Method to add a new column at user defined position in the dataframe
        '''
        # The following statement checks if the user provided column name already exists in the dataframe or not
        # The new column will only be added if it does not exist already
        if _col_name not in self.my_df.columns:
            return self.my_df.insert(position, _col_name, '', True)
        # Else the new column name will not be added to the dataframe
        else:
            print(f'Column :- "{_col_name}" is already present in the Dataframe, skipping addition...', end='\n')


    def add_cols_at_end(self, _col_names: list):
        '''
        Method to add multiple columns at the end of the dataframe
        Input Argument is a list of Column names of user choice
        '''
        # following line will add the new columns, only if they do not exist already
        # The list comprehension provides the string of column names
        # The columns are added without any value hence ' = '' '
        self.my_df[[str(_) for _ in _col_names if _ not in self.my_df.columns]] = ''
        return self.my_df


    def copy_paste_cols_data(self, _src_col_name: str, _tgt_col_name: str):
        ''' 
        Method to copy the contents from one column to another column of dataframe
        Arguments to this method are source column name and target column name
        '''
        # NOTE: - If target col does not exist in the dataframe, it will be created at run time
        try:
            self.my_df[_tgt_col_name] = self.my_df[_src_col_name]
        except KeyError:
            print(f' Source column :- "{_src_col_name}"  not found in worksheet')


    def create_df_from_excel_specific_ws(self, _ws_name: str):
        ''' 
        Method to create dataframe from specific sheet in excel
        Argument for this method is: - worksheet name for which dataframe needs to be created
        '''
        # read the excel file provided with the sheet_name parameter
        # keep_default_na = False, this stops null cells with being filed with N/A
        self.df = pd.read_excel(self.my_filename, skiprows=0, keep_default_na=False, sheet_name=_ws_name)
        # create the dataframe from the file and the worksheet
        self.my_df = pd.DataFrame(self.df)
        # return Dataframe
        return self.my_df


    def create_df_from_dataset(self, _dataset):
        ''' 
        Method to create a dataframe from a dataset
        Argument to this method is: - Dataset
        '''
        # create a dataframe using the user provided dataset
        self.my_df = pd.DataFrame(_dataset)
        # return Dataframe
        return self.my_df


    def create_df_from_filtered_data_single_in_condition(self, _column_name: str, _condition):
        '''
        Method to create dataframe with based on one condition at column level
        Arguments to this method are: - Column name where condition is to be applied, and the condition itself
        '''
        # create a new filtered dataset based on the condition applied on the column
        _filtered_data_set = (self.my_df.loc[self.my_df[_column_name] == _condition])
        # return Dataframe
        return pd.DataFrame(_filtered_data_set)


    def create_df_from_filtered_data_single_not_in_condition(self, _column_name: str, _condition):
        '''
        Method to create dataframe with based on one condition at column level
        Arguments to this method are: - Column name where condition is to be applied, and the condition itself
        '''
        # create a new filtered dataset based on the condition applied on the column
        _filtered_data_set = (self.my_df.loc[self.my_df[_column_name] != _condition])
        # return Dataframe
        return pd.DataFrame(_filtered_data_set)


    def create_df_from_filtered_data_multiple_and_conditions(self, _col_names: str, _conditions):
        ''' 
        Method to create dataframe with based on multiple and conditions
        argument: _col_names should preferably be a list
        argument: _conditions should preferably be a list
        It has to be a 1:1 mapping of _col_name and condition and is sequence sensitive
        Do not convert is to a static method
        '''
        try:
            if len(_col_names) == len(_conditions):
                _filter_con = []
                for _idx in range(len(_col_names)):
                    _filter_con.append('(self.my_df[\'' + _col_names[_idx] + '\'] == \'' + _conditions[_idx] + '\')')
                delta = '(self.my_df.loc[' + ' & '.join(_ for _ in _filter_con) + '])'
                _filtered_data_set = eval(delta)
                return pd.DataFrame(_filtered_data_set)
        except:
            print("Unexpected-Condition-In-Method")

    # Method to create dataframe with based on multiple or conditions
    # argument: _col_names should preferably be a list
    # argument: _conditions should preferably be a list
    # It has to be a 1:1 mapping of _col_name and condition and is sequence sensitive
    # Do not convert is to a static method
    def create_df_from_filtered_data_multiple_or_conditions(self, _col_names, _conditions):
        try:
            if len(_col_names) == len(_conditions):
                _filter_con = []
                for _idx in range(len(_col_names)):
                    _filter_con.append('(self.my_df[\'' + _col_names[_idx] + '\'] == \'' + _conditions[_idx] + '\')')
                delta = '(self.my_df.loc[' + ' | '.join(_ for _ in _filter_con) + '])'
                _filtered_data_set = eval(delta)
                return pd.DataFrame(_filtered_data_set)
        except:
            print("Unexpected-Condition-In-Method")

    # Method to remove a column from the dataframe
    # Note: This method is build using a try: except block to deal with spelling mistakes in column name
    def drop_col_by_name(self, _col_name):
        try:
            self.my_df.drop(_col_name, axis=1, inplace=True)
            # print(f'Column Name "{_col_name}" removed successfully from the dataframe')
        except KeyError:
            print(f'Error:- Column Name "{_col_name}" is not present in the dataframe')

    # Method to remove a column using its existing position
    # Note: This method is build using a try: except block to deal with index out of bounds exception
    def drop_col_by_index(self, _col_idx):
        try:
            self.my_df.drop(self.my_df.columns[_col_idx], axis=1, inplace=True)
        except IndexError:
            print(
                f'ERROR: - Index value {_col_idx} is out of bounds, Current Index length is {self.my_df.shape[-1]}')

    # Method to drop the last columns in the dataframe
    # Note: This method assumes that there's at least 1 column in the dataframe
    def drop_last_col(self):
        if len(self.my_df.columns.values) > 0:
            self.my_df.drop(self.my_df.columns[-1], axis=1, inplace=True)
        return 'dataframe is empty'

    # Method to sort data in a column at row level (basically each cell of a column)
    # It has four arguments
    # Column Name:- Where Data Needs to be sorted
    # _delim:- The current delimiter of the dataset in the cell
    # _sort_type:- Can be 'asc' or 'desc'
    # _str_join_param:- User provided _delim to join the strings
    # Important Note:- For this method to provide results, the column name in question must have data in it
    def df_sort_row_level_same_col(self, _col_name, _delim, _sort_type, _str_join_param):
        # The for loop will run for the number of rows in the dataframe
        for item in range(0, self.my_df.shape[0]):
            if _sort_type == 'asc':
                # loc allows accessing columns by name
                # iloc allows accessing columns by their index
                # LHS:- Following line accesses the particular cell
                # item is row index and _col_name is column index
                # syntax for loc[row_label, column_label]
                # syntax for iloc[row_position, column_position]
                self.my_df.loc[item, _col_name] = _str_join_param.join(
                    sorted(self.my_df.loc[item, _col_name].split(_delim), reverse=False))
            elif _sort_type == 'desc':
                self.my_df.loc[item, _col_name] = _str_join_param.join(
                    sorted(self.my_df.loc[item, _col_name].split(_delim), reverse=True))
        return self.my_df

    # Method to sort data in a column at row level (basically each cell of a column)
    # It has five arguments
    # source column name:- The columns which has the unsorted data
    # target column name:- The column where sorted data will be written
    # _delim:- The current delimiter of the dataset in the cell
    # _sort_type:- Can be 'asc' or 'desc'
    # _str_join_param:- User provided _delim to join the strings
    # Important Note:- This method can take care of both sorting and writing the data
    #                   and avoids the need of copying the data to target column before sorting
    def df_sort_row_level_diff_cols(self, _src_col_name, _tgt_col_name, _delim, _sort_type,
                                    _str_join_param):
        '''
        Method to sort data in a column at row level (basically each cell of a column)
        It has five arguments
        source column name:- The columns which has the unsorted data
        target column name:- The column where sorted data will be written
        _delim:- The current delimiter of the dataset in the cell
        _sort_type:- Can be 'asc' or 'desc
        _str_join_param:- User provided _delim to join the strings
        Important Note:- This method can take care of both sorting and writing the data and avoids the need of copying the data to target column before sorting
        '''
        for item in range(0, self.my_df[_src_col_name].shape[0]):
            if _sort_type == 'asc':
                # loc allows accessing columns by name
                # iloc allows accessing columns by their index
                # LHS:- Following line accesses the particular cell
                # item is row index and _col_name is column index
                # syntax for loc[row_label, column_label]
                # syntax for iloc[row_position, column_position]
                self.my_df.loc[item, _tgt_col_name] = _str_join_param.join(
                    sorted(self.my_df.loc[item, _src_col_name].split(_delim), reverse=False))
            elif _sort_type == 'desc':
                self.my_df.loc[item, _tgt_col_name] = _str_join_param.join(
                    sorted(self.my_df.loc[item, _src_col_name].split(_delim), reverse=True))
        return self.my_df

    # Method to standardize delimiter for scenarios where the dataset needs curation
    # If the dataset has different delimiters
    def df_standardize_delim(self, _col_name, _delim):
        '''
        Method to standardize delimiter for scenarios where the dataset needs curation
        If the dataset has different delimiters
        Arguments to this method are: - Column name and the delimiter which needs to be standardized'''
        to_replace = [", ", ",", "'", "; ", " ; ", " ", "\\", ";;", "-", "/", ",;"]
        for item in to_replace:
            # Assign the formatted value to the column
            self.my_df[_col_name] = self.my_df[_col_name].str.replace(item, _delim, regex=True)
        return self.my_df[_col_name]

    # Method to see df sample - Top 10 rows
    # No Arguments for this method
    def df_sampling_top_10_rows(self):
        '''
        Method to see df sample - Top 10 rows
        No Arguments for this method
        '''
        return self.my_df.head(10)

    # Method to see df sample - Bottom 10 rows
    # No Arguments for this method
    def df_sampling_bottom_10_rows(self):
        '''
        Method to see df sample - Bottom 10 rows
        No Arguments for this method
        '''
        return self.my_df.tail(10)

    # Method to get the column index based on column name
    # Argument to this method is: - Column name
    def get_col_idx_by_name(self, _col_name):
        ''' 
        Method to get the column index based on column name
        Argument to this method is: - Column name
        '''
        # return type is integer
        # get_loc will get the index of the column
        return self.my_df.columns.get_loc(_col_name)

    # Method to get the unique values from a given column index position
    # Argument to this method is: - Column Index
    def get_col_unique_values_by_idx(self, _col_idx):
        '''
        Method to get the unique values from a given column
        Argument to this method is: - Column Index
        '''
        # Return type is dependent on column values
        return self.my_df[self.my_df_col_idx_name[_col_idx]].unique()

    # Method to get the unique values from a given column
    # Argument to this method is: - Column name
    def get_col_unique_values_by_name(self, _col_name):
        ''' 
        Method to get the unique values from a given column
        Argument to this method is: - Column name'''
        # Return type is dependent on column values
        return self.my_df[_col_name].unique()

    # Method to get the values from a given column index position
    # Return type is dependent on column values
    def get_col_values_by_idx(self, _col_idx):
        '''
        Method to get the values from a given column
        Argument to this method is: - Column index position
        '''
        return self.my_df[self.my_df_col_idx_name[_col_idx]]


    def get_col_values_by_name_m1(self, _col_name):
        '''
        Method to get the values from a given column
        Argument to this method is: - Column name
        '''
        # Return type is dependent on column values
        return self.my_df[_col_name]


    def get_col_values_by_name_m2(self, _col_name):
        '''
        Method to get the values from a given column
        Argument to this method is: - Column name
        '''
        # Return type is dependent on column values
        return self.my_df.get(_col_name)


    def get_row_val_based_on_search_param_in_col(self, _col_name, _search_val):
        '''
        Method to get row values based on a search param in a given column name
        Arguments to this method are: - Column name to be searched and search value
        '''
        _col_idx = self.get_col_idx_by_name(_col_name)
        # Return the entire row, if searched value was found in the given column
        return [_ for _ in self.my_df.itertuples() if _[_col_idx+1] == _search_val]


    def get_row_idx_based_on_search_param_in_col(self, _col_name, _search_val):
        '''
        Method to get row index based on a search param in a given column name
        Arguments to this method are: - Column name to be searched and search value
        '''
        _col_idx = self.get_col_idx_by_name(_col_name)
        # Nested list comprehension returns the pandas index from _val[0]
        return [_val[0] for _val in [_ for _ in self.my_df.itertuples() if _[_col_idx+1] == _search_val]]


    def get_specific_col_val_based_on_search_match(self, _search_col_name, _search_val, _see_val_col_name):
        '''
        Method to get values of  specific columns if search value matched in another column
        Arguments to this method are: - Column Name to the searched,  Value to be searched, Values to be seen
        '''
        # get the column indexes
        _search_col_idx = self.get_col_idx_by_name(_search_col_name)
        _see_val_col_idx = self.get_col_idx_by_name(_see_val_col_name)
        return [_val[_see_val_col_idx+1] for _val in [_ for _ in self.my_df.itertuples() if _[_search_col_idx + 1] == _search_val]]


    def get_specific_row_val_based_on_cell_range(self,_row_start, _row_end, _start_col_name, _end_col_name):
        '''
        Method to get values from specific rows based on a cell range (inclusive of ending row and column)
        Arguments to this method are: - starting row index, ending row index,
        Starting column name and Ending column name
        '''
        # Get the index based on the starting column name
        _start_col_idx = self.get_col_idx_by_name(_start_col_name)
        # Get the index based on the ending column name
        _end_col_idx = self.get_col_idx_by_name(_end_col_name)
        # Ending row index must be greater than the starting row index
        if _row_end > _row_start:
            # loc allows accessing columns by name
            # iloc allows accessing columns by their index
            # syntax for loc[row_label, column_label]
            # syntax for iloc[row_idx_start:row_idx_end, col_idx_start:col_idx_end]
            return self.my_df.iloc[_row_start:_row_end+1, _start_col_idx:_end_col_idx+1]


    def get_specific_row_val_based_on_row_range(self, _row_start, _row_end):
        '''
        Method to get values from specific rows based on a row range (inclusive of ending row)
        Arguments to this method are: - starting row index and ending row index
        NOTE: - All column values will be fetched by this method
        '''
        # Ending row index must be greater than the starting row index
        if _row_end > _row_start:
            # loc allows accessing columns by name
            # iloc allows accessing columns by their index
            # syntax for loc[row_label, column_label]
            # syntax for iloc[row_idx_start:row_idx_end, col_idx_start:col_idx_end]
            # If column indexes are not provided, then all columns will be selected by default
            return self.my_df.iloc[_row_start:_row_end+1]


    def get_specific_row_col_val_based_on_row_range(self, _row_start, _row_end, _col_names_list):
        '''
        Method to get values from specific rows based on a row range for selected columns (inclusive of ending row)
        Arguments to this method are: - starting row index, ending row index and list with column names
        Only selected columns will be printed based on the column names provided
        '''
        # The columns name(s) provided should be in a list, other iterable methods will not work
        if isinstance(_col_names_list, list):
            # using list comprehension, get the index of the columns
            _col_idx_list = [self.get_col_idx_by_name(_) for _ in _col_names_list]
            # Ending row index must be greater than the starting row index
            if _row_end > _row_start:
                # loc allows accessing columns by name
                # iloc allows accessing columns by their index
                # syntax for loc[row_label, column_label]
                # syntax for iloc[row_idx_start:row_idx_end, col_idx_start:col_idx_end]
                # If column indexes are not provided, then all columns will be selected by default
                # A list containing column indexes can also be used
                return self.my_df.iloc[_row_start:_row_end+1, _col_idx_list]
        else:
            print('Column Names must be in a list')

    def get_specific_cell_val_based_on_row_num_col_name(self, _row_idx, _col_name):
        '''
        Method to get a cell value based on row index and column name
        Arguments to this method are: - Row index and Column name
        NOTE: - Only a single cell value will be returned, since the intersection is a row and column index
        '''
        # loc allows accessing columns by name
        # iloc allows accessing columns by their index
        # syntax for loc[row_label, column_label]
        return self.my_df.loc[_row_idx, _col_name]


    def get_row_val_by_row_idx(self, _pandas_row_idx):
        '''
        Method to get row values based on pandas row index
        Argument to this method is: - Row index of the pandas dataframe
        Note: Pandas row index is 2 + excel row index, since header row index is 0. 
        Pandas excludes the header row for df and starts with 0 for the first value row
        '''
        return [_ for _ in self.my_df.itertuples()][_pandas_row_idx]

    def get_unique_value_count_in_col(self, _col_name):
        '''
        Method to get count of unique items in a given column
        Argument to this method is: - Column name
        '''
        return self.my_df[_col_name].nunique()

    def prefix_delim(self, _tgt_col_name, _delim):
        '''
        Method to add a delimiter as prefix
        Note:- This was added for understanding, however their are pre-built functions in pandas for this task
        '''
        self.my_df[_tgt_col_name] = _delim + self.my_df[_tgt_col_name].astype(str)

    def reset_to_default_int_idx(self):
        '''
        Method to reset the index to default integer values
        No Arguments to this method
        '''
        return self.my_df.reset_index()

    def rename_col(self, _old_col_name, _new_col_name):
        '''
        Method to rename an existing column
        Arguments to this method are: - Old column name and New Column Name
        '''
        try:
            # Assign the renamed columns to original dataframe
            # so that changes are reflected in spreadsheet
            self.my_df = self.my_df.rename(columns={_old_col_name: _new_col_name})
        except KeyError:
            print(f' Column Name :- "{_old_col_name}" not found in the dataframe')

    def rename_multiple_cols(self, _old_col_name_iterable, _new_col_name_iterable):
        '''
        Method to rename multiple columns at once
        Arguments to this method are: - Two iterables, first with the old column names
        And second with the new column names
        '''
        # The length of both the iterables must be same
        # Same number of column names in the list for replacement
        if len(_old_col_name_iterable) == len(_new_col_name_iterable):
            # Create a dictionary using the two lists
            _my_map = dict(zip(_old_col_name_iterable, _new_col_name_iterable))
            # Iterate over the key-value pair of the dictionary
            for _ocv, _ncv in _my_map.items():
                # Assign the renamed columns to original dataframe
                # so that changes are reflected in spreadsheet
                self.my_df = self.my_df.rename(columns={str(_ocv): str(_ncv)})

    def suffix_delim(self, _tgt_col_name: str, _delim: str):
        '''
        Method to add a delimiter as suffix
        Note:- This was added for understanding, however their are pre-built functions in pandas for this task
        '''
        self.my_df[_tgt_col_name] = self.my_df[_tgt_col_name].astype(str) + _delim

    def save_df_same_tgt(self):
        '''
        Method to save the dataframe in the same file
        Based on the file extension appropriate pandas function will be called to save the data
        '''
        # If the file extension is xlsx then 'to_excel' will be called
        if self.my_filename.split('.')[-1] == 'xlsx':
            return self.my_df.to_excel(self.my_filename, index=False)
        # If the file extension is csv then 'to_csv' will be called
        elif self.my_filename.split('.')[-1] == 'csv':
            return self.my_df.to_csv(self.my_filename, index=False)

    def save_df_diff_tgt(self, _tgt_file_name: str):
        '''
        Method to save the dataframe to a different file
        Based on the file extension appropriate pandas function will be called to save the data
        '''
        # If the file extension is xlsx then 'to_excel' will be called
        if self.my_filename.split('.')[-1] == 'xlsx':
            return self.my_df.to_excel(_tgt_file_name, index=False)
        elif self.my_filename.split('.')[-1] == 'csv':
            return self.my_df.to_csv(_tgt_file_name, index=False)

    def set_col_as_index(self, _col_name: str):
        '''
        Method to set a column as the index column
        Argument to this method is: - Column name which needs to be set as index
        '''
        return self.my_df.set_index(_col_name)

    def value_frequency_in_col_by_idx(self, _col_idx: int):
        '''
        Method to get frequency of occurrences per unique item in a given column
        Argument to this method is: - Column index position
        '''
        return self.my_df[self.my_df_col_idx_name[_col_idx]].value_counts()

    def value_frequency_in_col_by_name(self, _col_name: str):
        '''
        Method to get frequency of occurrences per unique item in a given column
        Argument to this method is: - Column index position
        '''
        return self.my_df[_col_name].value_counts()
