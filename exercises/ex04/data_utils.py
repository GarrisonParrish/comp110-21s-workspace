"""Utility functions for wrangling data."""

__author__ = "730324058"


from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    file_handle = open(csv_file, "r", encoding="utf8")
    # TODO 0.1) Complete the implementation of this function here.
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        rows.append(row)
    file_handle.close()
    return rows


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """List all values at column!"""
    columns: list[str] = []
    for row in table:
        columns.append(row[column])
    return columns


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Returns the table data as a dict of strings as the columns!"""
    return_table: dict[str, list[str]] = {}
    for column in table[0]:
        return_table[column] = column_values(table, column)
    return return_table


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Return a table with the first n rows for each column!"""
    if n > len(table):
        n = len(table)
    return_table: dict[str, list[str]] = {}
    for column in table:
        rows: list[str] = []
        for i in range(n):
            rows.append(table[column][i])
        return_table[column] = rows
    return return_table


def select(table: dict[str, list[str]], cols: list[str]) -> dict[str, list[str]]:
    """Return a table with only the selected columns!"""
    return_table: dict[str, list[str]] = {}
    for col in cols:
        return_table[col] = table[col]
    return return_table


def count(values: list[str]) -> dict[str, int]:
    """Count the number of times a value repeats in a list of values!"""
    return_table: dict[str, int] = {}
    for value in values:
        if value in return_table:
            return_table[value] += 1
        else:
            return_table[value] = 1
    return return_table