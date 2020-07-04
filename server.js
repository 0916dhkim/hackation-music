const express = require('express');
const cors = require('cors');
const app = express();
app.use(cors());
const router = require('./routes');

// Use environment variable PORT or 3000 if not defined.
const port = process.env.PORT || 3000;

// Serve static contents from static directory.
app.use(express.static('public'));

// Use API endpoint from routes module.
app.use(router);

// Test API endpoint.
app.get('/hello', (req, res) => {
  res.send('Hello, World!');
});

// Start listening for requests.
app.listen(port, () => {
  console.log(`App listening on port ${port}`);
});
