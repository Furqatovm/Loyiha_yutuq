

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
