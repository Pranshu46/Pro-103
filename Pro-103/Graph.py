import pandas as pd
import plotly_express as px

df = pd.read_csv('data.csv')
graph = px.scatter(df,x = 'date',y = 'cases',color = 'country')
graph.show()