// Initialize the echarts instance based on the prepared dom
const chart1 = echarts.init(document.getElementById("main"));

const chart2 = echarts.init(document.getElementById("six"));

drawPM25();

function drawSixPm25() {
  $.ajax({
    url: "/six-pm25-data",
    type: "GET",
    dataType: "JSON",
    success: (result) => {
      console.log(result);
      drawChart(
        chart2,
        "六都PM2.5平均值",
        "PM2.5",
        result["site"],
        result["pm25"]
      );
    },
  });
}

function drawPM25() {
  chart1.showLoading();
  $.ajax({
    url: "/pm25-data",
    type: "GET",
    dataType: "JSON",
    success: (result) => {
      console.log(result);
      drawChart(
        chart1,
        result["datetime"],
        "PM2.5",
        result["site"],
        result["pm25"]
      );
      chart1.hideLoading();
      drawSixPm25();
    },
    error: () => {
      alert("System Updating, Please Try Again Later");
      chart1.hideLoading();
    },
  });
}

function drawChart(chart, title, legend, xData, yData) {
  // Specify the configuration items and data for the chart
  let option = {
    title: {
      text: title,
    },
    tooltip: {},
    legend: {
      data: legend,
    },
    xAxis: {
      data: xData,
    },
    yAxis: {},
    series: [
      {
        name: legend,
        type: "bar",
        data: yData,
      },
    ],
  };

  // Display the chart using the configuration items and data just specified.
  chart.setOption(option);
}
