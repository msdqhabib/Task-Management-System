
// Chart js Configuration
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



$(document).ready(function() {
	// Get sorted tasks on change
	$('#sort_by').change(function() {
		var selectedValue = $(this).val();
		if (selectedValue) {

			// Make a GET request using AJAX
			$.ajax({
				url: '/task/',
				method: 'GET',
				data: {
					sort_by: selectedValue
				},
				success: function(response) {

					var tasksHtml = $(response).find('.task-container').html();
                    // Replace the tasks section with the new content
                    $('.task-container').html(tasksHtml);
				},
				error: function(xhr, errmsg, err) {
					// Handle any errors here
					console.log(xhr.status + ": " + xhr.responseText);
				}
			});
		}
	});

	// filter tasks based on their status
	$('#status').change(function() {
		var selectedValue = $(this).val();
		if (selectedValue) {

			// Make a GET request using AJAX
			$.ajax({
				url: '/task/',
				method: 'GET',
				data: {
					status: selectedValue
				},
				success: function(response) {

					var tasksHtml = $(response).find('.task-container').html();
                    // Replace the tasks section with the new content
                    $('.task-container').html(tasksHtml);
				},
				error: function(xhr, errmsg, err) {
					// Handle any errors here
					console.log(xhr.status + ": " + xhr.responseText);
				}
			});
		}
	});


	

	$("#create-task-btn").click(function() {
		var selectedTeamId = $("#team_title").val();
		$.ajax({
			url: "/teams/",  // URL to fetch users
			type: "GET",
			data: {
				team: selectedTeamId  // Pass the selected team ID
			},
			dataType: "json",
			success: function(response) {
				var assignedUserField = $("#assigned_user_id");
				assignedUserField.empty();  // Clear existing options

				// Append options for each user returned in the response
				$.each(response.options, function(index, option) {
					assignedUserField.append($('<option>', {
						value: option.value,
						text: option.label
					}));
				});
			},
			error: function(xhr, errmsg, err) {
				console.log(errmsg);  // Handle error
			}
		});
	});
	
});