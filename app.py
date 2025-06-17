// server.js
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('express').json;
const app = express();
const PORT = 3000;

// Middleware
app.use(bodyParser());

// MongoDB Connection
mongoose.connect('mongodb://localhost:27017/todoDB', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});
const db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));
db.once('open', () => console.log('Connected to MongoDB'));

// Mongoose Schema
const ToDoItem = mongoose.model('ToDoItem', new mongoose.Schema({
  itemName: String,
  itemDescription: String,
}));

// POST /submittodoitem route
app.post('/submittodoitem', async (req, res) => {
  const { itemName, itemDescription } = req.body;

  if (!itemName || !itemDescription) {
    return res.status(400).json({ error: 'Both itemName and itemDescription are required.' });
  }

  try {
    const newItem = new ToDoItem({ itemName, itemDescription });
    await newItem.save();
    res.status(201).json({ message: 'To-Do item saved successfully.' });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Failed to save item to the database.' });
  }
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
