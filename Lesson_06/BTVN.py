import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv('company_sales_data.csv')

data = data.sort_values('month_number')

monthly_profit = data.groupby('month_number')['total_profit'].sum().reset_index()

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=monthly_profit['month_number'],
    y=monthly_profit['total_profit'],

))

fig.update_layout(
    title='Company profit per month',
    xaxis=dict(title='month_number', tickmode='linear'),
    yaxis=dict(title='Sold units number'),
    height=600, 
    width=800
)

fig.show()


#b2
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=monthly_profit['month_number'],
    y=monthly_profit['total_profit'],
    mode='lines+markers',
    line=dict(color='red', dash='dash', width=3),
    marker=dict(color='black', symbol='circle', size=8),
))

fig.update_layout(
    title='Company profit per month',
    xaxis=dict(title='month_number', tickmode='linear'),
    yaxis=dict(title='Sold units number'),
    legend=dict(x=0.98, y=0.02, bgcolor='rgba(255, 255, 255, 0.5)', bordercolor='rgba(0, 0, 0, 0.5)', borderwidth=3),
    height=600, 
    width=800
)

fig.show()

#b3

fig = go.Figure()

products = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo']
for product in products:
    fig.add_trace(go.Scatter(
        x=data['month_number'],
        y=data[product],
        mode='lines+markers',
        name=product,
        marker=dict(symbol='circle'),
        line=dict(width=2)
    ))
fig.update_layout(
    xaxis=dict(title='month_number', tickmode='linear'),
    yaxis=dict(title='Number of Units Sold'),
    legend=dict(x=0, y=1, bgcolor='rgba(255, 255, 255, 0.5)', bordercolor='rgba(0, 0, 0, 0.5)', borderwidth=3),
    height=600, 
    width=800

)

fig.show()

#b4

toothpaste_sales = data[['month_number', 'toothpaste']].copy()

fig = px.scatter(toothpaste_sales, x='month_number', y='toothpaste', title='Toothpaste Sales per Month')

fig.update_layout(
    xaxis_title='Month Number',
    yaxis_title='Toothpaste Sales',
    height=500,
    width=800
)

fig.show()

#b5
facewash_soap_sales = data[['month_number', 'facecream', 'facewash']].copy()

fig = px.bar(facewash_soap_sales, x='month_number', y=['facecream', 'facewash'], barmode='group',
             title='facecream and facewash Sales per Month')

fig.update_layout(
    xaxis_title='Month Number',
    yaxis_title='Sales',
    legend_title='Product',
    height=500,
    width=800
)

fig.show()

#b6
bathingsoap_sales = data[['month_number', 'bathingsoap']].copy()

fig = px.bar(bathingsoap_sales, x='month_number', y='bathingsoap', title='Bathing Soap Sales per Month')

fig.update_layout(
    xaxis_title='Month Number',
    yaxis_title='Bathing Soap Sales',
    height=500,
    width=800
)

fig.show()

#b7
monthly_profit = data.groupby('month_number')['total_profit'].sum().reset_index()

fig = px.histogram(monthly_profit, x='total_profit', nbins=10, title='Distribution of Monthly Profit')

fig.update_layout(
    xaxis_title='Total Profit',
    yaxis_title='Frequency',
    height=500,
    width=800
)

fig.show()

#b8
products = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo']

last_year_sales = []
product_names = []

for product in products:
    total_sales = data[product].sum()
    last_year_sales.append(total_sales)
    product_names.append(product)

sales_data = pd.DataFrame({'Product': products, 'Sales': last_year_sales})

fig = go.Figure(data=[go.Pie(labels=product_names, values=last_year_sales)])

fig.show()
