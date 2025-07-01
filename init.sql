CREATE TABLE IF NOT EXISTS bookings (
  id SERIAL PRIMARY KEY,
  user_name VARCHAR(100),
  service VARCHAR(100),
  time TIMESTAMP
);
GRANT ALL ON TABLE bookings TO beautyuser;