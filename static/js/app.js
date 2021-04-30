// function to extract the values for display

function extractValues(county) {
    d3.json("counties.json").then((data)=>{
        countydata = data.counties;
        // console.log(countydata);
        
        var mycounty = countydata.filter(d => d.county == county);                
        console.log(mycounty)

        mycounty = mycounty[0];

        vaccinated = mycounty.vaccinated;
        vacc_rate= mycounty.vacc_rate;
        vacc_percent= mycounty.vacc_percent;
        days_to_HIT= mycounty.days_to_HIT;
        population= mycounty.population;
        pc_uninsured= mycounty.pc_uninsured;
        pc_poverty= mycounty.pc_poverty;
        pop_density= mycounty.pop_density   
        
        document.getElementById("county-population").innerHTML = population;
        document.getElementById("county-pcvaccinated").innerHTML = vacc_percent;
        document.getElementById("county-rate").innerHTML = vacc_rate;
        document.getElementById("county-pcuninsured").innerHTML = pc_uninsured;
        document.getElementById("county-pcpoverty").innerHTML = pc_poverty;
        document.getElementById("county-hitdays").innerHTML = days_to_HIT;




    })
}
   
// Build the init function including the dropdown menu choices

function init(){
    var selector = d3.select("#selCounty");
    d3.json("counties.json").then((data)=>{
        var countynames = data.names;
        console.log(countynames)
        countynames.forEach((item)=>{
            selector.append("option").text(item).property("value",item);            
        })     
        
        var firstcounty = countynames[0];
        extractValues(firstcounty);
        buildCharts(firstcounty)
        
        // console.log(firstcounty)          
    });
}

// Build the updating function when dropdown menu changes
function dropdownChange(newCounty){    
    extractValues(newCounty);
    buildCharts(newCounty)
}

// Create the Gauge Chart
function buildCharts(county){
    d3.json("counties.json").then((data)=>{
        countydata = data.counties;        
        
        var mycounty = countydata.filter(d => d.county == county);                
        mycounty = mycounty[0];
                
        vacc_percent= mycounty.vacc_percent;
        vacc_percent=parseInt(vacc_percent, 10)

        pc_poverty = mycounty.pc_poverty;
        pc_poverty=parseInt(pc_poverty, 10)        

        pc_uninsured = mycounty.pc_uninsured;
        pc_uninsured=parseInt(pc_uninsured, 10)

        gaugeTrace ={
            domain: { x: [0, 1], y: [0, 1] },
            value: vacc_percent,
            title: { text: "% Vaccinated" },
            type: "indicator",
            mode: "gauge+number",
            gauge: {
                axis:  {range: [null,100]},
                steps: [
                    {range: [0,10], color: "purple"},
                    {range: [10,20], color: "violet"},
                    {range: [20,30], color: "red"},
                    {range: [30,40], color: "orange"},
                    {range: [40,50], color: "yellow"},
                    {range: [50,60], color: "yellow"},
                    {range: [60,70], color: "lightblue"},
                    {range: [70,80], color: "lightgreen"},
                    {range: [80,90], color: "green"},
                    {range: [90,100], color: "darkgreen"}
                ],
            }
        }
        
        var gaugelayout = { 
            width: 600, 
            height: 500, 
            margin: { t: 0, b: 0 } 
        };     

        Plotly.newPlot("vacc_gauge",[gaugeTrace],gaugelayout);

        gaugeTrace ={
            domain: { x: [0, 1], y: [0, 1] },
            value: pc_poverty,
            title: { text: "% Poverty" },
            type: "indicator",
            mode: "gauge+number",
            gauge: {
                axis:  {range: [null,100]},
                steps: [
                    {range: [0,10], color: "green"},
                    {range: [10,40], color: "yellow"},
                    {range: [40,60], color: "lightblue"},
                    {range: [60,100], color: "blue"},
                    
                ],
            }
        }
        
        var gaugelayout = { 
            width: 600, 
            height: 500, 
            margin: { t: 0, b: 0 } 
        };     

        Plotly.newPlot("poverty_gauge",[gaugeTrace],gaugelayout);

        
        gaugeTrace ={
            domain: { x: [0, 1], y: [0, 1] },
            value: pc_uninsured,
            title: { text: "% Uninsured" },
            type: "indicator",
            mode: "gauge+number",
            gauge: {
                axis:  {range: [null,100]},
                steps: [
                    {range: [0,10], color: "green"},
                    {range: [10,40], color: "yellow"},
                    {range: [40,60], color: "lightblue"},
                    {range: [60,100], color: "blue"},
                    
                ],
            }
        }
        
        var gaugelayout = { 
            width: 600, 
            height: 500, 
            margin: { t: 0, b: 0 } 
        };     

        Plotly.newPlot("uninsured_gauge",[gaugeTrace],gaugelayout);
        
    })   
};

// Load the Initial County
init();



