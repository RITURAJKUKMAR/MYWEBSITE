
let minBox= document.getElementById('show-min');

let min = (((Number(minBox.innerText))*10)/60).toFixed(0);
minBox.innerText=min;
let sec = 0;
let st = 0;
let t = setInterval(() => {
    sec--;
    if (st == 0) {
        alert("Start Test");
        st = 1;
    }
    if (sec == -1) {
        if (min == 0 && sec == -1) {
            sec--;
            let sub = document.getElementById("sub");
            sub.click();
            alert("TIME OVER");
            clearTimeout(t);
            scoreboard();
            sec = 0;
            min = 0;
        }
        else {
            min--;
            sec = 59;
        }
    }
    document.getElementById('show-min').innerHTML = min;
    document.getElementById('show-colon').innerHTML = ":";
    document.getElementById('show-sec').innerHTML = sec;
}, 1000);
