import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"

data = pd.read_csv('rides.csv')
print(data.head())

#Looking for the Null Values and Removing it.
print(data.isnull().sum())
data = data.dropna()

#Looking relationship between Number of Drivers Active per Hour & Number of Riders active per Hour
demand = data["Riders Active Per Hour"]
supply = data["Drivers Active Per Hour"]

figure = px.scatter(data, x = "Drivers Active Per Hour",
                    y = "Riders Active Per Hour", trendline="ols", 
                    title="Demand and Supply Analysis")
figure.update_layout(
    xaxis_title="Number of Drivers Active per Hour (Supply)",
    yaxis_title="Number of Riders Active per Hour (Demand)",
)
figure.show()

#Calculating Elasticity of Demand for Rides concerning the Number of Active Drivers per Hour
avg_demand = data['Riders Active Per Hour'].mean()
avg_supply = data['Drivers Active Per Hour'].mean()
pct_change_demand = (max(data["Riders Active Per Hour"]) - min(data['Riders Active Per Hour'])) / avg_demand * 100
pct_change_supply = (max(data["Drivers Active Per Hour"]) - min(data['Drivers Active Per Hour'])) / avg_supply * 100
elasticity = pct_change_demand / pct_change_supply
print("Elasticity of Demand with respect to the Number of Active Drivers per Hour: {:.2f}".format(elasticity))

#Adding new Column in the Dataset by Calculating the Supply Ratio
data['Supply Ratio'] = data['Rides Completed'] / data['Drivers Active Per Hour']
print(data.head())

#Visualize the Supply Ratio
fig = go.Figure()
fig.add_trace(go.Scatter(x=data['Drivers Active Per Hour'], 
                         y=data['Supply Ratio'], mode='markers'))
fig.update_layout(
    title='Supply Ratio vs. Driver Activity',
    xaxis_title='Driver Activity (Drivers Active Per Hour)',
    yaxis_title='Supply Ratio (Rides Completed per Driver Active per Hour)'
)
fig.show()


