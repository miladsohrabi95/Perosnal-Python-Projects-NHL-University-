import requests
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import time

# Fetching the real-time prices
def fetch_bitcoin_price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data['bitcoin']['usd']

# Updating and plotting 
def update_plot(fig, x_data, y_data):
    # Current price are fetched
    price = fetch_bitcoin_price()
    
    # New prices are appended
    x_data.append(time.strftime('%H:%M:%S'))
    y_data.append(price)
    
    # Update plot 
    fig.data[0].x = x_data
    fig.data[0].y = y_data
    
    # Update plot layout
    fig.update_layout(title='Real-time Bitcoin Price Tracker', xaxis_title='Time', yaxis_title='Price (USD)')

# Main function
def main():
    # Initialize plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[], y=[], mode='lines', name='Bitcoin Price'))
    
    # subplots with shared x-axis
    fig.update_layout(title='Real-time Bitcoin Price Tracker', xaxis_title='Time', yaxis_title='Price (USD)')
    
    # Initialize data lists
    x_data = []
    y_data = []
    
    # data will be plotted every 30 secs
    interval = 30
    
    # Plot+update Bitcoin price in real-time
    while True:
        update_plot(fig, x_data, y_data)
        fig.show()
        
        # it shouldn't go forever!
        user_input = input("Enter 'update' to continue or 'exit' to quit: ")
        if user_input.lower() == 'exit':
            break
        time.sleep(interval)

if __name__ == "__main__":
    main()
