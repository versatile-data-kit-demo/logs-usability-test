# Copyright 2021-2023 VMware, Inc.
# SPDX-License-Identifier: Apache-2.0
import logging

import pandas as pd
from vdk.api.job_input import IJobInput

log = logging.getLogger(__name__)


def run(job_input: IJobInput):

    # Read CSV data into a DataFrame
    df = pd.read_csv("./data.csv")

    df['Age'] = pd.to_numeric(df['Age'], errors='coerce').fillna(0) + 1

    job_input.execute_query("""CREATE TABLE IF NOT EXISTS people (ID TEXT, Name TEXT, Age TEXT, City TEXT)""")

    rows = df.values.tolist()
    column_names = df.columns.tolist()

    job_input.send_tabular_data_for_ingestion(
        rows=rows,
        column_names=column_names,
        destination_table="people"
    )