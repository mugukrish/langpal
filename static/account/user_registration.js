const username = document.getElementById('username');
const email = document.getElementById('email');
const password1 = document.getElementById('password1');
const password2 = document.getElementById('password2');
const form = document.getElementById('signup_form');

// console.log(username, email, password1, password2, form.parentElement)

form.addEventListener('submit', e => {
    	e.preventDefault();
        
    	checkInputs();

    });
    

function checkInputs() {
    let success_count = 0
    const usernameValue = username.value.trim();
    const emailValue = email.value.trim();
    const passwordValue = password1.value.trim();
    const password2Value = password2.value.trim();
    
    if(usernameValue === '') {
        setErrorFor(username, 'Username cannot be blank');
    } else if(usernameValue.length<5) {
        setErrorFor(username, 'Username cannot be less than 5 characters')
    } else if(/\s/.test(usernameValue)){
        setErrorFor(username, 'Username should not contain white spaces')
    }
     else {
        success_count+=1
        setSuccessFor(username);
    }
    
    if(emailValue === '') {
        setErrorFor(email, 'Email cannot be blank');
    } else if (!isEmail(emailValue)) {
        setErrorFor(email, 'Not a valid email');
    } else {
        success_count+=1
        setSuccessFor(email);
    }
    
    if(passwordValue === '') {
        setErrorFor(password1, 'Password cannot be blank');
    } else if (password2Value.length<8){
        setErrorFor(password1, 'Password must contain atleast 8 characters')
    } 
    else {
        success_count+=1
        setSuccessFor(password1);
    }
    
    if(password2Value === '') {
        setErrorFor(password2, 'Password2 cannot be blank');
    } else if(passwordValue !== password2Value) {
        setErrorFor(password2, 'Passwords does not match');
    } else{
        success_count+=1
        setSuccessFor(password2);
    }

    if (success_count==4){
        form.submit();
    }

}



function setErrorFor(input, message) {
    const formControl = input.parentElement;
    const select_child = formControl.querySelector('.check_from_js')
    input.className += ' border-red-500';
    select_child.innerText = message;
}

function setSuccessFor(input) {
    const formControl = input.parentElement;
    const select_child = formControl.querySelector('.check_from_js')
    input.classList.remove('border-red-500');
    select_child.innerText = '';
}
    
function isEmail(email) {
    return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}


// const form = document.getElementById('form');
// const username = document.getElementById('username');
// const email = document.getElementById('email');
// const password = document.getElementById('password');
// const password2 = document.getElementById('password2');

// form.addEventListener('submit', e => {
// 	e.preventDefault();
	
// 	checkInputs();
// });

// function checkInputs() {
// 	// trim to remove the whitespaces
// 	const usernameValue = username.value.trim();
// 	const emailValue = email.value.trim();
// 	const passwordValue = password.value.trim();
// 	const password2Value = password2.value.trim();
	
// 	if(usernameValue === '') {
// 		setErrorFor(username, 'Username cannot be blank');
// 	} else {
// 		setSuccessFor(username);
// 	}
	
// 	if(emailValue === '') {
// 		setErrorFor(email, 'Email cannot be blank');
// 	} else if (!isEmail(emailValue)) {
// 		setErrorFor(email, 'Not a valid email');
// 	} else {
// 		setSuccessFor(email);
// 	}
	
// 	if(passwordValue === '') {
// 		setErrorFor(password, 'Password cannot be blank');
// 	} else {
// 		setSuccessFor(password);
// 	}
	
// 	if(password2Value === '') {
// 		setErrorFor(password2, 'Password2 cannot be blank');
// 	} else if(passwordValue !== password2Value) {
// 		setErrorFor(password2, 'Passwords does not match');
// 	} else{
// 		setSuccessFor(password2);
// 	}
// }

// function setErrorFor(input, message) {
// 	const formControl = input.parentElement;
// 	const small = formControl.querySelector('small');
// 	formControl.className = 'form-control error';
// 	small.innerText = message;
// }

// function setSuccessFor(input) {
// 	const formControl = input.parentElement;
// 	formControl.className = 'form-control success';
// }
	
// function isEmail(email) {
// 	return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
// }


