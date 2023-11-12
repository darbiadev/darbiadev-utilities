"""Utility functions."""

from logging import Logger
from pathlib import Path

import pandas as pd


def load_sheet(
    logger: Logger,
    data_path: Path,
    file_name: str,
    sheet_name: str,
) -> list[dict]:
    """
    Load a sheet from a spreadsheet.

    Parameters
    ----------
    logger
        logger
    data_path
        path to the data directory
    file_name
        name of the spreadsheet
    sheet_name
        name of the sheet

    Returns
    -------
    data
        list of dicts representing the rows in the sheet

    """
    logger.info("_load_sheet: %s %s", file_name, sheet_name)
    return (
        pd.read_excel(
            io=str(data_path / file_name),
            sheet_name=sheet_name,
        )
        .fillna("")
        .to_dict(orient="records")
    )
