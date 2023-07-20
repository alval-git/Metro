from sqlalchemy import create_engine, select, update
from sqlalchemy.orm import Session
from config import DATABASE_URI, DEBUG
from models import Base, Station, StationObservation
from parsers.station_parser import parseStations
# from parsers.air_temp_parser import parseAirTemperature
# from parsers.base_parser import baseParser
from parsers.join_observations_data import joinData

import datetime
import os

engine = create_engine(DATABASE_URI, echo=DEBUG)

def main():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:

        # добавление метеостанций в бд
        stations_list = parseStations()
        stations = [Station(station_name = station["station_name"], longitude = station["longitude"], latitude = station["latitude"], \
                    production_date = datetime.datetime.now()) for station in stations_list]
        session.add_all(stations)
        session.commit()

        # добавление наблюдений за метеостанциями (название станции, время наблюдения, температура воздуха)
        stations = session.execute(select(*Station.__table__.columns).order_by(Station.station_name)).fetchall()
        objects = joinData(stations)
        
        print(len(objects))
        observations = [StationObservation(station_id = obj["station_id"], air_temperature = obj["air_temperature"],\
                        observation_time = obj["observation_time"], road_surface_temperature = obj["road_surface_temperature"]) \
                        for obj in objects]
        session.add_all(observations)
        session.commit()
        
        # surface_temp_list = baseParser("surface_temp.xlsx", "Температура поверхности")
        # i = 0
        # for surface_temp_obj in surface_temp_list:
        #     session.execute(update(StationObservation).values(road_surface_temperature = surface_temp_obj["parameter_value"]) \
        #                     .where(StationObservation.observation_time == surface_temp_obj["observation_time"] \
        #                     and StationObservation.station.station_name == surface_temp_obj["station_name"]  )
        #                     )
        #     # session.execute(update(db_obj))
        #     i += 1
        #     if i == 1000:
        #         break
        # session.commit()

        


if __name__ == '__main__':
    main()