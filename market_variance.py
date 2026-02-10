import pandas as pd
import numpy as np

def calculate_market_variance(data_payload):
    """
    Analyzes JSON payload from API to detect price anomalies.
    Threshold for alert: 5% variance.
    """
    # Convert JSON payload to DataFrame
    df = pd.DataFrame(data_payload)
    
    # Calculate 7-day moving average
    df['moving_avg'] = df['price'].rolling(window=7).mean()
    
    # Identify variance
    df['variance_pct'] = (df['price'] - df['moving_avg']) / df['moving_avg']
    
    # Filter for significant anomalies (Signal vs Noise)
    anomalies = df[df['variance_pct'].abs() > 0.05]
    
    return anomalies.to_json()
