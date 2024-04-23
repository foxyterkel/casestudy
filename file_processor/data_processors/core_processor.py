import logging

import pandas as pd
from data_processors.base_processor import BaseProcessor

LOG = logging.getLogger()


class CoreDataProcessor(BaseProcessor):

    CORE_PROCESSOR_MAP = {
        "school": str,
        "sex": str,
        "age": int,
        "address": str,
        "famsize": str,
        "Pstatus": str,
        "Medu": int,
        "Fedu": int,
        "Mjob": str,
        "Fjob": str,
        "reason": str,
        "guardian": str,
        "traveltime": int,
        "studytime": int,
        "failures": int,
        "schoolsup": str,
        "famsup": str,
        "paid": str,
        "activities": str,
        "nursery": str,
        "higher": str,
        "internet": str,
        "romantic": str,
        "famrel": int,
        "freetime": int,
        "goout": int,
        "Dalc": int,
        "Walc": int,
        "health": int,
        "absences": int,
        "G1": int,
        "G2": int,
        "G3": int
    }

    def process(self, file_object):
        # import status DF
        metrics_series = pd.Series()
        metrics_series['file_name'] = file_object.name
        metrics_series['success'] = True
        metrics_series['error_message'] = None
        metrics_series['all_null_count'] = 0
        metrics_series['import_time'] = pd.Timestamp.now()

        # result DF
        raw_df = pd.DataFrame()

        try:
            raw_df = pd.read_csv(file_object, sep=";", dtype=self.CORE_PROCESSOR_MAP)
        except Exception as e:
            metrics_series['error_message'] = str(e)
            metrics_series['success'] = False
            return raw_df, metrics_series.to_frame().T

        # lowercase colum names
        raw_df.columns = map(str.lower, raw_df.columns)

        metrics_series['all_null_count'] = int(raw_df.isnull().all(axis=1).sum())
        metrics_df = metrics_series.to_frame().T

        return raw_df, metrics_df
