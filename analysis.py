import pandas as pd
import plotly.express as px

df = pd.read_csv("rides.csv")
df.dropna()

supply = df["Drivers Active Per Hour"]
demand = df["Riders Active Per Hour"]

fig = px.scatter(df, x="Drivers Active Per Hour", y= "Riders Active Per Hour", trendline="ols", title="Supply and Demand")
fig.show()

avg_demand = demand.mean()
avg_supply = supply.mean()

rate_change_demand = (max(demand)-min(demand))/avg_demand*100
rate_change_supply = (max(supply)-min(supply))/avg_supply*100

elasticity = rate_change_demand/rate_change_supply

print(f"Elasticity of demand respect to supply per hour: {elasticity}")

df["Supply Ratio"] = df["Rides Completed"]/supply
    
fig = px.scatter(df, x="Drivers Active Per Hour", y= "Supply Ratio", trendline="ols", title="Supply Ratio and Driver Activity")
fig.show()
