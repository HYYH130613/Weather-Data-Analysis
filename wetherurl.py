
import pandas as pd
import requests as r


latitude = 52.2297
longitude = 21.0122

url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    f"&hourly=temperature_2m,apparent_temperature&start_date=2025-08-01&end_date=2025-09-14&"
)

filepath = "./wetherdata.csv"

def get_data(url):
    response = r.get(url)
    data = response.json()
    hourly = data['hourly']
    df = pd.DataFrame(hourly)
    
    return df

df = get_data(url)
df.to_csv(filepath)