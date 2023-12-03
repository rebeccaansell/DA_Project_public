import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd

df_combined = pd.read_csv('p4_combined_data.csv')

df_combined['7_day_avg_cases'] = df_combined['Daily_Cases'].rolling(window=7).mean()

fig = px.line(df_combined, x='Start_Date', y='Total_Rides',
              title='Total Bike Rides Over Time')

# Add rangeslider
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

# Create a figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add the total bike rides to the primary y-axis
fig.add_trace(
    go.Scatter(x=df_combined['Start_Date'], y=df_combined['Total_Rides'], name='Total Bike Rides', marker_color='blue'),
    secondary_y=False,
)

# Add the COVID-19 cases to the secondary y-axis
fig.add_trace(
    go.Scatter(x=df_combined['Start_Date'], y=df_combined['7_day_avg_cases'], name='7-Day Average COVID-19 Cases', marker_color='red'),
    secondary_y=True,
)

# Add titles and labels
fig.update_layout(
    title_text='Total Bike Rides and 7-Day Average COVID-19 Cases Over Time',
    xaxis_title='Date',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

# Set y-axes titles
fig.update_yaxes(title_text='Total Bike Rides', secondary_y=False)
fig.update_yaxes(title_text='7-Day Average COVID-19 Cases', secondary_y=True)

# Show the figure
fig.show()