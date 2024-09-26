document.querySelector('.btn-sign-in').addEventListener('click', function(event) {
    event.preventDefault();
    document.body.classList.add('fade-out');


    setTimeout(function() {
        window.location.href = 'templates/login.html';
    }, 500);
});