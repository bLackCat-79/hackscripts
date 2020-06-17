#!/usr/bin/env python3
#    Copyright (C) 2019 Alexandre Teyar

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
#    limitations under the License.

# TODO:
# * try to add the constant part of the code (workbook closing) to the
#   abstract method

from abc import ABC, abstractmethod

import logging
import xlsxwriter


class Parser(object):
    def __init__(self, input_files, output_file):
        self._input_files = input_files
        self._output_file = output_file
        self._workbook = xlsxwriter.Workbook("{}".format(output_file))

    @abstractmethod
    def print_vars(self):
        pass

    @abstractmethod
    def parse(self):
        pass

    def draw_table(self, worksheet, table_headers, table_data):
        column_count = 0
        row_count = 0
        table_column_count = column_count + len(table_headers) - 1
        table_row_count = row_count + len(table_data)

        logging.debug("{}".format(table_headers))
        logging.debug("{}".format(table_data))

        if table_data:
            worksheet.add_table(
                row_count,
                column_count,
                table_row_count,
                table_column_count,
                {
                    "banded_rows": True,
                    "columns": table_headers,
                    "data": table_data,
                    "first_column": True,
                    "style": "Table Style Medium 1"
                }
            )
        else:
            logging.warning(
                "parsing of the input file(s) returned an empty dataset")