def copy_paste_cols_data(self, _src_col_name, _tgt_col_name):
    '''
    Method to copy the contents from one column to another column of dataframe
    Input:1 - _src_col_name:- The column from which data needs to be copied
    Input:2 - _tgt_col_name:- The column to which data needs to be
    Output: None
    '''
    # NOTE: - If target col does not exist in the dataframe, it will be created at run time
    try:
        self.my_df[_tgt_col_name] = self.my_df[_src_col_name]
    except KeyError:
        print(f' Source column :- "{_src_col_name}"  not found in worksheet')