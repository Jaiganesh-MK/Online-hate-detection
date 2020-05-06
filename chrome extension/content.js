window.onload = (event) =>{

// Sends the text contents of the webpage being viewed to the background script
var port = chrome.runtime.connect({name: "port"});
port.postMessage({contents:document.body.innerText});

port.onMessage.addListener(function(msg){
    
    // data containing offensive words is received from background script
    received_data = msg.result;
    const len = received_data.length;
    for( var i = 0; i<len; i++){

        for(var j=0;j<document.getElementsByTagName("body").length;j++){
            
            var to_hide = new RegExp(received_data[i],"gi");
            // replacing the offensive words with ****
            document.body.innerHTML = document.body.innerHTML.replace(to_hide,'****');
        }
    }
});};

