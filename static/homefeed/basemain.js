const practicebtn = document.getElementById('button-practice')
const practice_mobilebtn = document.getElementById('button-practice-mobile')
const practice_closebtn = document.getElementById('close-practice')

const popup = document.getElementById('dropdown-practice')
const overlay_back = document.getElementById('overlay-back')


practicebtn.addEventListener('click', (e) =>{

    popup.classList.remove('hidden');
    overlay_back.classList.remove('hidden');
    console.log("mobile menu")
    
})

practice_closebtn.addEventListener('click', (e) =>{

    popup.classList.add('hidden');
    overlay_back.classList.add('hidden');
    
})

practice_mobilebtn.addEventListener('click', (e) =>{
    popup.classList.remove('hidden');
    overlay_back.classList.remove('hidden');
    console.log("mobile menu")
})