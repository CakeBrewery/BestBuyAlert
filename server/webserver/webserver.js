var http = require('http'),
    express = require('express'),
    bodyParser = require('body-parser');


// Create HTTP server
var app = express();

app.use("/", express.static(__dirname));

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// POST from index.html
app.post('/', function(request, response) {
    // Responds to web server request
    response.send('ok');

    // Send POST request to Django at localhost:8000
    var body = JSON.stringify({
        sku: request.body.sku,
        price: request.body.price
    })

    var options = {
        hostname: "localhost",
        port: 8000,
        path: "/requests/",
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Content-Length": Buffer.byteLength(body)
        }
    };

    var req = http.request(options, function(res) {
        res.setEncoding('utf8');

        // Prints out response
        res.on('data', function (chunk) {
            console.log(chunk);
        });
    });

    req.write(body);
    req.end();

    console.log(res);

});

app.listen(8080); //the port you want to use