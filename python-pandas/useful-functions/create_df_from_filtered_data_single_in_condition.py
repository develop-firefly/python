import pandas as pd
def create_df_from_filtered_data_single_in_condition(self, _column_name, _condition):
    '''
    Create Dataframe from filtered data based on single condition
    Input:1 - param _column_name: Column name where condition is to be applied
    Input:2 - param _condition: Condition to be applied on the column
    '''
    # create a new filtered dataset based on the condition applied on the column
    _filtered_data_set = (self.my_df.loc[self.my_df[_column_name] == _condition])
    # return Dataframe
    return pd.DataFrame(_filtered_data_set)