# Copyright 2021-2023 VMware, Inc.
# SPDX-License-Identifier: Apache-2.0
import logging

import pandas as pd
from vdk.api.job_input import IJobInput

log = logging.getLogger(__name__)


def run(job_input: IJobInput):

    # Read CSV data into a DataFrame
    df = pd.read_csv("./data.csv")

    df['Age'] = df['Age'] + 1  # Increment age by 1

    job_input.execute_query("""CREATE TABLE IF NOT EXISTS people (ID TEXT, Name TEXT, Age TEXT, City TEXT)""")
    job_input.send_tabular_data_for_ingestion(table_name="people", method="insert", payload=df)