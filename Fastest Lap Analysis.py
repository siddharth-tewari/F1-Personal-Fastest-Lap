import fastf1 as ff1
import fastf1
from timple.timedelta import strftimedelta


fastf1.Cache.enable_cache('cache')

laps = ff1.get_session(2021, 22, 'Q').load_laps()

td = laps.pick_driver('VER').pick_fastest()['LapTime']
print("Max Verstappen")
print(strftimedelta(td, '%m:%s.%ms'))

best = laps.pick_driver('VER').pick_fastest()
weather = laps.pick_driver('VER').get_weather_data()
print("Tyre Age: ",best['TyreLife'], "laps old")
print("Tyre Compound:",best['Compound'])
print("Weather: ",'\n',weather)





 
