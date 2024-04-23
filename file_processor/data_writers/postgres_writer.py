import logging
import pandas as pd
import os
from data_writers.base_writer import BaseWriter
from sqlalchemy import create_engine
import time

LOG = logging.getLogger()


class PostgresDataWriter(BaseWriter):

    env_var_host = "POSTGRES_HOST"
    env_var_port = "POSTGRES_PORT"
    env_var_db = "POSTGRES_DB"
    env_var_user = "POSTGRES_USER"
    env_var_password = "POSTGRES_PASSWORD"
    env_var_result_table = "POSTGRES_RESULT_TABLE"
    env_var_import_table = "POSTGRES_IMPORT_TABLE"
    engine_uri = 'postgresql://{user}:{password}@{host}:{port}/{db}'

    def get_uri_elements(self):
        return {
            "user": os.getenv(self.env_var_user),
            "password": os.getenv(self.env_var_password),
            "host": os.getenv(self.env_var_host),
            "port": os.getenv(self.env_var_port),
            "db": os.getenv(self.env_var_db)
        }

    def get_engine(self):
        engine_uri = self.engine_uri.format(**self.get_uri_elements())
        LOG.info(f"engine_uri - {engine_uri}")
        return create_engine(engine_uri)

    def write(self, result_dataframe, import_dataframe):
        engine = self.get_engine()
        result_table = os.getenv(self.env_var_result_table)
        import_table = os.getenv(self.env_var_import_table)
        LOG.info(f"Writing to result table - {result_table}, import - {import_table}")
        result_dataframe.to_sql(
            name=result_table,  # table name
            con=engine,  # engine
            if_exists="append",  # If the table already exists, append
            index=False  # no index
        )
        import_dataframe.to_sql(
            name=import_table,  # table name
            con=engine,  # engine
            if_exists="append",  # If the table already exists, append
            index=False  # no index
        )