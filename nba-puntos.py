import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("games.csv")

# 1. Calcular la columna TOTAL_POINTS sumando los puntos de local y visitante
df["TOTAL_POINTS"] = df["PTS_home"] + df["PTS_away"]

# 2. Ordenar de mayor a menor utilizando el método optimizado de Pandas
sorted_games = df.sort_values(by="TOTAL_POINTS", ascending=False)

# 3. Mostrar los 10 partidos con mayor puntaje
for idx, g in sorted_games.head(10).iterrows():
  print(
      f"{g['GAME_DATE_EST']}: Home ID {g['HOME_TEAM_ID']} ({g['PTS_home']}) "
      f"vs Away ID {g['VISITOR_TEAM_ID']} ({g['PTS_away']}) "
      f"[Total: {g['TOTAL_POINTS']}]"
  )