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