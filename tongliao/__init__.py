from .collect_data import collect_data

collect_data()
from .country2tongliao import country2tongliao, DATA as COUNTRIES_DATA
from .core import (
    TONGLIAO_CHINESE,
    TONGLIAO_ENGLISH,
    TONGLIAO_AREA,
    TONGLIAO_PEOPLE,
    area2tongliao,
    people2tongliao,
)

__all__ = [
    "TONGLIAO_AREA",
    "TONGLIAO_CHINESE",
    "TONGLIAO_ENGLISH",
    "TONGLIAO_PEOPLE",
    "area2tongliao",
    "country2tongliao",
    "people2tongliao",
]
