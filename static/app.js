// app.js
window.addEventListener('scroll', () => {
  const whatsappButton = document.getElementById('whatsapp-button');

  if (whatsappButton) {
    if (window.scrollY > 200) {
      whatsappButton.classList.add('scrolled');
    } else {
      whatsappButton.classList.remove('scrolled');
    }
  }
});
