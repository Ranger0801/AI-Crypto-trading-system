import pandas as pd
import pandas_ta as ta

def get_signals(df):
    # Calculate indicators: MACD, RSI, EMA, ATR, VWAP [cite: 2206, 2225]
    df.ta.macd(append=True)
    df.ta.rsi(append=True)
    df.ta.ema(length=200, append=True)
    df.ta.atr(append=True)
    
    score = 0
    reasons = []
    
    # Confluence Scoring [cite: 2338]
    if df['MACD_12_26_9'].iloc[-1] > df['MACDs_12_26_9'].iloc[-1]: 
        score += 2 # [cite: 2338]
        reasons.append("MACD Bullish")
    if df['close'].iloc[-1] > df['EMA_200'].iloc[-1]: 
        score += 1 # [cite: 2338]
        reasons.append("EMA200 Bullish")
        
    # ATR-based Stop Loss [cite: 2208, 2315]
    sl = df['close'].iloc[-1] - (df['ATRr_14'].iloc[-1] * 1.5)
    return score, reasons, sl