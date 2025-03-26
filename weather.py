# Import the module.
import python_weather

import asyncio
import os


async def main() -> None:

  # Declare the client. The measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.METRIC) as client:

    # Fetch a weather forecast from Ouarzazate, Morocco.
    weather = await client.get('Ouarzazate')

    # Fetch the wind speed for today. (THIS OUTPUTS OLD DATA; WE WANT REAL TIME OR WEATHER FORECAST)
    '''print(f"Date and Time in Ourzazate: {weather.datetime}")
    print(f"Time of Call: {weather.datetime.now()}")
    print(f"Wind speed: {weather.wind_speed} km/h")
    print(f"Wind direction: {weather.wind_direction.degrees}°")
    print(f"UV index: {weather.ultraviolet.index}")'''

    # Fetch weather forecast for the day.
    count = 0; # random variable

    for daily in weather:
      if count != 0:
        count = 0 # might not need this for when code is run following day
        break
      else:
        print(daily)
        count +=1

      # Each daily forecast has their own hourly forecasts.
        for hourly in daily:
          print(f'Hour of the day: {hourly.time!r}')
          print(f'--> Wind speed: {hourly.wind_speed!r} km/h')
          print(f'--> Wind direction: {hourly.wind_direction.degrees!r}°')

if __name__ == '__main__':

  # See https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
  # for more details.
  if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

  asyncio.run(main())