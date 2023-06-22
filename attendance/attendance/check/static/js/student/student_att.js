document.addEventListener('DOMContentLoaded', function () {
    const dropdowns = document.querySelectorAll('.dropdown');
  
    dropdowns.forEach((dropdown) => {
      dropdown.addEventListener('click', () => {
        const dropdownMenu = dropdown.querySelector('.dropdown-menu');
        dropdownMenu.style.display = dropdownMenu.style.display === 'none' ? 'block' : 'none';
      });
    });
  
    // 페이지의 다른 부분을 클릭하면 드랍다운 메뉴가 사라지도록 하는 코드
    document.addEventListener('click', (event) => {
      if (!event.target.closest('.dropdown')) {
        dropdowns.forEach((dropdown) => {
          dropdown.querySelector('.dropdown-menu').style.display = 'none';
        });
      }
    });
  });