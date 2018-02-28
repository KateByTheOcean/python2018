# Automate the heinous stuff

from openpyxl import load_workbook
wb1 = load_workbook('December 2017 Analysis.xlsx')
print wb1.get_sheet_names()

wb1.guess_types = 1 # enables automatic type association (I <3 Duck Typing)
ws1 = wb1.active # identifies the active sheet
sheet_ranges = wb1['2191 2ug Toluene']
print(sheet_ranges['D'].value)



