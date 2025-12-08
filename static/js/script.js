// Apply Bootstrap classes to signup form input fields
const signupForm = document.getElementById('signup_form');
if (signupForm) {
    const inputFields = signupForm.querySelectorAll('input[type="text"], input[type="email"], input[type="password"]');
    inputFields.forEach(field => {
        field.classList.add('form-control', 'my-2');
    });
}

// Apply Bootstrap classes to login form input fields
const loginForm = document.getElementById('login_form');
if (loginForm) {
    const inputFields = loginForm.querySelectorAll('input[type="text"], input[type="password"]');
    inputFields.forEach(field => {
        field.classList.add('form-control', 'my-2');
    });
}

// Style error messages with Bootstrap alert classes in signup and login forms
const errorlist = document.querySelectorAll('.errorlist');
errorlist.forEach(list => {
    list.classList.add('alert', 'alert-danger', 'mb-2');
});

// Resource form validation and URL label styling
const resourceForm = document.getElementById('resource_form');
if (resourceForm) {
    const urlLabel = resourceForm.querySelector('label[for="id_url"]');
    urlLabel.style.textTransform = 'uppercase';
    resourceForm.addEventListener('submit', e => {
        e.preventDefault();
        const nameField = resourceForm.querySelector('input[name="name"]');
        if (nameField.value.trim() === '') {
            alert('Resource name cannot be empty.');
            nameField.value = '';
            nameField.focus();
            return;
        } else if (nameField.value.length > 200) {
            alert('Resource name cannot exceed 200 characters.');
            nameField.focus();
            return;
        }
        resourceForm.submit();
    });
}

// Category form validation
const categoryForm = document.getElementById('category_form');
if (categoryForm) {
    categoryForm.addEventListener('submit', e => {
        e.preventDefault();
        const nameField = categoryForm.querySelector('input[name="name"]');
        if (nameField.value.trim() === '') {
            alert('Category name cannot be empty.');
            nameField.value = '';
            nameField.focus();
            return;
        } else if (nameField.value.length > 100) {
            alert('Category name cannot exceed 100 characters.');
            nameField.focus();
            return;
        }
        categoryForm.submit();
    });
}

// Set the selected option in the sort_by dropdown based on URL parameter
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

// Contact form validation
const contactForm = document.querySelector('#contact_form');
if (contactForm) {
    contactForm.addEventListener('submit', e => {
        e.preventDefault();
        const nameField = contactForm.querySelector('input[name="name"]');
        if (nameField.value.trim() === '') {
            alert('Name cannot be empty.');
            nameField.value = '';
            nameField.focus();
            return;
        } else if (nameField.value.length > 200) {  
            alert('Name cannot exceed 200 characters.');
            nameField.focus();
            return;
        }
        const messageField = contactForm.querySelector('textarea[name="message"]');
        if (messageField.value.trim() === '') {
            alert('Message cannot be empty.');
            messageField.value = '';
            messageField.focus();
            return;
        }
    });
}