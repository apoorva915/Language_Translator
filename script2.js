// your_script2.js
fetch('server.py')
    .then(response => response.json())
    .then(data => {
        // Process the data and render it in the browser
        console.log(data);
    })
    .catch(error => console.error('Error:', error));
