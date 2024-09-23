import os
from datetime import datetime, timedelta

from alpaca.data.historical import (CryptoHistoricalDataClient,
                                    StockHistoricalDataClient)
from alpaca.data.requests import (CryptoLatestQuoteRequest,
                                  StockLatestQuoteRequest)
from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.requests import MarketOrderRequest
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Get API keys from environment variables
api_key = os.getenv('ALPACA_API_KEY')
secret_key = os.getenv('ALPACA_SECRET_KEY')

# SetUp clients
stock_data_client = StockHistoricalDataClient(api_key, secret_key)
crypto_data_client = CryptoHistoricalDataClient(api_key, secret_key)
trading_client = TradingClient(api_key, secret_key, paper=True)

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/account_info')
def account_info():
    """Fetch and return account information"""
    account = trading_client.get_account()
    return jsonify({
        'buying_power': account.buying_power,
        'cash': account.cash,
        'portfolio_value': account.portfolio_value
    })

@app.route('/orders')
def get_orders():
    """Fetch and return all orders"""
    orders = trading_client.get_orders()
    return jsonify([order.dict() for order in orders])

@app.route('/positions')
def get_positions():
    """Fetch and return all positions"""
    positions = trading_client.get_all_positions()
    return jsonify([position.dict() for position in positions])

@app.route('/submit_order', methods=['POST'])
def submit_order():
    """Submit a market order"""
    data = request.json
    market_order_data = MarketOrderRequest(
        symbol=data['symbol'],
        qty=float(data['quantity']),
        side=OrderSide.BUY if data['side'] == 'buy' else OrderSide.SELL,
        time_in_force=TimeInForce.DAY
    )
    market_order = trading_client.submit_order(order_data=market_order_data)
    return jsonify(market_order.dict())

@app.route('/cancel_order/<order_id>', methods=['POST'])
def cancel_order(order_id):
    """Cancel a specific order"""
    try:
        cancel_status = trading_client.cancel_order_by_id(order_id=order_id)
        return jsonify({'status': 'success', 'message': 'Order cancelled successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/real_time_data')
def get_real_time_data():
    """Fetch real-time stock and crypto data"""
    stock_symbols = ["SPY", "MSFT", "AAPL", "AMZN"]
    crypto_symbols = ["BTC/USD", "ETH/USD", "SOL/USD", "DOGE/USD", "BNB/USD"]
    
    # Fetch stock data
    stock_request = StockLatestQuoteRequest(symbol_or_symbols=stock_symbols)
    stock_quotes = stock_data_client.get_stock_latest_quote(stock_request)
    
    # Fetch crypto data
    crypto_request = CryptoLatestQuoteRequest(symbol_or_symbols=crypto_symbols)
    crypto_quotes = crypto_data_client.get_crypto_latest_quote(crypto_request)
    
    return jsonify({
        'stocks': {symbol: quote.dict() for symbol, quote in stock_quotes.items()},
        'crypto': {symbol: quote.dict() for symbol, quote in crypto_quotes.items()}
    })

if __name__ == '__main__':
    app.run(debug=True)