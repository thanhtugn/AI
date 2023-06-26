import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

excel_file_path = "Cars_Data.csv"

data_excel = pd.read_csv(excel_file_path)

# print(data.head())

# df = px.data.gapminder().query("brand = bmw")
# df.head()

# data_line = px.line(x=["Jan", "Feb", "Mar", "Apr", "May", "Jun"], y=[45.6, 47, 56, 34, 59, 66], title="abc")
# data_line.show() 

# data_line_chart_excel = px.line(data_excel, x='brand', y='price', title='line chart from excel file')
# data_line_chart_excel.show()

# bar_chart_excel = px.bar(data_excel, x='brand', y = 'price', hover_data=['price', 'brand'], color='price', title='bar chart from excel file', labels={'price': 'price'}, height=400) 
# bar_chart_excel.show()

# car_brand = ['chevrolet', 'honda', 'bmw']
# car_type = ['sedan', 'hatchback', 'wagon']
# fig = go.Figure(data=[
#     go.Bar(name='Car 1', x= car_brand, y= [45, 67, 65], textposition='auto'),
#     go.Bar(name='Car 2', x= car_brand, y= [60, 23, 39], textposition='auto')
# ])

# fig.update_layout(barmode='stack')
# fig.show()

# label_brand = data_excel['brand'].tolist()
# wheel_base = data_excel['wheel-base'].tolist()

# fig_pie = px.pie(data_excel, values='wheel-base', names='brand', title='wheel-base of every car brand')
# fig_pie.show()

label_brand = data_excel['brand'].tolist()
wheel_base = data_excel['wheel-base'].tolist()

fig_donut = go.Figure(data=[go.Pie(labels=label_brand, values=wheel_base, hole=.3)])
fig_donut.show()