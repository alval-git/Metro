from .load_excel_book import load_excel_book

excel_book = load_excel_book('../Metro/BGU/air_temperature.xlsx')
sheet = excel_book['air_temperature']

def parseAirTemperature(stations):
    observation_list = []
    for row in range(2, sheet.max_row + 1):
        station_name = sheet.cell(row = row, column = 3).value
        station_id = 0
        for station in stations:
            if station_name == station[1]:
                station_id = station[0]
                observation_time = sheet.cell(row = row, column = 2).value
                air_temp = sheet.cell(row = row, column = 1).value
                dict = {"station_id": station_id, "observation_time": observation_time, "air_temperature": air_temp}
                observation_list.append(dict)
                break



    return observation_list