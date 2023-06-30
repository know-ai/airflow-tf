from ..helpers import Helpers
import pandas as pd

@Helpers.as_airflow_tasks()
class Preprocessing:
    """Documentation here
    """
    @staticmethod
    def set_rule(df:pd.DataFrame)->pd.DataFrame:
        """Documentation here
        """

        return df
    
    @staticmethod
    def add_instrument_noise(df:pd.DataFrame)->pd.DataFrame:
        """Documentation here
        """
        return df
    
    @staticmethod
    def set_time_window(df:pd.DataFrame)->pd.DataFrame:
        """Documentation here
        """

        return df
    
    @staticmethod
    def feature_extraction(df:pd.DataFrame)->pd.DataFrame:
        """Documentation here
        """
        return df
    
    @staticmethod
    def output_labelizer(df:pd.DataFrame)->pd.DataFrame:
        """Documentation here
        """

        return df
    
    @staticmethod
    def feature_selection(df:pd.DataFrame)->pd.DataFrame:
        """Documentation here
        """
        return df
    
    @staticmethod
    def merge(*dfs)->pd.DataFrame:
        """Documentation here
        """

        return pd.DataFrame()
    
    @staticmethod
    def shuffle(df:pd.DataFrame)->pd.DataFrame:
        """Documentation here
        """
        return df
    
    @staticmethod
    def split_input_output(df:pd.DataFrame)->pd.DataFrame:
        """Documentation here
        """