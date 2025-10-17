def df_sampling_bottom_10_rows(self):
    '''
    Method returns the bottom 10 rows of the DataFrame.
    Input: None
    Output: DataFrame containing the last 10 rows.
    '''
    return self.my_df.tail(10)