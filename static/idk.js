// JS 
var chart = JSC.chart('chartDiv', { 
    debug: true, 
    legend: { 
      position: 'inside left bottom', 
      template: 
        '%value {%percentOfTotal:n1}% %icon %name'
    }, 
    title_position: 'center', 
    defaultSeries_type: 'pieDonut', 
    defaultPoint_label_text: '<b>%artist_name</b>', 
    title_label_text: 'Artist Popularity', 
    yAxis: { label_text: 'Popularity', formatString: 'n' }, 
    series: [ 
      { 
        name: 'Artist', 
        points: [ 
          { artist_name: 'United States', y: 5452500 }, 
          { artist_name: 'Canada', y: 786052 }, 
          { artist_name: 'United Kingdom', y: 477338 }, 
          { artist_name: 'Mexico', y: 155313 } 
        ] 
      } 
    ] 
  }); 