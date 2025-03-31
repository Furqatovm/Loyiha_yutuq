

let openn =document.getElementById("open");
let closee =document.getElementById("close");

let navv =document.getElementById("navv");

openn.addEventListener("click", function(){
    navv.style.display ="flex";
    navv.style.position ="fixed";
    closee.style.display ="block";
})


closee.addEventListener("click", function(){
    navv.style.display ="none";
})


let none =document.getElementById("main");

let timeLeft =15;
let timer =setInterval(() =>{
    timeLeft--;
    document.getElementById("second").textContent =timeLeft;

    if (timeLeft <= 0){
        clearInterval(timer);
        window.location.href ="/result"

    }
}, 1000);

function endQuiz(){
    clearInterval(timer)
    window.location.href ="/result";
}