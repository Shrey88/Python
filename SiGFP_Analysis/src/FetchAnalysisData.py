from configparser import ConfigParser
from src.SigfpDB import SigfpDB
from fileParsing import FileParsing
import pyodbc
import datetime


class FetchAnalysisData(object):

    def __init__(self):
        self._sigfpdb = SigfpDB()
        self._parser = None
        self._conn = None
        self._cursor = None

    def _fetch_data(self):
        self._conn = self._sigfpdb.get_conn()

        if self._conn is not None:
            self._cursor = self._conn.cursor()
            try:
                if self._cursor is not None:
                    select_col = FileParsing.parse_file(filename='..\\_external_files\\arg_param.ini',
                                                        section='COLUMN_NAMES', outputformat='List')
                    select_col = ",".join(select_col)

                    execution_date = FileParsing.parse_file(filename='..\\_external_files\\arg_param.ini',
                                                            section='EXECUTION_DATE', outputformat='String')

                    if execution_date != 'None':
                        self._cursor.execute(f"SELECT {select_col} "
                                             f"FROM SiGFP.dbo.SiGFP_Summary "
                                             f"WHERE execution_date={execution_date}")
                    else:
                        self._cursor.execute(f"SELECT {select_col} "
                                             f"FROM SiGFP.dbo.SiGFP_Summary "
                                             f"WHERE execution_date='{datetime.datetime.now().date()}'")

                rows = self._cursor.fetchall()
                if rows is not None:
                    print(f"==> {rows.__len__()} results found")
                    self._sigfpdb.close_conn(self._cursor)
                    return rows
                else:
                    print("==> 0 results found")
                    self._sigfpdb.close_conn(self._cursor)
                    return None
            except(Exception, pyodbc.DatabaseError) as error:
                print(f"Exception: {error}")

    def fetch_data(self):
        # FetchAnalysisData._fetch_data(self)
        return self._fetch_data()

    @staticmethod
    def get_column_header(filename='..\\_external_files\\arg_param.ini',
                          section='COLUMN_NAMES', outputformat='List'):
        return FileParsing.parse_file(filename=filename, section=section, outputformat=outputformat)
