Chart.defaults.font.family = 'Noto Sans KR';
Chart.defaults.locale = 'ko';
const chartData1 = {
  labels: [
    '2023-04-01',
    '2023-04-08',
    '2023-04-15',
    '2023-04-22',
    '2023-04-29',
    '2023-04-30',
    '2023-05-01',
    '2023-05-02',
    '2023-05-03',
    '2023-05-04',
    '2023-05-05',
    '2023-05-06',
    '2023-05-07',
    '2023-05-08',
  ],
  datasets: [
    {
      label: '강의1 출석 현황',
      data: [1, 0.5, 0, 0.5, 0.5, 0, 1, 1, 1, 0.5, 1, 1, 1],
      backgroundColor: '#36A2EB',
      borderWidth: 1,
    },
  ],
};

const config1 = {
  type: 'bar',
  data: chartData1,
  options: {
    plugins: {
      legend: {
        labels: {
          font: {
            size: 14,
            family: "Noto Sans KR"
          },
          color: "#36A2EB"
        },
      },
    },
    scales: {
      x: {
        ticks: {
          color: "#36A2EB",
          font: {
            family: "Noto Sans KR",
            size: 14
          },
          padding: 10
        },
        grid: {
          display: false
        }
      },
      y: {
        ticks: {
          color: "#36A2EB",
          font: {
            family: "Noto Sans KR",
            size: 14
          },
          callback: function(value, index, values) {
            return value.toFixed(1) + '%';
          }
        },
        grid: {
          color: "#36A2EB",
          drawTicks: false
        },
        min: 0,
        max: 1
      }
    },
    animation: {
      duration: 2000,
      easing: 'easeInOutCirc',
      animateRotate: true,
      animateScale: true
    }
  }
};

const chartData1Values = chartData1.datasets[0].data;
const chartData1AttendanceRate = chartData1Values.reduce((acc, curr) => acc + curr) / chartData1Values.length;

const chartData1Mean = {
  type: 'line',
  label: '평균',
  data: Array(chartData1Values.length).fill(chartData1AttendanceRate),
  backgroundColor: 'red',
  borderColor: 'red',
  borderWidth: 1,
  fill: false,
};
chartData1.datasets.push(chartData1Mean);
const chart1 = new Chart(document.getElementById('attendance-chart-1'), config1);

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

