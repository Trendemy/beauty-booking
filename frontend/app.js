const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');
const path = require('path');

const app = express();

// Cấu hình thư mục chứa views
app.set('views', path.join(__dirname, 'views'));
// Cấu hình template engine là EJS
app.set('view engine', 'ejs');

// Middleware để xử lý form data
app.use(bodyParser.urlencoded({ extended: true }));

// Route hiển thị form đặt lịch
app.get('/', (req, res) => {
  res.render('index');  // sẽ tìm file views/index.ejs
});

// Route xử lý submit form
app.post('/book', async (req, res) => {
  const { user, service, time } = req.body;

  try {
    const response = await axios.post('http://booking-service:5001/book', {
      user,
      service,
      time
    });
    if (response.status === 200) {
      // Redirect kèm query param báo thành công
      res.redirect('/?status=success');
    } else {
      // Redirect kèm query param báo thất bại
      res.redirect('/?status=fail');
    }
  } catch (error) {
    res.redirect('/?status=fail');
  }
});

const PORT = 5000;
app.listen(PORT, () => {
  console.log(`Frontend running on port ${PORT}`);
});
