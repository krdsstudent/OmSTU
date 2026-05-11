document.getElementById('contactForm').addEventListener('submit', function(e) {
  e.preventDefault();
  alert('Соединение установлено. Мы ответим вам в ближайшее время.');
  this.reset();
});

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    document.querySelector(this.getAttribute('href')).scrollIntoView({
      behavior: 'smooth'
    });
  });
});