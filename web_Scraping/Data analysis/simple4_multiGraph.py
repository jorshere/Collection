import justpy as jp

import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv("reviews.csv",parse_dates=['Timestamp'])

data["Month"]  = data['Timestamp'].dt.strftime("%Y-%m") 

month_avg_course = data.groupby(['Month','Course Name'])["Rating"].mean().unstack()


chart_def = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average fruit consumption during one week'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor: '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""


def app():
    wp = jp.QuasarPage()                #wp: webpage;
    h1 = jp.QDiv(a=wp, text="Analysis of course review", classes="text-h3 text-center q-pa-md")
    p1= jp.QDiv(a=wp, text=" These graphs represantation")

    hc = jp.HighCharts(a=wp, options= chart_def)

    hc.options.xAxis.categories= list(month_avg_course.index)

    hc_data = [{"name":var1, "data":[var2 for var2 in month_avg_course[var1]]} for var1 in month_avg_course.columns ]
   
    hc.options.series = hc_data

    return wp
jp.justpy(app) 