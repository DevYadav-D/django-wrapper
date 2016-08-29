from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from ..lib.fusioncharts import FusionCharts

# Loading Data from a Static JSON String
# It is a example to show a Column 2D chart where data is passed as JSON string format.
# The `fc_xmlurl` method is defined to load chart data from an JSON string.

def fc_xmlurl(request):
  # Create an object for the column2d chart using the FusionCharts class constructor
  column2d = FusionCharts("column2d", "ex1" , "600", "400", "chart-1", "xmlurl","http://127.0.0.1:8000/static/data/data.xml")
  
    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.  
  return  render(request, 'fusioncharts-html-template.html', {'output' : column2d.render()})
