import fastf1 as ff1
import fastf1

#Made using Fast F1 by Siddharth Tewari
fastf1.Cache.enable_cache('cache')

laps = ff1.get_session(2021, 'Turkey', 'R').load_laps()
print("Hamilton")
best_hamilton = laps.pick_driver('HAM').pick_fastest()
print(best_hamilton['LapTime'])

print("Bottas")
best_bottas = laps.pick_driver('BOT').pick_fastest()
print(best_bottas['LapTime'])

print("Max")
best_max = laps.pick_driver('VER').pick_fastest()
print(best_max['LapTime'])

print("Perez")
best_checo = laps.pick_driver('PER').pick_fastest()
print(best_checo['LapTime'])

print("Leclerc")
best_leclerc = laps.pick_driver('LEC').pick_fastest()
print(best_leclerc['LapTime'])

print("Sainz")
best_sainz = laps.pick_driver('SAI').pick_fastest()
print(best_sainz['LapTime'])

print("Lando")
best_lando = laps.pick_driver('NOR').pick_fastest()
print(best_lando['LapTime'])

print("Riccardo")
best_riccardo = laps.pick_driver('RIC').pick_fastest()
print(best_riccardo['LapTime'])

print("Vettel")
best_vettel = laps.pick_driver('VET').pick_fastest()
print(best_vettel['LapTime'])

print("Stroll")
best_stroll = laps.pick_driver('STR').pick_fastest()
print(best_stroll['LapTime'])

print("Alonso")
best_alonso = laps.pick_driver('ALO').pick_fastest()
print(best_alonso['LapTime'])

print("Ocon")
best_ocon = laps.pick_driver('OCO').pick_fastest()
print(best_ocon['LapTime'])

print("Gasly")
best_gasly = laps.pick_driver('GAS').pick_fastest()
print(best_gasly['LapTime'])

print("Tsunoda")
best_yuki = laps.pick_driver('TSU').pick_fastest()
print(best_yuki['LapTime'])

print("Russell")
best_russell = laps.pick_driver('RUS').pick_fastest()
print(best_russell['LapTime'])

print("Latifi")
best_latifi = laps.pick_driver('LAT').pick_fastest()
print(best_latifi['LapTime'])

print("Kimi")
best_kimi = laps.pick_driver('RAI').pick_fastest()
print(best_kimi['LapTime'])

print("Giovinazzi")
best_giovinazzi = laps.pick_driver('GIO').pick_fastest()
print(best_giovinazzi['LapTime'])

print("Mick")
best_mickymouse = laps.pick_driver('MSC').pick_fastest()
print(best_mickymouse['LapTime'])

print("Mazepin")
best_spin = laps.pick_driver('MAZ').pick_fastest()
print(best_spin['LapTime'])







