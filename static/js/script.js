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

const sortBySelect = document.querySelector('#sort_by');
if (sortBySelect) {
    const selectOptions = sortBySelect.querySelectorAll('option');
    let queryString = window.location.search;
    let urlParams = new URLSearchParams(queryString);
    let currentSort = urlParams.get('sort_by') || 'alphabetical';
    selectOptions.forEach(option => {
        if (option.value === currentSort) {
            option.selected = true;
        } else {
            option.selected = false;
        }
    });
}