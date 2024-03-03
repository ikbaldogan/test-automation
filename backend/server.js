const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const fs = require('fs');
const app = express();
const PORT = 3000;


app.use(cors());
app.use(bodyParser.json());


const testUsers = JSON.parse(fs.readFileSync('testUsers.json'));

app.post('/login', (req, res) => {
    const { email, password } = req.body;
    
    const user = testUsers.find(user => user.email === email && user.password === password);
    if (user) {
        res.json({ success: true });
    } else {
        res.status(401).json({ success: false });
    }
});




app.listen(PORT, () => console.log(`Server is running on http://localhost:${PORT}`));
