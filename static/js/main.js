
 const navToggler = document.querySelector(".nav-toggler");
 navToggler.addEventListener("click", navToggle);

 function navToggle() {
    navToggler.classList.toggle("active");
    const nav = document.querySelector(".nav");
    nav.classList.toggle("open");
    if(nav.classList.contains("open")){
    	nav.style.maxHeight = nav.scrollHeight + "px";
    }
    else{
    	nav.removeAttribute("style");
    }
 } 

 export default main

 /*===== LOGIN SHOW and HIDDEN =====*/
const signUp = document.getElementById('sign-up'),
signIn = document.getElementById('sign-in'),
loginIn = document.getElementById('login-in'),
loginUp = document.getElementById('login-up')


signUp.addEventListener('click', ()=>{
// Remove classes first if they exist
loginIn.classList.remove('block')
loginUp.classList.remove('none')

// Add classes
loginIn.classList.toggle('none')
loginUp.classList.toggle('block')
})

signIn.addEventListener('click', ()=>{
// Remove classes first if they exist
loginIn.classList.remove('none')
loginUp.classList.remove('block')

// Add classes
loginIn.classList.toggle('block')
loginUp.classList.toggle('none')
})