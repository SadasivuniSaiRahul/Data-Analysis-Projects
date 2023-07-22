import pandas as pd 
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("Screen Time Analysis/Screentime-App-Details.csv")
# print(data.head())
# print(data.isnull().sum()) # Checking if there are any null values

# Usage of Apps
figure1 = px.bar(data_frame=data, 
                x = "Date", 
                y = "Usage", 
                color="App", 
                title="Usage of Apps (Rahul)")
figure1.show()

#  No of Notifications from Apps

figure2 = px.bar(data_frame=data, 
                x = "Date", 
                y = "Notifications", 
                color="App", 
                title="Notifications(Rahul)")
figure2.show()

#  No of times the apps were opened

figure3 = px.bar(data_frame=data, 
                x = "Date", 
                y = "Times opened", 
                color="App",
                title="Times Opened(Rahul)")
figure3.show()

# Relation between notofications received and apps usage 
figure4 = px.scatter(data_frame = data, 
                    x="Notifications",
                    y="Usage", 
                    size="Notifications", 
                    trendline="ols", 
                    title = "Relationship Between Number of Notifications and Usage")
figure4.show()


