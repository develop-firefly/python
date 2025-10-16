def drop_col_by_index(self, _col_idx):
    '''
    Method to drop a column from the dataframe using its index position
    Input :param _col_idx: Index position of the column to be removed
    Output: None
    '''
    try:
        self.my_df.drop(self.my_df.columns[_col_idx], axis=1, inplace=True)
    except IndexError:
        print(
            f'ERROR: - Index value {_col_idx} is out of bounds, Current Index length is {self.my_df.shape[-1]}')
