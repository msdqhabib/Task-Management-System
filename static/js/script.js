var stackedChart = document.getElementById("myChart4");


if (stackedChart) {

	
	stackedChart.getContext('2d');
	var myChart = new Chart(stackedChart, {
	type: 'bar',
	data: {
		labels: ["01 Apr","02 Apr","03 Apr","04 Apr","05 Apr","06 Apr"],
		datasets: [{
			label: 'Total',
			backgroundColor: "#60a5fa",
			data: [4, 3, 5, 6, 7],
		}, {
			label: 'Incomplete',
			backgroundColor: "#fb7185",
			data: [2, 3, 1, 3, 2],
		}, {
			label: 'Complete',
			backgroundColor: "#4ade80",
			data: [2, 0, 4, 3, 5],
		}],
	},
	options: {
		tooltips: {
      displayColors: true,
      callbacks:{
		  mode: 'x',
		},
    },
    scales: {
		xAxes: [{
			stacked: true,
			gridLines: {
          display: false,
        }
	}],
      yAxes: [{
        stacked: true,
        ticks: {
			beginAtZero: true,
        },
        type: 'linear',
	}]
},
		responsive: true,
		maintainAspectRatio: false,
		legend: { position: 'bottom' },
	}
});
	}