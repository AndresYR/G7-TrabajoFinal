const hamburger = document.getElementById('hamburger');
const navbar = document.getElementById('navbar');
const closeMenuButton = document.getElementById('close-menu');


hamburger.addEventListener('click', () => {
  navbar.classList.toggle('active');
});


closeMenuButton.addEventListener('click', () => {
    navbar.classList.remove('active');
});