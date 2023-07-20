from .load_excel_book import load_excel_book 
import json


excel_book = load_excel_book('../Metro/BGU/stations.xlsx')
sheet = excel_book['Точки']

def parseStations():
    stations = []
    for row in range(1, sheet.max_row + 1):
        if ( sheet.cell(row = row, column = 1).value != None) & ( "type" in sheet.cell(row = row, column = 2).value):
            station_name = sheet.cell(row = row, column = 1).value
            dict = json.loads(sheet.cell(row = row, column = 2).value)
            latitude = dict['coordinates'][0]
            longitude = dict['coordinates'][1]
            stations.append({'station_name': station_name, 'latitude': latitude, 'longitude': longitude})
    return stations
            

   





