from flask import Flask, request, jsonify
import psycopg2
import redis
import os

app = Flask(__name__)

# Kết nối PostgreSQL
conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT")
)
cur = conn.cursor()

# Kết nối Redis
cache = redis.Redis(host=os.getenv("REDIS_HOST"), port=6379, db=0)

@app.route('/book', methods=['POST'])
def book_service():
    data = request.json
    user = data.get('user')
    service = data.get('service')
    time = data.get('time')

    # Lưu vào PostgreSQL
    cur.execute("INSERT INTO bookings (user_name, service, time) VALUES (%s, %s, %s) RETURNING id", (user, service, time))
    booking_id = cur.fetchone()[0]
    conn.commit()

    # Cache booking
    cache.set(f"booking:{booking_id}", f"{user} - {service} at {time}")

    return jsonify({"message": "Booking successful", "booking_id": booking_id})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
