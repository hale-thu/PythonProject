from datetime import date

events_in_dortmund = {
    "DEW21 Museumsnacht": (date(2026, 9, 19), date(2026, 9, 19)),
    "Djelem Djelem Kunst und Kulturfestival": (date(2026, 8, 28), date(2026, 9, 27)),
    "Digitale Woche 2026": (date(2026, 9, 15), date(2026, 9, 21)),
    "Die Nacht der Jugendkultur 2026": (date(2026, 9, 26), date(2026, 9, 27)),
    "Demokratietag in Scharnhorst": (date(2026, 9, 25), date(2026, 9, 25)),
}

museum_night_date = date(2026, 9, 19)

print("Museum night on", museum_night_date, ":")
for event, (start_date, end_date) in events_in_dortmund.items():
    if start_date <= museum_night_date <= end_date:
        print("-", event)
