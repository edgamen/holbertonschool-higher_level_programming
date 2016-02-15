var https = require('https');

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
	'User-Agent': 'Holberton_School',
	'Authorization': 'token a635ae0fd8b0451c6845400566face4e4329605b'
    }
}

var req = https.request (options, function(res) {
	streamToString(res,closure);  
});
req.end();

req.on('error', function(e) {
	console.error(e);
    });


function streamToString(stream, cb) {
    const chunks = [];
    stream.on('data', (chunk) => {
	    chunks.push(chunk);
	});
    stream.on('end', () => {
	    cb(chunks.join(''));
	});
}
var closure = function(jsonString){
    var fs = require('fs');
    fs.writeFile('/tmp/18', jsonString, function (err) {
	if (err) return console.log(err);
	console.log('The file was saved!'); 
    });
};


