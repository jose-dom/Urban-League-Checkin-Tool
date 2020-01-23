    <script type="text/javascript" src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
    <script src="{% static 'view/dataTables.bootstrap4.min.js' %}"></script>
    <script src="{% static 'view/jquery.dataTables.min.js' %}"></script>
    <script src="https://code.jquery.com/jquery-3.3.1.js"></script>
    <script src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.19/js/dataTables.bootstrap.min.js"></script>
    <script src="https://cdn.datatables.net/responsive/2.2.3/js/dataTables.responsive.min.js"></script>
    <script src="https://cdn.datatables.net/responsive/2.2.3/js/responsive.bootstrap.min.js"></script>
    <script src="https://cdn.datatables.net/buttons/1.6.0/js/dataTables.buttons.min.js"></script>
    <script src="https://cdn.datatables.net/buttons/1.6.0/js/buttons.bootstrap4.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/pdfmake.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/vfs_fonts.js"></script>
    <script src="https://cdn.datatables.net/buttons/1.6.0/js/buttons.html5.min.js"></script>
    <script src="https://cdn.datatables.net/buttons/1.6.0/js/buttons.print.min.js"></script>
    <script src="https://cdn.datatables.net/buttons/1.6.0/js/buttons.colVis.min.js"></script>

//DataTable
    var table = $('#mainTable').DataTable({
        //pagingType: "simple",
        //autoWidth: true,
        buttons: ['excel', 'pdf']
    });
    table.buttons().container().appendTo('#menu');
//Monthly Visitors Graph
    var month = ["January","February","March","April","May","June","July","August","September","October","November","December","."];
    var count = [{% for t in date %}{{ t }},{% endfor %}0];
    var ctx = document.getElementById("month");   
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: month,
            datasets: [
            { 
                label: "Visitors",
                data: count,
                lineTension: 0.3,
                backgroundColor: "rgba(78,115,223,0.05)",
                borderColor: "rgba(78,115,223,1)",
                pointRadius: 3,
                pointBackgroundColor: "rgba(78,115,223,1)",
                pointBorderColor: "rgba(78,115,223,1)",
                pointHoverRadius: 3,
                pointHoverBackgroundColor: "rgba(78,115,223,1)",
                pointHoverBorderColor: "rgba(78,115,223,1)",
                pointHitRadius: 10,
                pointBorderWidth: 2
            }
            ],
        },
        options: {
            responsive: true, 
            maintainAspectRatio: false,
            layout: {
                padding: {
                    left: 10,
                    right: 25,
                    top: 25,
                    bottom: 0
                }
            },
            title: {
                display: true,
                text: 'Monthly Visits - 2019'
            },
            scales: {
                yAxes: [{
                    ticks: {
                        maxTicksLimit: 5,
                        padding: 10
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Total Number of Visitors'
                    },
                    gridLines: {
                        color: "rgb(234,236,244)",
                        zeroLineColor: "rgb(234,236,244)",
                        drawBorder: false,
                        borderDash: [2],
                        zeroLineBorderDash: [2]
                    }
                }],
                xAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: 'Month'
                    },
                    gridLines: {
                        display: false,
                        drawBorder: false
                    }
                }]
            },
            tooltips: {
            backgroundColor: "rgb(255,255,255)",
            bodyFontColor: "#858796",
            titleMarginBottom: 10,
            titleFontColor: '#6e707e',
            titleFontSize: 14,
            borderColor: '#dddfeb',
            borderWidth: 1,
            xPadding: 15,
            yPadding: 15,
            displayColors: false,
            intersect: false,
            model: 'index',
            caretPadding: 10,
            }
        }
    });        
//Visitor Gender Chart
    var gender = ["Male","Female","Other"];
    var count = [{% for t in gender %}{{ t }},{% endfor %}0];
    var ctx = document.getElementById("gender");
    var myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: gender,
            datasets: [
            { 
                data: count,
                backgroundColor: ["#4e73df", "#1cc88a", "#36b9cc"],
                hoverBackgroundColor: ["#2e59d9", "#17a673", "#2c9faf"],
                hoverBorderColor: "rgba(234,236,244,1)"
            }
            ],
        },
        options: {
            responsive: true, 
            maintainAspectRatio: false,
            tooltips: {
                backgroundColor: "rgb(255,255,255)",
                bodyFontColor: "#858796",
                borderColor: "#dddfeb",
                borderWidth: 1,
                xPadding: 15,
                yPadding: 15,
                displayColors: false,
                caretPadding: 10
            },
            title: {
                display: true,
                text: 'Visitors By Gender - 2019'
            },
            cutoutPercentage: 70,
        }
    });
//Popular Times Graph
    var time = ["3:00 AM","4:00 AM","5:00 AM","6:00 AM","7:00 AM","8:00 AM","9:00 AM","10:00 AM","11:00 AM","12:00 PM","1:00 PM","2:00 PM","3:00 PM","4:00 PM","5:00 PM","6:00PM","7:00PM","8:00PM","9:00PM","10:00PM", "."];
    var count = [{% for t in time %}{{ t }},{% endfor %}0];
    var ctx = document.getElementById("time");       
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: time,
            datasets: [
            { 
                label: "Visitors",
                data: count,
                lineTension: 0.3,
                backgroundColor: "rgba(78,115,223,0.05)",
                borderColor: "rgba(78,115,223,1)",
                pointRadius: 3,
                pointBackgroundColor: "rgba(78,115,223,1)",
                pointBorderColor: "rgba(78,115,223,1)",
                pointHoverRadius: 3,
                pointHoverBackgroundColor: "rgba(78,115,223,1)",
                pointHoverBorderColor: "rgba(78,115,223,1)",
                pointHitRadius: 10,
                pointBorderWidth: 2
            }
            ],
        },
        options: {
            responsive: true, 
            maintainAspectRatio: false,
            layout: {
                padding: {
                    left: 10,
                    right: 25,
                    top: 25,
                    bottom: 0
                }
            },
            title: {
                display: true,
                text: 'Popular Times - 2019'
            },
            scales: {
                yAxes: [{
                    ticks: {
                        maxTicksLimit: 5,
                        padding: 10
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Total Number of Visitors'
                    },
                    gridLines: {
                        color: "rgb(234,236,244)",
                        zeroLineColor: "rgb(234,236,244)",
                        drawBorder: false,
                        borderDash: [2],
                        zeroLineBorderDash: [2]
                    }
                }],
                xAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: 'Hour'
                    },
                    gridLines: {
                        display: false,
                        drawBorder: false
                    }
                }]
            },
            tooltips: {
            backgroundColor: "rgb(255,255,255)",
            bodyFontColor: "#858796",
            titleMarginBottom: 10,
            titleFontColor: '#6e707e',
            titleFontSize: 14,
            borderColor: '#dddfeb',
            borderWidth: 1,
            xPadding: 15,
            yPadding: 15,
            displayColors: false,
            intersect: false,
            mode: 'index',
            caretPadding: 10,
            }
        }
    });
//Major Purpose Graph
    var purpose = ["Employment Programs","Workforce Training Programs","Financial Opportunity Center","Workshops","Housing","Young Adults Program","Youth Education","Volunteering", "."];
    var count = [{% for t in major %}{{ t }},{% endfor %}0];
    var ctx = document.getElementById("purpose");
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: purpose,
            datasets: [
            { 
                label: "Visitors",
                data: count,
                lineTension: 0.3,
                backgroundColor: "rgba(78,115,223,0.05)",
                borderColor: "rgba(78,115,223,1)",
                pointRadius: 3,
                pointBackgroundColor: "rgba(78,115,223,1)",
                pointBorderColor: "rgba(78,115,223,1)",
                pointHoverRadius: 3,
                pointHoverBackgroundColor: "rgba(78,115,223,1)",
                pointHoverBorderColor: "rgba(78,115,223,1)",
                pointHitRadius: 10,
                pointBorderWidth: 2
            }
            ],
        },
        options: {
            responsive: true, 
            maintainAspectRatio: false,
            layout: {
                padding: {
                    left: 10,
                    right: 25,
                    top: 25,
                    bottom: 0
                }
            },
            title: {
                display: true,
                text: 'Major Purpose - 2019'
            },
            scales: {
                yAxes: [{
                    ticks: {
                        maxTicksLimit: 5,
                        padding: 10
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Total Number of Visitors'
                    },
                    gridLines: {
                        color: "rgb(234,236,244)",
                        zeroLineColor: "rgb(234,236,244)",
                        drawBorder: false,
                        borderDash: [2],
                        zeroLineBorderDash: [2]
                    }
                }],
                xAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: 'Major Purpose'
                    },
                    gridLines: {
                        display: false,
                        drawBorder: false
                    }
                }]
            },
            tooltips: {
            backgroundColor: "rgb(255,255,255)",
            bodyFontColor: "#858796",
            titleMarginBottom: 10,
            titleFontColor: '#6e707e',
            titleFontSize: 14,
            borderColor: '#dddfeb',
            borderWidth: 1,
            xPadding: 15,
            yPadding: 15,
            displayColors: false,
            intersect: false,
            mode: 'index',
            caretPadding: 10,
            }
        }
    });
//Visitor Race Chart -->
    var race = ["White","Black/Afro American","Hispanic","Aisan","Mixed","Other"];
    var count = [{% for t in ethnicity %}{{ t }},{% endfor %}0];
    var ctx = document.getElementById("ethnicity");
    var myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: race,
            datasets: [
            { 
                data: count,
                backgroundColor: ["#4e73df", "#1cc88a", "#36b9cc","#ff0000","#e0d1f7","#cd27ca"],
                hoverBackgroundColor: ["#4e73df", "#1cc88a", "#36b9cc","#ff0000","#e0d1f7","#cd27ca"],
                hoverBorderColor: "rgba(234,236,244,1)"
            }
            ],
        },
        options: {
            responsive: true, 
            maintainAspectRatio: false,
            tooltips: {
                backgroundColor: "rgb(255,255,255)",
                bodyFontColor: "#858796",
                borderColor: "#dddfeb",
                borderWidth: 1,
                xPadding: 15,
                yPadding: 15,
                displayColors: false,
                caretPadding: 10
            },
            title: {
                display: true,
                text: 'Visitors By Ethnicity - 2019'
            },
            cutoutPercentage: 70,
        }
    });
//Paginate Visitor Log
    $(document).ready(function () {
        $('#dataTable').DataTable({
            "pagingType": "simple"
        });
        $('.dataTables_length').addClass('bs-select');
    });
//Visitor Log Search Functions
    function searchEmail() 
    {
        var input, filter, table, tr, td, i, txtValue;
        input = document.getElementById("EmailInput");
        filter = input.value.toUpperCase();
        table = document.getElementById("dataTable");
        tr = table.getElementsByTagName("tr");

        //Loop through all rows, and hide those who don't match the search query
        for(i=0; i<tr.length; i++)
        {
            td = tr[i].getElementsByTagName("td")[4];
            if(td)
            {
                txtValue = td.textContent || td.innerText;
                if(txtValue.toUpperCase().indexOf(filter) > -1)
                {
                    tr[i].style.display = "";
                }
                else
                {
                    tr[i].style.display = "none";
                }
            }
        }
    }
    function searchAddress() 
    {
        var input, filter, table, tr, td, i, txtValue;
        input = document.getElementById("AddressInput");
        filter = input.value.toUpperCase();
        table = document.getElementById("dataTable");
        tr = table.getElementsByTagName("tr");

        //Loop through all rows, and hide those who don't match the search query
        for(i=0; i<tr.length; i++)
        {
            td = tr[i].getElementsByTagName("td")[5];
            if(td)
            {
                txtValue = td.textContent || td.innerText;
                if(txtValue.toUpperCase().indexOf(filter) > -1)
                {
                    tr[i].style.display = "";
                }
                else
                {
                    tr[i].style.display = "none";
                }
            }
        }
    }
    function searchPhone() 
    {
        var input, filter, table, tr, td, i, txtValue;
        input = document.getElementById("PhoneInput");
        filter = input.value.toUpperCase();
        table = document.getElementById("dataTable");
        tr = table.getElementsByTagName("tr");

        //Loop through all rows, and hide those who don't match the search query
        for(i=0; i<tr.length; i++)
        {
            td = tr[i].getElementsByTagName("td")[6];
            if(td)
            {
                txtValue = td.textContent || td.innerText;
                if(txtValue.toUpperCase().indexOf(filter) > -1)
                {
                    tr[i].style.display = "";
                }
                else
                {
                    tr[i].style.display = "none";
                }
            }
        }
    }