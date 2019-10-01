class Janitor:
    """
    Janitor - a class to help with cleaning up dataframes!
    """

    def __init__(self, df):
        self.df = df
        self.cols = df.columns

    def replace_values(self, value =nan, new = -999):
        """
        Replaces values in Dataframe.
        By default it will turn Default turns NaN values -999
        """
        self.df = self.df.replace(value, new)
    def drop_nans(self,axis=0,how='all'):
        """
        This will drop rows with NaN values in a DataFrame.
        """
        self.df = self.df.dropna(axis,how)