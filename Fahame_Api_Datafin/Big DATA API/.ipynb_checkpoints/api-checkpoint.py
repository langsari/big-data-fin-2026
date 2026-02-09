from fastapi import FastAPI
import psycopg2

app = FastAPI(
    title="Stock Data API",
    description="API สำหรับดึงข้อมูลราคาหุ้นจาก PostgreSQL",
    version="1.0.0"
)

# -------------------------
# Database Connection
# -------------------------
def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="api_data",  
        user="postgres",
        password="postgres",
        port=5432
    )

# -------------------------
# Health Check
# -------------------------
@app.get("/")
def root():
    return {"status": "API is running"}

# -------------------------
# Get Stock Prices
# -------------------------
@app.get("/stocks")
def get_stocks():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT date, open, high, low, close, volume
        FROM stock_prices
        ORDER BY date
    """)

    rows = cur.fetchall()

    cur.close()
    conn.close()

    data = []
    for r in rows:
        data.append({
            "date": r[0],
            "open": float(r[1]),
            "high": float(r[2]),
            "low": float(r[3]),
            "close": float(r[4]),
            "volume": int(r[5])
        })

    return data