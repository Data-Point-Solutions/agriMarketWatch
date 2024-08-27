// agriMarketWatch/node/src/index.js

const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
    res.send('Welcome to the agriMarketWatch Node.js service!');
});

app.get('/status', (req, res) => {
    res.json({ status: 'Node.js service is up and running.' });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});