# -----------------------------------------------------------------------------
# Copyright (c) 2012 - 2018, Anaconda, Inc. and Intake contributors
# All rights reserved.
#
# The full license is in the LICENSE file, distributed with this software.
# -----------------------------------------------------------------------------

from intake.readers.datatypes import CSV
from intake.readers.readers import DaskCSV, PandasCSV, SparkDataFrame


class CSVSource:
    """Read CSV files into dataframes

    Backward compatibility for V1 catalogs.
    """

    name = "csv"

    def __init__(self, urlpath, storage_options=None, metadata=None, **kwargs):
        self.data = CSV(url=urlpath, storage_options=storage_options, metadata=metadata)
        self.kwargs = kwargs

    def discover(self):
        return PandasCSV(self.data).discover(**self.kwargs)

    def to_dask(self):
        return DaskCSV(self.data).read(**self.kwargs)

    def read(self):
        return PandasCSV(self.data).read(**self.kwargs)

    def to_spark(self):
        return SparkDataFrame(self.data).read(**self.kwargs)
