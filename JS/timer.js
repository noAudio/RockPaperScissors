var time = document.getElementById('timer')
var timeLeft = 4;

var run = setInterval(function() {
    if(timeLeft <= -1){
        clearInterval(run);
        
        /* There should be a function call to pick randomly for player when timer finish */
        /* There should also be a function call to update score */
        
    } else {
        time.innerHTML = '00:0' + timeLeft + "s";
    }
    timeLeft -=1;
}, 1000);



/* There should be an if statement that picks for computer whenever player chooses his card */
