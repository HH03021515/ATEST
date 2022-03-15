import openpyxl
import faker
from base.base_path import ReadPath


class GreatData:

    def __init__(self):

        self.book = openpyxl.Workbook()
        self.sheet = self.book.active

    def great(self):

        title = ['姓名', '电话']
        self.sheet.append(title)

        faker_data = faker.Faker(locale='zh_CN')

        for i in range(50):
            self.sheet.append([faker_data.name(), faker_data.phone_number()])

        self.book.save(ReadPath().excel_path())


# 练习
"""class ExcelData:

    def __init__(self):

        self.book = openpyxl.Workbook()
        self.sheet = self.book.active

    def excel_data(self):

        title = ['姓名', '电话']
        self.sheet.append(title)

        faker_data = faker.Faker(locale='zh_CN')

        for i in range(50):
            self.sheet.append([faker_data.name(), faker_data.phone_number])

        self.book.save(Read.excel_path())"""

great = GreatData()
great.great()
