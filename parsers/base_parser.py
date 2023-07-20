from .load_excel_book import load_excel_book



def baseParser(file_name, sheet_name):
    excel_book = load_excel_book('../Metro/BGU/' + file_name)
    sheet = excel_book[sheet_name]
    observation_list = []
    for row in range(2, sheet.max_row + 1):
        station_name = sheet.cell(row = row, column = 3).value
        observation_time = sheet.cell(row = row, column = 2).value
        parameter_value = sheet.cell(row = row, column = 1).value
        dict = {"station_name": station_name, "observation_time": observation_time, "parameter_value": parameter_value}
        observation_list.append(dict)

    return observation_list