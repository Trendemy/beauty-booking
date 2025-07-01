# Bài tập DevOps: Viết Dockerfile và Docker Compose cho ứng dụng đặt lịch dịch vụ làm đẹp

## Mục tiêu

- Hiểu cấu trúc source code ứng dụng gồm frontend (Node.js) và backend booking-service (Python Flask).
- Viết Dockerfile cho từng service để đóng gói ứng dụng thành container.
- Viết file `docker-compose.yml` để chạy đồng thời các service cùng với PostgreSQL và Redis.
- Triển khai và kiểm thử ứng dụng trên môi trường Docker.

## Phần 1: Tìm hiểu source code

- **Frontend:** Node.js + Express + EJS, cung cấp giao diện web đơn giản cho phép người dùng đặt lịch.
- **Booking service:** Python Flask API, xử lý lưu đặt lịch vào PostgreSQL và cache dữ liệu vào Redis.
- **Database:** PostgreSQL lưu trữ dữ liệu chính.
- **Cache:** Redis dùng để cache thông tin đặt lịch.

## Phần 2: Viết Dockerfile cho từng service

### 2.1. Viết Dockerfile cho booking-service (Python Flask)

Yêu cầu:

- Sử dụng image `python:3.9-slim`.
- Cài đặt các package trong `requirements.txt`.
- Copy toàn bộ source code vào container.
- Expose port `5001`.
- Chạy ứng dụng Flask.

### 2.2. Viết Dockerfile cho frontend (Node.js)

Yêu cầu:

- Sử dụng image `node:18-alpine`.
- Copy `package.json` và `package-lock.json`, chạy `npm install`.
- Copy toàn bộ source code.
- Expose port `5000`.
- Chạy ứng dụng Node.js.

## Phần 3: Viết docker-compose.yml

Yêu cầu:

- Sử dụng image chính thức cho PostgreSQL (phiên bản `14-alpine`).
- Sử dụng image chính thức cho Redis (phiên bản `6.2-alpine`).
- Khai báo service `booking-service` build từ thư mục tương ứng, truyền biến môi trường kết nối tới PostgreSQL và Redis.
- Khai báo service `frontend` build từ thư mục tương ứng, phụ thuộc `booking-service`.
- Map port `5432` cho PostgreSQL, `6379` cho Redis, `5001` cho booking-service, `5000` cho frontend.
- Sử dụng volume để lưu dữ liệu PostgreSQL.

## Phần 4: Tạo file init.sql để tự động tạo bảng khi khởi động PostgreSQL

- Viết file SQL tạo bảng `bookings` nếu chưa tồn tại, hoặc sử dụng file `init.sql` cho sẵn.
- Mount file này vào thư mục `/docker-entrypoint-initdb.d/` trong container postgres để tự động chạy khi khởi tạo database lần đầu.

## Phần 5: Hướng dẫn chạy và kiểm thử

- Chạy lệnh: `docker-compose up --build` để build và chạy toàn bộ ứng dụng.
- Truy cập `http://localhost:5000` trên trình duyệt để kiểm thử giao diện đặt lịch.
- Kiểm tra logs của các container để xác nhận các service hoạt động bình thường.
- Thực hiện đặt lịch và xác nhận dữ liệu được lưu trong PostgreSQL (có thể dùng `psql` hoặc công cụ quản lý DB).

## Phần 6: Yêu cầu báo cáo

- Nộp file Dockerfile cho từng service.
- Nộp file `docker-compose.yml`.
- Mô tả quá trình triển khai và các vấn đề gặp phải (nếu có).
- Gợi ý cải tiến hoặc mở rộng ứng dụng (ví dụ: thêm service mới, thêm cache, sử dụng mạng Docker riêng, ...).

---

# Tài liệu tham khảo

- [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)
- [Docker Compose documentation](https://docs.docker.com/compose/)
- [PostgreSQL Docker image initialization](https://hub.docker.com/_/postgres)
- [Redis Docker image](https://hub.docker.com/_/redis)