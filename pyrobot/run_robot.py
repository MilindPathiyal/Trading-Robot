import time as true_time
import pprint
import pathlib
import operator

import pandas as pd
from datetime import datetime
from datetime import timedelta
from configparser import ConfigParser

from indicators import Indicators
from portfolio import Portfolio
from robot import PyRobot


# Grab values from config file
config = ConfigParser()
config.read('config/config.ini')

CLIENT_ID = 'FAKE'
REDIRECT_URI = 'FAKE'
CREDENTIALS_PATH = "FAKE"
ACCOUNT_NUMBER = 'FAKE'

'''
CLIENT_ID = config.get('main', 'CLIENT_ID')
REDIRECT_URI = config.get('main', 'REDIRECT_URL')
CREDENTIALS_PATH = config.get('main', 'JSON_PATH')
ACCOUNT_NUMBER = config.get('main', 'ACCOUNT_NUMBER')
'''

# Initialize the robot
trading_robot = PyRobot(
    client_id=CLIENT_ID,
    redirect_uri=REDIRECT_URI,
    credentials_path=CREDENTIALS_PATH,
    paper_trading=True
)

# Create new portfolio
trading_robot_portfolio = trading_robot.create_portfolio()

# Add multiple positions to our portfolio
multi_position = [ 
    {
        'asset_type': 'equity',
        'quantity': 2,
        'purchase_price': 4.00,
        'symbol': 'SQ',
        'purchase_date': '2022-09-01'
    },
    {
        'asset_type': 'equity',
        'quantity': 2,
        'purchase_price': 4.00,
        'symbol': 'SQ',
        'purchase_date': '2022-09-01'
    }
]


# Add positions to the portfolio
new_positions = trading_robot.portfolio.add_positions(positions=multi_position)
pprint.pprint(new_positions)

# Add a single position to the portfolio
trading_robot.portfolio.add_position(
    symbol='MSFT',
    quantity=10,
    purchase_price=10.00,
    asset_type='equity',
    purchase_date='2022-09-01'
)

pprint.pprint(trading_robot.portfolio.positions)

if trading_robot.regular_market_open:
    print('Regular Market Open')
else:
    print('Regular Market Not Open')
    
current_quotes = trading_robot.grab_current_quotes()
pprint.pprint(current_quotes)