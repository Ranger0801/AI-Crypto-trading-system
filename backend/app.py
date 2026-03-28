from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/api/signals', methods=['GET'])
def get_signals():
    # In production, this fetches from the 'signals' table 
    return jsonify({"status": "success", "message": "Latest signals endpoint"})

@app.route('/api/market_summary', methods=['GET'])
def market_summary():
    return jsonify({
        "btc_trend": "BEARISH", # [cite: 5, 596, 1155, 1680]
        "market_cap": "$2.44T", # [cite: 17, 597, 1156, 1681]
        "btc_dominance": "56.5%" # [cite: 18, 598, 1157, 1682]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))