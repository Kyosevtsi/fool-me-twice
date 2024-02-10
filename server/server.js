const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
const port = 3001; // Or another port of your choice

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Routes 
app.use('/api/items', require('./routes/itemRoutes')); // Example route

app.listen(port, () => console.log(`Server listening on port ${port}`));
