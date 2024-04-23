from data_providers.local_provider import LocalDataProvider
from data_processors.core_processor import CoreDataProcessor
from data_writers.postgres_writer import PostgresDataWriter
import logging
import time


logging.basicConfig(level="DEBUG")
LOG = logging.getLogger()


if __name__ == '__main__':
    start_time = time.time()
    data_provider = LocalDataProvider()
    data_processor = CoreDataProcessor()
    data_writer = PostgresDataWriter()
    result_data_frame, metrics_df = data_processor.process(data_provider.provide())
    data_writer.write(result_data_frame, metrics_df)
    LOG.info(f"Processing finished in {time.time() - start_time} seconds.")

