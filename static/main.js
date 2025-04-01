

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
    if(timeLeft < 6){
        document.getElementById("second").style.color ="red";
    }
    if (timeLeft <= 0){
        clearInterval(timer);
        window.location.href ="/result"

    }
}, 1000);

function endQuiz(){
    clearInterval(timer)
    window.location.href ="/result";
}

let suggestion =document.querySelectorAll(".suggestion");

let ochko =document.querySelectorAll(".achko");

if (ochko > 8 && ochko < 10){
    suggestion.textContent ="Siz haqiqiy A1 o'quvchi";
} 
else if(ochko > 6 && ochko < 8){
    suggestion.textContent ="siz o'rtacha ekansiz";

}
else if (ochko > 5 && ochko < 6){
    suggestion.textContent ="siz qattiq harakat qiling";
}
else{
    suggestion.textContent ="siz 0 ekansiz"
}

