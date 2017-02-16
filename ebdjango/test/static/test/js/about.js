
if (window.addEventListener){
    window.addEventListener('load', WindowLoad, false);
} else if (window.attachEvent) {
    window.attachEvent('onload', WindowLoad);
}

function WindowLoad(event) {
    var nyt = $('#nyt');
    var w1 = nyt.clientWidth;
    
}