from pydantic import BaseModel

class Condition(BaseModel):
    text: str
    icon: str
    code: int

class CurrentWeather(BaseModel):
    temp_c: float
    humidity: int
    wind_kph: float
    condition: Condition

class Location(BaseModel):
    name: str
    region: str
    country: str
    lat: float
    lon: float
    localtime: str

class WeatherData(BaseModel):
    location: Location
    current: CurrentWeather