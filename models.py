from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import List
import datetime


Base = declarative_base()


class Station(Base):
    __tablename__ = 'stations'
    id: Mapped[int] = mapped_column(primary_key=True) 
    station_name: Mapped[str] 
    longitude: Mapped[float]
    latitude: Mapped[float]
    production_date: Mapped[datetime.datetime]
    station_observations: Mapped[List['StationObservation']] = relationship(
        back_populates='station',
        cascade='all, delete-orphan',
    )
    atmospheric_forecasts: Mapped[List['AtmosphericForecast']] = relationship(
        back_populates='station',
        cascade='all, delete-orphan',
    )

    def __repr__(self):
        return "<Station(id='{}', station_name='{}')>".format(self.id, self.station_name)


class StationObservation(Base):
    __tablename__ = 'station_observations'
    id: Mapped[int] = mapped_column(primary_key=True)  
    observation_time: Mapped[datetime.datetime]
    station_id = mapped_column(ForeignKey('stations.id'))
    station: Mapped[Station] = relationship(back_populates='station_observations')
    air_temperature: Mapped[float] = mapped_column(nullable=True)
    dew_point: Mapped[float] = mapped_column(nullable=True)
    presence_of_precipitation: Mapped[bool] = mapped_column(nullable=True)
    # скорость ветра в км/ч
    wind_speed: Mapped[float] = mapped_column(nullable=True)
    # значения от 0 до 8 см. классификацию
    road_condition: Mapped[int] = mapped_column(nullable=True)
    road_surface_temperature: Mapped[float] = mapped_column(nullable=True)
    # температура покрытия на глубине 40см
    road_subsurface_temperature: Mapped[float] = mapped_column(nullable=True)

    def __repr__(self):
        return "<Station(id='{}', station_name='{}', observation_time='{}')>".format(self.id, self.observation_time)
    

class AtmosphericForecast(Base):
    __tablename__ = 'atmospheric_forecast'
    id: Mapped[int] = mapped_column(primary_key=True)  
    forecast_time: Mapped[datetime.datetime]
    station_id = mapped_column(ForeignKey('stations.id'))
    station: Mapped[Station] = relationship(back_populates='atmospheric_forecasts')
    air_temperature: Mapped[float] 
    dew_point: Mapped[float]
    # количество дождя в мм с начала прогноза
    rain_precipitation_quantity: Mapped[float]
    # количество снега в см с начала прогноза
    snow_precipitation_quantity: Mapped[float]
    # скорость ветра в км/ч
    wind_speed: Mapped[float]
    # давление воздуха на высоте станции в милибарах
    road_surface_pressure: Mapped[float] 
    # значения от 0 до 8 (0 - безоблачно, 8 - полная облачность)
    octal_cloud_coverage: Mapped[int]

    def __repr__(self):
        return "<Station(id='{}', station_name='{}', forecat_time='{}')>".format(self.id, self.station_name, self.forecast_time)
    

    
