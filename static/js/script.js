const signupForm = document.getElementById('signup_form');
if (signupForm) {
    const inputFields = signupForm.querySelectorAll('input[type="text"], input[type="email"], input[type="password"]');
    inputFields.forEach(field => {
        field.classList.add('form-control', 'my-2');
    });
}

const loginForm = document.getElementById('login_form');
if (loginForm) {
    const inputFields = loginForm.querySelectorAll('input[type="text"], input[type="password"]');
    inputFields.forEach(field => {
        field.classList.add('form-control', 'my-2');
    });
}