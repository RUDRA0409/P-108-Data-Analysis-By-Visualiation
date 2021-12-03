
import pandas as pd
import csv
import plotly.graph_objects as px

df = pd.read_csv("P108.csv")

mean = df.groupby(["student_id", "level"])["attempt"].mean()

fig = px.Figure(px.Bar(x = df.groupby("level")["attempt"].mean(),y = ["level 1","level 2","level 3","level 4"],orientation = "h"))

fig.show()