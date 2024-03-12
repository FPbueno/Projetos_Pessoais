let seconds = 0;
let minutes = 0;
let hours = 0;
let interval; 

function start(){
    watch();
    interval = setInterval(watch,1000);
};

function pause(){
    clearInterval(interval);
};

function reset(){
    clearInterval(interval);
    seconds = 0;
    minutes = 0;
    document.getElementById('time').innerText = '00:00:00';
};

function twoDigits(digit){
    if(digit < 10){
        return ('0' + digit);
    }
    else{
        return digit;
    }
}

function watch(){
    seconds++;
    if (seconds == 60){
        minutes++;
        seconds = 0;
        if(minutes == 60){
            hours++;
            minutes = 0;
            seconds = 0;
        }
    }
    document.getElementById('time').innerText = twoDigits(hours) + ':' + twoDigits(minutes) + ':' + twoDigits(seconds);
};