var width = 450,
    height = 450,
    margin = 40;

// The radius of the pie plot is half the width or half the height (the smallest dimension). Subtract a bit of margin.
var radius = Math.min(width, height) / 2 - margin;

// append the svg object to the div called 'my_dataviz'
var svg2 = d3.select("#my_dataviz")
  .append("svg")
    .attr("width", width)
    .attr("height", height)
  .append("g")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

// create 2 data sets
var data3 = {a: 9, b: 20, c: 30, d: 8, e: 12};
var data4 = {a: 6, b: 16, c: 20, d: 14, e: 19, f: 12};

// set the color scale
var color = d3.scaleOrdinal()
  .domain(["a", "b", "c", "d", "e", "f"])
  .range(d3.schemeDark2);

// A function that creates / updates the plot for the second graph:
function update2(data) {
  // Compute the position of each group on the pie
  var pie = d3.pie()
    .value(function(d) { return d.value; })
    .sort(function(a, b) { console.log(a); return d3.ascending(a.key, b.key); }); // This ensures that group order remains the same in the pie chart
  var data_ready = pie(d3.entries(data));

  // map to data
  var t = svg2.selectAll("path")
    .data(data_ready);

  // Build the pie chart: Each part of the pie is a path built using the arc function
  t.enter()
    .append("path")
    .merge(t)
    .transition()
    .duration(1000)
    .attr("d", d3.arc()
      .innerRadius(0)
      .outerRadius(radius)
    )
    .attr("fill", function(d) { return color(d.data.key); })
    .attr("stroke", "white")
    .style("stroke-width", "2px")
    .style("opacity", 1);

  // Remove the group that is not present anymore
  t.exit()
    .remove();
}

// Initialize the plot with the first dataset for the second graph
update2(data3);
