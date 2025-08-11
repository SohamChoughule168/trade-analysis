#!/usr/bin/env python3
"""analysis_script.py
Script version of the notebook. Usage:
python analysis_script.py --trader data/hyperliquid_historical.csv --sentiment data/fear_greed_index.csv
"""
import argparse
import pandas as pd
import numpy as np
from pathlib import Path

def load_data(trader_path, sentiment_path):
    print('Loading trader data from', trader_path)
    trader = pd.read_csv(trader_path, parse_dates=['time'], low_memory=False)
    print('Loading sentiment data from', sentiment_path)
    sent = pd.read_csv(sentiment_path, parse_dates=['Date'], low_memory=False)
    return trader, sent

def preprocess_trader(trader):
    # lowercase cols
    trader.columns = [c.strip().lower().replace(' ', '_') for c in trader.columns]
    # ensure time column exists
    if 'time' in trader.columns:
        trader['date'] = pd.to_datetime(trader['time']).dt.date
    elif 'timestamp' in trader.columns:
        trader['date'] = pd.to_datetime(trader['timestamp']).dt.date
    else:
        raise ValueError('No time/timestamp column found in trader data')
    # convert numeric columns
    for col in ['closedpnl','size','leverage','execution_price']:
        if col in trader.columns:
            trader[col] = pd.to_numeric(trader[col], errors='coerce')
    return trader

def aggregate_by_date_account(trader):
    # Basic aggregations per account per date
    ag = trader.groupby(['date','account']).agg(
        trades_count = ('account','size'),
        total_pnl = ('closedpnl','sum'),
        avg_pnl = ('closedpnl','mean'),
        win_rate = (lambda x: (x['closedpnl']>0).sum()/len(x) if len(x)>0 else np.nan),
    ).reset_index()
    # Note: the lambda in groupby agg may not work depending on pandas version; see notebook for robust version.
    return ag

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--trader', required=True)
    p.add_argument('--sentiment', required=True)
    args = p.parse_args()
    trader, sent = load_data(args.trader, args.sentiment)
    trader = preprocess_trader(trader)
    print('Sample trader rows:', trader.shape)
    # Save a small sample for quick inspection
    trader.head(5).to_csv('trader_sample_head.csv', index=False)
    print('Done. For full analysis use the notebook which contains visualization and tests.')

if __name__ == '__main__':
    main()
