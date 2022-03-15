from pathlib import Path


class ReadPath:

    Base = Path(__file__).resolve().parents[1]

    @staticmethod
    def excel_path():

        excel_bath = ReadPath.Base/'data'/'phone.xlsx'

        return excel_bath


#  练习"""
"""class Read:

    re = Path(__file__).resolve().parents[1]

    @staticmethod
    def excel_path():

        excel_path = Read.re/'data'/'Phone.xlsx'

        return excel_path"""
read = ReadPath()
read.excel_path()
