

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



document.addEventListener("DOMContentLoaded", function () {
    let suggestion = document.getElementById("scoree");
    let ochkoElement = document.getElementById("ochko");

    if (ochkoElement) {
        let ochko = parseFloat(ochkoElement.textContent.replace("Score: ", "").trim());

        if (ochko >= 8 && ochko <= 10) {
            suggestion.textContent = "Darajangiz A1";
        } 
        else if (ochko >= 6 && ochko < 8) {
            suggestion.textContent = "Starter";
        }
        else if (ochko >= 5 && ochko < 6) {
            suggestion.textContent = "Darajangiz 0";
        }
        else {
            suggestion.textContent = "Siz 0 ekansiz";
        }

        // Agar ochko 8 bo‘lsa, <p> ni ham o‘zgartiramiz
        let paragraph = document.querySelector(".info-text");
        if (paragraph && ochko === 8) {
            paragraph.textContent = suggestion.textContent;
        }
    }
});
