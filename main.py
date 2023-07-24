import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import yfinance as yf

st.title('Stock Market Analysis by Industry')

start_date = datetime(2013, 1, 1)
end_date = datetime(2018, 1, 1)

tickers = ['AAPL', 'MSFT', 'JPM', 'V', 'CVX', 'XOM']

df_list = []

for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)
    monthly_data = data.resample('M').mean()  # Resample to monthly data and calculate the mean
    df_list.append(monthly_data)

df = pd.concat(df_list, keys=tickers, names=['Ticker', 'Date'])
df = df.reset_index()
df = df.drop('Volume', axis=1)
df = df.reset_index()

fig = px.line(df, x='Date',
              y='Close',
              color='Ticker',
              title="Stock Performance 2013-2018")

# Display the chart using st.plotly_chart
st.plotly_chart(fig)

# Create the Plotly figure
fig = px.area(df, x='Date', y='Close', color='Ticker',
              facet_col='Ticker',
              labels={'Date': 'Date', 'Close': 'Closing Price', 'Ticker': 'Company'},
              title='Stock Perfromance 2013-2018 fig.2')

# Display the chart using st.plotly_chart
st.plotly_chart(fig)

def fetch_data(ticker):
    data = yf.download(ticker, start=start_date, end=end_date)
    data['MA12'] = data['Close'].rolling(window=12).mean()
    data['MA24'] = data['Close'].rolling(window=24).mean()
    return data

# Fetch and resample data for each ticker
df_list = [fetch_data(ticker) for ticker in tickers]

# Concatenate data for all tickers
df = pd.concat(df_list, keys=tickers, names=['Ticker', 'Date']).reset_index()

# Drop 'Volume' column
df = df.drop('Volume', axis=1)

# Group by 'Ticker' and plot each moving average chart
for ticker, group in df.groupby('Ticker'):
    fig = px.line(group, x='Date', y=['Close', 'MA12', 'MA24'], 
                  title=f"{ticker} Moving Averages")
    # Display the chart using st.plotly_chart
    st.plotly_chart(fig)

def fetch_data(ticker):
    data = yf.download(ticker, start=start_date, end=end_date)
    data['Volatility'] = data['Close'].pct_change().rolling(window=10).std()
    return data

# Fetch data and calculate volatility for each ticker
df_list = [fetch_data(ticker) for ticker in tickers]

# Concatenate data for all tickers
df = pd.concat(df_list, keys=tickers, names=['Ticker', 'Date']).reset_index()

# Drop 'Volume' column
df = df.drop('Volume', axis=1)

# Create the Plotly figure
fig = px.line(df, x='Date', y='Volatility', 
              color='Ticker', 
              title='Volatility of All Companies')

# Display the chart using st.plotly_chart
st.plotly_chart(fig)



st.title('Stock Market Analysis by Industry')

# Create date range selection widgets
start_date = st.date_input("Start Date", datetime(2013, 1, 1))
end_date = st.date_input("End Date", datetime(2018, 1, 1))

tickers = ['AAPL', 'MSFT', 'JPM', 'V', 'CVX', 'XOM']

# Function to fetch data and resample
def fetch_data(ticker):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

# Fetch data for Apple and Microsoft
df_list = [fetch_data(ticker) for ticker in ['AAPL', 'MSFT']]

# Concatenate data for Apple and Microsoft
df = pd.concat(df_list, keys=['AAPL', 'MSFT'], names=['Ticker', 'Date']).reset_index()

# Drop 'Volume' column
df = df.drop('Volume', axis=1)

# Create a DataFrame with the stock prices of Apple and Microsoft
apple = df.loc[df['Ticker'] == 'AAPL', ['Date', 'Close']].rename(columns={'Close': 'AAPL'})
microsoft = df.loc[df['Ticker'] == 'MSFT', ['Date', 'Close']].rename(columns={'Close': 'MSFT'})
df_corr = pd.merge(apple, microsoft, on='Date')

# Calculate the correlation matrix
corr_matrix = df_corr[['AAPL', 'MSFT']].corr()

# Create the Plotly scatter plot
fig = px.scatter(df_corr, x='AAPL', y='MSFT', 
                 trendline='ols', 
                 title='Correlation between Apple and Microsoft')

# Display the correlation matrix
st.write("Correlation Matrix:")
st.dataframe(corr_matrix)

# Display the chart using st.plotly_chart
st.plotly_chart(fig)

# Function to fetch data and resample
def fetch_data(ticker):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

# Fetch data for JPM and V
df_list = [fetch_data(ticker) for ticker in ['JPM', 'V']]

# Concatenate data for JPM and V
df = pd.concat(df_list, keys=['JPM', 'V'], names=['Ticker', 'Date']).reset_index()

# Drop 'Volume' column
df = df.drop('Volume', axis=1)

# Create a DataFrame with the stock prices of JPM and V
jpm = df.loc[df['Ticker'] == 'JPM', ['Date', 'Close']].rename(columns={'Close': 'JPM'})
v = df.loc[df['Ticker'] == 'V', ['Date', 'Close']].rename(columns={'Close': 'V'})

# Merge the stock price DataFrames
df_corr = pd.merge(jpm, v, on='Date')

# Calculate the correlation matrix
corr_matrix = df_corr[['JPM', 'V']].corr()

# Create the Plotly scatter plot
fig = px.scatter(df_corr, x='JPM', y='V',
                 trendline='ols',
                 title='Correlation between JPM and V stocks')

# Display the correlation matrix
st.write("Correlation Matrix:")
st.write(corr_matrix)

# Display the chart using st.plotly_chart
st.plotly_chart(fig)


# Function to fetch data and resample
def fetch_data(ticker):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

# Fetch data for Chevron and Exxon Mobil
df_list = [fetch_data(ticker) for ticker in ['CVX', 'XOM']]

# Concatenate data for Chevron and Exxon Mobil
df = pd.concat(df_list, keys=['CVX', 'XOM'], names=['Ticker', 'Date']).reset_index()

# Drop 'Volume' column
df = df.drop('Volume', axis=1)

# Create a DataFrame with the stock prices of Chevron and Exxon Mobil
chevron = df.loc[df['Ticker'] == 'CVX', ['Date', 'Close']].rename(columns={'Close': 'CVX'})
exxon = df.loc[df['Ticker'] == 'XOM', ['Date', 'Close']].rename(columns={'Close': 'XOM'})

# Merge the stock price DataFrames
df_corr = pd.merge(chevron, exxon, on='Date')

# Calculate the correlation matrix
corr_matrix = df_corr[['CVX', 'XOM']].corr()

# Create the Plotly scatter plot
fig = px.scatter(df_corr, x='CVX', y='XOM',
                 trendline='ols',
                 title='Correlation between Chevron and Exxon Mobil stocks')

# Display the correlation matrix
st.write("Correlation Matrix:")
st.write(corr_matrix)

# Display the chart using st.plotly_chart
st.plotly_chart(fig)



import plotly.graph_objects as go

# Create date range selection widgets
start_date = st.date_input("Start Date", datetime(2013, 1, 1), key="start_date")
end_date = st.date_input("End Date", datetime(2018, 1, 1), key="end_date")

tickers = ['AAPL', 'MSFT', 'JPM', 'V', 'CVX', 'XOM']

# Function to fetch data and resample
def fetch_data(ticker):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

# Fetch data for each industry
tech_data = [fetch_data(ticker) for ticker in ['AAPL', 'MSFT']]
finance_data = [fetch_data(ticker) for ticker in ['JPM', 'V']]
energy_data = [fetch_data(ticker) for ticker in ['XOM', 'CVX']]

# Merge data for each industry
tech = pd.merge(tech_data[0], tech_data[1], on='Date').rename(columns={'Close_x': 'Tech - Apple', 'Close_y': 'Tech - Microsoft'})
finance = pd.merge(finance_data[0], finance_data[1], on='Date').rename(columns={'Close_x': 'Finance - JPMorgan', 'Close_y': 'Finance - Visa'})
energy = pd.merge(energy_data[0], energy_data[1], on='Date').rename(columns={'Close_x': 'Energy - Exxon Mobil', 'Close_y': 'Energy - Chevron'})

# Merge all industry DataFrames
merged_df = pd.merge(tech, finance, on='Date')
merged_df = pd.merge(merged_df, energy, on='Date')

# Add 'Date' column back to the DataFrame
merged_df['Date'] = tech_data[0].index

# Create the Plotly figure
fig = go.Figure()

fig.add_trace(go.Scatter(x=merged_df['Date'], y=merged_df['Tech - Apple'], name='Tech'))
fig.add_trace(go.Scatter(x=merged_df['Date'], y=merged_df['Finance - JPMorgan'], name='Finance'))
fig.add_trace(go.Scatter(x=merged_df['Date'], y=merged_df['Energy - Exxon Mobil'], name='Energy'))

fig.update_layout(title='Comparison of Stock Prices by Industry',
                  xaxis_title='Date',
                  yaxis_title='Stock Price')

# Display the chart using st.plotly_chart
st.plotly_chart(fig)



# Create date range selection widgets with unique keys
start_date = st.date_input("Start Date", datetime(2013, 1, 1), key="start_date_input")
end_date = st.date_input("End Date", datetime(2018, 1, 1), key="end_date_input")

tickers = ['AAPL', 'MSFT', 'JPM', 'V', 'CVX', 'XOM']

# Function to fetch data and resample
def fetch_data(ticker):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

# Fetch data for each industry
tech_data = [fetch_data(ticker) for ticker in ['AAPL', 'MSFT']]
finance_data = [fetch_data(ticker) for ticker in ['JPM', 'V']]
energy_data = [fetch_data(ticker) for ticker in ['XOM', 'CVX']]

# Merge data for each industry
tech = pd.merge(tech_data[0], tech_data[1], on='Date').rename(columns={'Close_x': 'Tech - Apple', 'Close_y': 'Tech - Microsoft'})
finance = pd.merge(finance_data[0], finance_data[1], on='Date').rename(columns={'Close_x': 'Finance - JPMorgan', 'Close_y': 'Finance - Visa'})
energy = pd.merge(energy_data[0], energy_data[1], on='Date').rename(columns={'Close_x': 'Energy - Exxon Mobil', 'Close_y': 'Energy - Chevron'})

# Merge all industry DataFrames
merged_df = pd.merge(tech, finance, on='Date')
merged_df = pd.merge(merged_df, energy, on='Date')

# Add 'Date' column back to the DataFrame
merged_df['Date'] = tech_data[0].index

# Calculate the correlation matrix
correlation_matrix = merged_df[['Tech - Apple', 'Finance - JPMorgan', 'Energy - Exxon Mobil']].corr()

# Rename the rows and columns of the correlation matrix
correlation_matrix = correlation_matrix.rename(index={'Tech - Apple': 'Tech', 'Finance - JPMorgan': 'Finance', 'Energy - Exxon Mobil': 'Energy'},
                                               columns={'Tech - Apple': 'Tech', 'Finance - JPMorgan': 'Finance', 'Energy - Exxon Mobil': 'Energy'})

# Display the correlation matrix
st.write("Correlation Matrix:")
st.dataframe(correlation_matrix)
