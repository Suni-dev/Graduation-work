
      document.addEventListener('DOMContentLoaded', function () {
    const dropdowns = document.querySelectorAll('.dropdown');
  
    dropdowns.forEach((dropdown) => {
      dropdown.addEventListener('mouseenter', () => {
        dropdown.querySelector('.dropdown-menu').style.display = 'block';
      });
  
      dropdown.addEventListener('mouseleave', () => {
        dropdown.querySelector('.dropdown-menu').style.display = 'none';
      });
    });
  });
    const chartData1 = {
      labels: ['2023-04-01', '2023-04-08', '2023-04-15', '2023-04-22', '2023-04-29'],
      datasets: [
        {
          label: '강의1 출석 현황',
          data: [1, 0, -1, 1, 1],
          backgroundColor: ['#4BC0C0', '#4BC0C0', '#FF6384', '#4BC0C0', '#4BC0C0'],
          borderWidth: 1
        },
      ],
    };
  
    const chartData2 = {
      labels: ['2023-04-02', '2023-04-09', '2023-04-16', '2023-04-23', '2023-04-30'],
      datasets: [
        {
          label: '강의2 출석 현황',
          data: [1, 1, -1, 1, 1],
          backgroundColor: ['#4BC0C0', '#4BC0C0', '#FF6384', '#4BC0C0', '#4BC0C0'],
          borderWidth: 1
        },
      ],
    };
  
    const chartData3 = {
      labels: ['2023-04-03', '2023-04-10', '2023-04-17', '2023-04-24', '2023-05-01'],
      datasets: [
        {
          label: '강의3 출석 현황',
          data: [1, 1, 1, 1, 1],
          backgroundColor: ['#4BC0C0', '#4BC0C0', '#4BC0C0', '#4BC0C0', '#4BC0C0'],
          borderWidth: 1
        },
      ],
    };
  
    const config1 = {
      type: 'bar',
      data: chartData1,
      options: {
        indexAxis: 'x',
        scales: {
          y: {
            max: 1,
            min: -1,
          },
        },
      },
    };
  
    const config2 = {
      type: 'bar',
      data: chartData2,
      options: {
        indexAxis: 'x',
        scales: {
          y: {
            max: 1,
            min: -1,
          },
        },
      },
    };
  
    const config3 = {
      type: 'bar',
      data: chartData3,
      options: {
        indexAxis: 'x',
        scales: {
          y: {
            max: 1,
            min: -1,
          },
        },
      },
    };
  
    const chart1 = new Chart(document.getElementById('attendance-chart-1'), config1);
    const chart2 = new Chart(document.getElementById('attendance-chart-2'), config2);
    const chart3 = new Chart(document.getElementById('attendance-chart-3'), config3);

    const logoutBtn = document.querySelector('.logout-btn');
logoutBtn.addEventListener('click', function() {
  // 서버에 로그아웃 요청을 보내는 코드를 여기에 작성하세요.
  // 예: fetch('/logout', { method: 'POST' }) 와 같이 서버에 로그아웃 요청을 보냅니다.
  fetch('/logout', { method: 'POST' })
    .then(response => {
      if (response.ok) {
        // 로그아웃 처리가 완료되면 로그인 페이지로 이동합니다.
        window.location.href = 'templates/check/student';
      } else {
        throw new Error(`로그아웃 요청 실패: ${response.status}`);
      }
    })
    .catch(error => {
      console.error('로그아웃 요청 중 오류 발생:', error);
    });
});


    
