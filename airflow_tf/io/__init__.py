from ..helpers import Helpers
import pandas as pd

@Helpers.as_airflow_tasks()
class IO:
    r"""
    Input/Output helps to extract data from different sources, like '.csv', '.tpl', 'sql databases', etc, into a Pandas
    DataFrame to be transformed in Airflow Pipelines.
    """
    @staticmethod
    def load_dataset(filepath:str)->pd.DataFrame:
        """Documentation here
        """
        return pd.DataFrame()
    
    @staticmethod
    def save_dataset(df:str):
        """Documentation here
        """
        pass
