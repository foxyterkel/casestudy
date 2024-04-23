import logging
from data_providers.base_provider import BaseProvider


LOG = logging.getLogger()


class LocalDataProvider(BaseProvider):

    DEFAULT_LOCATION = "input_data/student-mat.csv"

    def __init__(self, file_location=None):
        self.file_location = file_location or self.DEFAULT_LOCATION

    def provide(self):
        LOG.info(f"Providing local file - {self.file_location}")
        return open(self.file_location)


