document.querySelectorAll('.sidebar li').forEach(item => {
  item.addEventListener('click', () => {
    document.querySelectorAll('.sidebar li').forEach(el => el.classList.remove('active'));
    item.classList.add('active');
  });
});
