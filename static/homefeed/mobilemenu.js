const menuButton = document.getElementById('menu-button');
const openMenuButton = document.getElementById('menu-open')
const closeMenuButton = document.getElementById('menu-close')
const menu = document.getElementById('menu');
let menu_open = false;

menuButton.addEventListener('click',() =>{
    if (!menu_open){
        menu.classList.remove("hidden");
        openMenuButton.classList.add("hidden")
        closeMenuButton.classList.remove("hidden")
        menu_open=true;
    }else{
        menu.classList.add("hidden");
        openMenuButton.classList.remove("hidden")
        closeMenuButton.classList.add("hidden")
        menu_open=false;
    }
    

})