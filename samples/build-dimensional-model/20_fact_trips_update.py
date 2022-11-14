import logging
import os

from vdk.api.job_input import IJobInput

log = logging.getLogger(__name__)

def run(job_input: IJobInput) -> None:
    """
    The following aspects are automatically handled by the template.

    1. Late arrival updates are generally supported.
    2. It overwrites the overlap between the new data (the source) and target

    See https://github.com/vmware/versatile-data-kit/wiki/SQL-Data-Processing-templates-examples#append-strategy-fact


    """
    job_input.execute_template(
        template_name='periodic_snapshot',
        template_args={
            'source_schema': os.environ.get("VDK_TRINO_SCHEMA"),
            'source_view': 'staging_area_trips',
            'target_schema': os.environ.get("VDK_TRINO_SCHEMA"),
            'target_table': 'fact_trips',
            'last_arrival_ts': 'date'
        },
    )
