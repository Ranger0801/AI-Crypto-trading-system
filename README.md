# SignalEdge AI — Crypto Signal Scanner v2.0

An AI-powered multi-market trading signal scanner designed to reduce manual analysis for professional traders.

## 🚀 Features
- [cite_start]**19 Technical Indicators**: Full suite across Trend, Momentum, Volume, Volatility, and Levels[cite: 2202, 2223].
- [cite_start]**Confluence Scoring**: Signals only trigger when multiple indicators align (Score 7+)[cite: 2210, 2344].
- [cite_start]**AI Insights**: Automated trade reasoning and probability analysis[cite: 2197, 2344].
- [cite_start]**Risk Management**: Automated ATR-based Stop Loss and 3-tier Take Profit levels[cite: 2208, 2314].
- [cite_start]**Real-Time Alerts**: Instant delivery via Telegram and Web Dashboard[cite: 2204, 2354].

## 📂 Project Structure
- [cite_start]`/backend`: Flask API for data delivery[cite: 2216].
- [cite_start]`/scanners`: The core engine (Indicator calculation & AI reasoning)[cite: 2216].
- [cite_start]`/database`: PostgreSQL/Supabase manager for trade journaling[cite: 2216, 2352].
- [cite_start]`/scheduler`: Background job controller for 5-minute scans[cite: 2204, 2363].
- [cite_start]`/frontend`: Dark-themed trader dashboard[cite: 2216, 2429].

## 🛠️ Setup & Installation

### 1. Environment Variables
Create a `.env` file in the root directory and add the following:
```env
# Exchange & Data
BINANCE_API_KEY=your_binance_key
BINANCE_SECRET_KEY=your_binance_secret

# Database
DATABASE_URL=your_postgresql_or_supabase_url

# AI Layer (Gemini or Claude)
AI_API_KEY=your_llm_api_key

# Delivery
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id