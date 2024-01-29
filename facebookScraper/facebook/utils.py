"""
containe utils function
"""
import re
import datetime
from openpyxl.workbook import Workbook
from openpyxl.styles import Font, Alignment
def str_to_int(chaine:str)-> int:
    """
    @description:
        extracte number from string
    """
    return int(re.sub("[^0-9]", "", chaine))

center = Alignment(horizontal='center', vertical='center')
left = Alignment(horizontal='left' )
def excel_header(sheet,title:str, columns:list):
    """
    @description:
        define a header of excel file
    """
    sheet["A1"] = title + "Date-Time: " + str(datetime.datetime.now())
    sheet.merge_cells(range_string="A1:L1")
    sheet.row_dimensions[1].font = Font(bold=True, color='0000ff', sz=25)
    sheet.merge_cells("A1:L1")
    sheet.row_dimensions[1].alignment =  Alignment(horizontal='left', indent=30)
    sheet.row_dimensions[2].alignment =  Alignment(horizontal='center')
    sheet.row_dimensions[1].height = 50 
    sheet.sheet_properties.tabColor = "00ff00"
    #column list
    sheet.row_dimensions[2].font = Font(bold=True, size=18)
    sheet.row_dimensions[2].height = 25
    sheet.row_dimensions[2].alignment = center 
    sheet.column_dimensions["A"].width = 40
    sheet.column_dimensions["A"].alignment = left 
    sheet.column_dimensions["A"].font = Font(size=15, bold=True, color="343f3b")
    sheet.column_dimensions["B"].width = 30
    sheet.column_dimensions["B"].font = Font(size=15, bold=True) 
    sheet.column_dimensions["B"].alignment = center 
    sheet.column_dimensions["C"].width = 90
    sheet.column_dimensions["C"].font = Font(size=16, name='arial', color="526a89") 
    sheet.column_dimensions["C"].alignment = left 
    sheet.column_dimensions["D"].width = 100 
    sheet.column_dimensions["D"].alignment = left  
    sheet.column_dimensions["D"].font = Font(size=16, color='343f3b', bold=True) 
    sheet.column_dimensions["E"].width = 100 
    sheet.column_dimensions["E"].alignment = left  
    sheet.column_dimensions["E"].font = Font(size=16, color='343f3b', bold=True) 
    sheet.column_dimensions["F"].width = 100 
    sheet.column_dimensions["F"].alignment = left  
    sheet.column_dimensions["F"].font = Font(size=16, color='343f3b', bold=True) 
    sheet.append(columns)
def selenium_cookie_to_request(sel_cookies):
    return {cookie['name']: cookie['value'] for cookie in sel_cookies}


#from collector
import csv

# creating CSV header
def create_csv(filename):
    with open(filename, "w+", newline='', encoding="utf-8") as save_file:
        writer = csv.writer(save_file)
        writer.writerow(["Author", "uTime", "Text"])

# clean all non-alphanumberic characters       
def strip(string):
    words = string.split()
    words = [word for word in words if "#" not in word]
    string = " ".join(words)
    clean = ""
    for c in string:
        if str.isalnum(c) or (c in [" ", ".", ","]):
            clean += c
    return clean

def write_to_csv(filename, data):
    with open(filename, "a+", newline='', encoding="utf-8") as save_file:
        writer = csv.writer(save_file)
        writer.writerow(data)