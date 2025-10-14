def save_df_diff_tgt(self, _tgt_file_name):
    '''
    Method to save the dataframe to a different file
    Based on the file extension appropriate pandas function will be called to save the data
    Input: - Target file name where dataframe needs to be saved'''
    # If the file extension is xlsx then 'to_excel' will be called
    if self.my_filename.split('.')[-1] == 'xlsx':
        return self.my_df.to_excel(_tgt_file_name, index=False)
    elif self.my_filename.split('.')[-1] == 'csv':
        return self.my_df.to_csv(_tgt_file_name, index=False)