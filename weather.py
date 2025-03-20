# Import the module.
import python_weather

import asyncio
import os


async def main() -> None:

  # Declare the client. The measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.METRIC) as client:

    # Fetch a weather forecast from a city.
    weather = await client.get('Ouarzazate')

    # Fetch the temperature for today.
    print(f"Date and Time: {weather.datetime}")
    print(f"Wind speed: {weather.wind_speed} km/h")
    print(f"Wind direction: {weather.wind_direction.degrees}°")
    print(f"UV index: {weather.ultraviolet.index}")

    # Fetch weather forecast for upcoming days.
    for daily in weather:
      print(daily)

      # Each daily forecast has their own hourly forecasts.
      for hourly in daily:
        print(f' --> {hourly!r}')


    # NEXT STEPS: adjust for loop to fetch weather forecast for one day only
        # change to output wind

if __name__ == '__main__':

  # See https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
  # for more details.
  if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

  asyncio.run(main())