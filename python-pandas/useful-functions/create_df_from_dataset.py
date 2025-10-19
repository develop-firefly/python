import pandas as pd
def create_df_from_dataset(self, _dataset):
    '''
    Method to create a dataframe from a dataset
    Input: - Dataset
    '''
    # create a dataframe using the user provided dataset
    self.my_df = pd.DataFrame(_dataset)
    # return Dataframe
    return self.my_df