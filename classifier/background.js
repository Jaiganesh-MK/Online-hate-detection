chrome.runtime.onConnect.addListener(function(port){
    console.assert(port.name == "port");
    // receives the message from content.js
    port.onMessage.addListener(function(msg){
        var data = msg.contents;
        var xhttp = new XMLHttpRequest();
        // created ajax request to the flask server 
        xhttp.open('POST','http://127.0.0.1:5000//_get_data/');

        xhttp.onload = () => {
            const r = JSON.parse(xhttp.responseText);
            // received data containing offensive words is sent back to content script
            port.postMessage({result:r.rate});
            console.log("here");
        };
        // sends the data to the flask server
        const mydata = new FormData();
        mydata.append('data', data);
        xhttp.send(mydata);
    
    })
});






