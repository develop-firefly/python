def suffix_delim(self, _tgt_col_name, _delim):
    '''
    Method to add a delimiter as suffix
    Input Arguments: - Target column name, Delimiter to be added as suffix
    '''
    self.my_df[_tgt_col_name] = self.my_df[_tgt_col_name].astype(str) + _delim