import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("Students.csv")
studentDF = df.loc[df["student_id"] == "TRL_zny"]
fig = go.Figure(go.Bar(x = studentDF.groupby("level")["attempt"].mean(), y = ["Level 1", "Level 2", "Level 3", "Level 4"], orientation = "h"))
fig.show()