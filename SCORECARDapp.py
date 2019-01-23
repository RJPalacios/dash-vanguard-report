# coding: utf-8

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import os

app = dash.Dash()
server = app.server

# read data for tables (one df per table)
#df_fund_facts = pd.read_csv('https://plot.ly/~bdun9/2754.csv')
df_fund_facts = pd.read_csv('C:/Users/rick/Downloads/2754(3).csv')

df_price_perf = pd.read_csv('https://plot.ly/~bdun9/2756.csv')
df_current_prices = pd.read_csv('https://plot.ly/~bdun9/2753.csv')
df_hist_prices = pd.read_csv('https://plot.ly/~bdun9/2765.csv')
df_avg_returns = pd.read_csv('https://plot.ly/~bdun9/2793.csv')
df_after_tax = pd.read_csv('https://plot.ly/~bdun9/2794.csv')
df_recent_returns = pd.read_csv('https://plot.ly/~bdun9/2795.csv')
df_equity_char = pd.read_csv('https://plot.ly/~bdun9/2796.csv')
df_equity_diver = pd.read_csv('https://plot.ly/~bdun9/2797.csv')
df_expenses = pd.read_csv('https://plot.ly/~bdun9/2798.csv')
df_minimums = pd.read_csv('https://plot.ly/~bdun9/2799.csv')
df_dividend = pd.read_csv('https://plot.ly/~bdun9/2800.csv')
df_realized = pd.read_csv('https://plot.ly/~bdun9/2801.csv')
df_unrealized = pd.read_csv('https://plot.ly/~bdun9/2802.csv')

df_graph = pd.read_csv("https://plot.ly/~bdun9/2804.csv")

class fund:
    def __init__(self, name):
        self.name = name
        self.returns = []
        self.benchmark_name = []
    def add_fund_return_info(self, df):
        self.returns = df
    def add_benchmark(self, name):
        self.benchmark_name = name
    def add_benchmark_return(self, bench_df):
        self.benchmark_retrun = bench_df

my_fucking_funds = ['Fund_1', 'Fund 2', 'Fund 3']
for f in my_fucking_funds:
    usaa_fund1 = fund(f)
    file_name_for_f = "c:/my_fking_file_path/"+ f + '.csv'
    usaa_fund1.benchmark_name = "S & P 500"
    usaa_fund1.add_fund_return_info(pd.DataFrame(data={'year':["1 Year", "3 Year", "5 Year", "10 Year", "41 Year"], 'returns': ["21.67", "11.26", "15.62", "8.37", "11.11"]}))
    usaa_fund1.add_benchmark_return(pd.DataFrame(data ={'year':["1 Year", "3 Year", "5 Year", "10 Year", "41 Year"], 'returns':["21.83", "11.41", "15.79", "8.50", '12.5']}))

# reusable components
def make_dash_table(df):
    ''' Return a dash definitio of an HTML table for a Pandas dataframe '''
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table


def print_button():
    printButton = html.A(['Print PDF'],className="button no-print print",style={'position': "absolute", 'top': '-40', 'right': '0'})
    return printButton

# includes page/full view
def get_logo():
    logo = html.Div([

        html.Div([
            #use USAA logo
            html.Img(src='https://botw-pd.s3.amazonaws.com/styles/logo-thumbnail/s3/012013/usaa_0.png?itok=ni4sDbQv', height='40', width='40')
        ], className="ten columns padded"),

        html.Div([
            dcc.Link('Full View   ', href='/full-view')
        ], className="two columns page-view no-print")

    ], className="row gs-header")
    return logo


def get_header():
    header = html.Div([

        html.Div([
            html.H5(
                'January 2019 UMP Manager Research Scorecard')
        ], className="twelve columns padded")

    ], className="row gs-header gs-text-header")
    return header


def get_menu():
    menu = html.Div([

        dcc.Link('Overview   ', href='/overview', className="tab first"),

        dcc.Link('Performance   ', href='/price-performance', className="tab"),

        dcc.Link('Exposures  ', href='/portfolio-management', className="tab"),

        dcc.Link('Scorecard   ', href='/fees', className="tab"),

        dcc.Link('Team   ', href='/distributions', className="tab"),

        dcc.Link('Operations & Contacts   ', href='/news-and-reviews', className="tab")

    ], className="row ")
    return menu

## Page layouts
overview = html.Div([  # page 1

        print_button(),

        html.Div([

            # Header
            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 3

            html.Div([

                html.Div([
                    html.H6('Strategy Summary',
                            className="gs-header gs-text-header padded"),

                    html.Br([]),

                    html.P("\
                            High level description of strategy, firm, and process.\
                            Example: The fund offers exposure to 500 of the \
                            largest U.S. companies, which span many different industries and \
                            account for about three-fourths of the U.S. stock market’s value. \
                            The key risk for the fund is the volatility that comes with its full \
                            exposure to the stock market. Because the 500 Index Fund is broadly \
                            diversified within the large-capitalization market, it may be \
                            considered a core equity holding in a portfolio."),

                ], className="six columns"),

                html.Div([
                    html.H6(["Fund Facts"],
                            className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(df_fund_facts))
                ], className="six columns"),

            ], className="row "),

            # Row 4

            html.Div([

                html.Div([
                    html.H6('Rolling Excess Returns',
                            className="gs-header gs-text-header padded"),
                    dcc.Graph(
                        id = "graph-1",
                        figure={
                            'data': [
                                go.Bar(
                                    x = usaa_fund1.returns.year,
                                    y = usaa_fund1.returns.returns,
                                    marker = {
                                      "color": "rgb(53, 83, 255)",
                                      "line": {
                                        "color": "rgb(255, 255, 255)",
                                        "width": 2
                                      }
                                    },
                                    name = usaa_fund1.name,
                                    type = "bar"
                                ),
                                go.Bar(
                                    x=usaa_fund1.benchmark_retrun.year,
                                    y=usaa_fund1.benchmark_retrun.returns,
                                    marker = {
                                      "color": "rgb(255, 225, 53)",
                                      "line": {
                                        "color": "rgb(255, 255, 255)",
                                        "width": 2
                                        }
                                    },
                                    name = usaa_fund1.benchmark_name,
                                    type = "bar"
                                ),
                            ],
                            'layout': go.Layout(
                                autosize = False,
                                bargap = 0.35,
                                font = {
                                  "family": "Raleway",
                                  "size": 10
                                },
                                height = 200,
                                hovermode = "closest",
                                legend = {
                                  "x": -0.0228945952895,
                                  "y": -0.189563896463,
                                  "orientation": "h",
                                  "yanchor": "top"
                                },
                                margin = {
                                  "r": 0,
                                  "t": 20,
                                  "b": 10,
                                  "l": 10
                                },
                                showlegend = True,
                                title = "",
                                width = 340,
                                xaxis = {
                                  "autorange": True,
                                  "range": [-0.5, 4.5],
                                  "showline": True,
                                  "title": "",
                                  "type": "category"
                                },
                                yaxis = {
                                  "autorange": True,
                                  "range": [0, 22.9789473684],
                                  "showgrid": True,
                                  "showline": True,
                                  "title": "",
                                  "type": "linear",
                                  "zeroline": False
                                }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="six columns"),

                html.Div([
                    html.H6("Member Experience",
                            className="gs-header gs-table-header padded"),
                    dcc.Graph(
                        id="grpah-2",
                        figure={
                            'data': [
                                go.Scatter(
                                    x = ["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018"],
                                    y = ["10000", "7500", "9000", "10000", "10500", "11000", "14000", "18000", "19000", "20500", "24000"],
                                    line = {"color": "rgb(53, 83, 255)"},
                                    mode = "lines",
                                    name = "Implemented June 30, 2016"
                                )
                            ],
                            'layout': go.Layout(
                                autosize = False,
                                title = "",
                                font = {
                                  "family": "Raleway",
                                  "size": 10
                                },
                                height = 200,
                                width = 340,
                                hovermode = "closest",
                                legend = {
                                  "x": -0.0277108433735,
                                  "y": -0.142606516291,
                                  "orientation": "h"
                                },
                                margin = {
                                  "r": 20,
                                  "t": 20,
                                  "b": 20,
                                  "l": 50
                                },
                                showlegend = True,
                                xaxis = {
                                  "autorange": True,
                                  "linecolor": "rgb(0, 0, 0)",
                                  "linewidth": 1,
                                  "range": [2008, 2018],
                                  "showgrid": False,
                                  "showline": True,
                                  "title": "",
                                  "type": "linear"
                                },
                                yaxis = {
                                  "autorange": False,
                                  "gridcolor": "rgba(127, 127, 127, 0.2)",
                                  "mirror": False,
                                  "nticks": 4,
                                  "range": [0, 30000],
                                  "showgrid": True,
                                  "showline": True,
                                  "ticklen": 10,
                                  "ticks": "outside",
                                  "title": "$",
                                  "type": "linear",
                                  "zeroline": False,
                                  "zerolinewidth": 4
                                }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="six columns"),

            ], className="row "),

            # Row 5

            html.Div([

                html.Div([
                    html.H6('Scorecard Summary',
                            className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(df_price_perf))
                ], className="six columns"),

                html.Div([
                    html.H6("Rating",
                            className="gs-header gs-table-header padded"),
                    dcc.Graph(
                        id='graph-3',
                        figure = {
                            'data': [
                                go.Scatter(
                                    x = ["0", "0.18", "0.18", "0"],
                                    y = ["0.2", "0.2", "0.4", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(31, 119, 180, 0.2)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "B",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.2", "0.38", "0.38", "0.2", "0.2"],
                                    y = ["0.2", "0.2", "0.6", "0.4", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(31, 119, 180, 0.4)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "D",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.4", "0.58", "0.58", "0.4", "0.4"],
                                    y = ["0.2", "0.2", "0.8", "0.6", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(31, 119, 180, 0.6)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "F",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.6", "0.78", "0.78", "0.6", "0.6"],
                                    y = ["0.2", "0.2", "1", "0.8", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgb(31, 119, 180)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "H",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.8", "0.98", "0.98", "0.8", "0.8"],
                                    y = ["0.2", "0.2", "1.2", "1", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(31, 119, 180, 0.8)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "J",
                                    showlegend = False
                                ),
                            ],
                            'layout': go.Layout(
                                title = "",
                                annotations = [
                                    {
                                      "x": 0.69,
                                      "y": 0.6,
                                      "font": {
                                        "color": "rgb(31, 119, 180)",
                                        "family": "Raleway",
                                        "size": 30
                                      },
                                      "showarrow": False,
                                      "text": "<b>4</b>",
                                      "xref": "x",
                                      "yref": "y"
                                    },
                                    {
                                      "x": 0.0631034482759,
                                      "y": -0.04,
                                      "align": "left",
                                      "font": {
                                        "color": "rgb(44, 160, 44)",
                                        "family": "Raleway",
                                        "size": 10
                                      },
                                      "showarrow": False,
                                      "text": "<b>Poor Fit<br>Redeem $</b>",
                                      "xref": "x",
                                      "yref": "y"
                                    },
                                    {
                                      "x": 0.92125,
                                      "y": -0.04,
                                      "align": "right",
                                      "font": {
                                        "color": "rgb(214, 39, 40)",
                                        "family": "Raleway",
                                        "size": 10
                                      },
                                      "showarrow": False,
                                      "text": "<b>Best in Class<br>Firm & Strategy</b>",
                                      "xref": "x",
                                      "yref": "y"
                                    }
                                  ],
                                  autosize = False,
                                  height = 200,
                                  width = 340,
                                  hovermode = "closest",
                                  margin = {
                                    "r": 10,
                                    "t": 20,
                                    "b": 80,
                                    "l": 10
                                  },
                                  shapes = [
                                    {
                                      "fillcolor": "rgb(255, 255, 255)",
                                      "line": {
                                        "color": "rgb(31, 119, 180)",
                                        "width": 4
                                      },
                                      "opacity": 1,
                                      "type": "circle",
                                      "x0": 0.621,
                                      "x1": 0.764,
                                      "xref": "x",
                                      "y0": 0.135238095238,
                                      "y1": 0.98619047619,
                                      "yref": "y"
                                    }
                                  ],
                                  showlegend = True,
                                  xaxis = {
                                    "autorange": False,
                                    "fixedrange": True,
                                    "range": [-0.05, 1.05],
                                    "showgrid": False,
                                    "showticklabels": False,
                                    "title": "<br>",
                                    "type": "linear",
                                    "zeroline": False
                                  },
                                  yaxis = {
                                    "autorange": False,
                                    "fixedrange": True,
                                    "range": [-0.3, 1.6],
                                    "showgrid": False,
                                    "showticklabels": False,
                                    "title": "<br>",
                                    "type": "linear",
                                    "zeroline": False
                                }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="six columns"),

            ], className="row ")

        ], className="subpage")

    ], className="page")


pricePerformance = html.Div([  # page 2

        print_button(),

        html.Div([

            # Header
            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row ``

            html.Div([

                html.Div([
                    html.H6(["As of 12/30/18"],
                            className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(df_current_prices))

                ], className="six columns"),

                html.Div([
                    html.H6(["Annual Returns"],
                            className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(df_hist_prices))
                ], className="six columns"),

            ], className="row "),

            # Row 2

            html.Div([

                html.Div([
                    html.H6("Performance",
                            className="gs-header gs-table-header padded"),
                    dcc.Graph(
                        id='graph-4',
                        figure={
                            'data': [
                                go.Scatter(
                                    x = df_graph['Date'],
                                    y = df_graph['Vanguard 500 Index Fund'], # column name in csv file
                                    line = {"color": "rgb(53, 83, 255)"},
                                    mode = "lines",
                                    name = "Vanguard" # legend name
                                ),
                                go.Scatter(
                                    x = df_graph['Date'],
                                    y = df_graph['MSCI EAFE Index Fund (ETF)'],
                                    line = {"color": "rgb(255, 225, 53)"},
                                    mode = "lines",
                                    name = "SP 500"
                                )
                            ],
                            'layout': go.Layout(
                                autosize = False,
                                width = 700,
                                height = 200,
                                font = {
                                    "family": "Raleway",
                                    "size": 10
                                  },
                                 margin = {
                                    "r": 40,
                                    "t": 40,
                                    "b": 30,
                                    "l": 40
                                  },
                                  showlegend = True,
                                  titlefont = {
                                    "family": "Raleway",
                                    "size": 10
                                  },
                                  xaxis = {
                                    "autorange": True,
                                    "range": ["2007-12-31", "2018-03-06"],
                                    "rangeselector": {"buttons": [
                                        {
                                          "count": 1,
                                          "label": "1Y",
                                          "step": "year",
                                          "stepmode": "backward"
                                        },
                                        {
                                          "count": 3,
                                          "label": "3Y",
                                          "step": "year",
                                          "stepmode": "backward"
                                        },
                                        {
                                          "count": 5,
                                          "label": "5Y",
                                          "step": "year"
                                        },
                                        {
                                          "count": 10,
                                          "label": "10Y",
                                          "step": "year",
                                          "stepmode": "backward"
                                        },
                                        {
                                          "label": "All",
                                          "step": "all"
                                        }
                                      ]},
                                    "showline": True,
                                    "type": "date",
                                    "zeroline": False
                                  },
                                  yaxis = {
                                    "autorange": True,
                                    "range": [18.6880162434, 278.431996757],
                                    "showline": True,
                                    "type": "linear",
                                    "zeroline": False
                                  }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="twelve columns")

            ], className="row "),

            # Row 3

            html.Div([

                html.Div([
                    html.H6(["Trailing Returns"], className="gs-header gs-table-header tiny-header"),
                    html.Table(make_dash_table(df_avg_returns), className="tiny-header")
                ], className=" twelve columns"),

            ], className="row "),

            # Row 4

            html.Div([

                html.Div([
                    html.H6(["vs Peers & Category"], className="gs-header gs-table-header tiny-header"),
                    html.Table(make_dash_table(df_after_tax), className="tiny-header")
                ], className=" twelve columns"),

            ], className="row "),

            # Row 5

            html.Div([

                html.Div([
                    html.H6(["Ratios"], className="gs-header gs-table-header tiny-header"),
                    html.Table(make_dash_table(df_recent_returns), className="tiny-header")
                ], className=" twelve columns"),

            ], className="row "),

        ], className="subpage")

    ], className="page")


portfolioManagement = html.Div([ # page 3

        print_button(),

        html.Div([

            # Header

            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 1

            html.Div([

                html.Div([
                    html.H6(["Portfolio"],
                            className="gs-header gs-table-header padded")
                ], className="twelve columns"),

            ], className="row "),

            # Row 2

            html.Div([

                html.Div([
                    html.Strong(["Stock style"]),
                    dcc.Graph(
                        id='graph-5',
                        figure={
                            'data': [
                                go.Scatter(
                                    x = ["1"],
                                    y = ["1"],
                                    hoverinfo = "none",
                                    marker = {
                                        "color": ["transparent"]
                                    },
                                    mode = "markers",
                                    name = "B",
                                )
                            ],
                            'layout': go.Layout(
                                title = "",
                                annotations = [
                                {
                                  "x": 0.990130093458,
                                  "y": 1.00181709504,
                                  "align": "left",
                                  "font": {
                                    "family": "Raleway",
                                    "size": 9
                                  },
                                  "showarrow": False,
                                  "text": "<b>Market<br>Cap</b>",
                                  "xref": "x",
                                  "yref": "y"
                                },
                                {
                                  "x": 1.00001816013,
                                  "y": 1.35907755794e-16,
                                  "font": {
                                    "family": "Raleway",
                                    "size": 9
                                  },
                                  "showarrow": False,
                                  "text": "<b>Style</b>",
                                  "xref": "x",
                                  "yanchor": "top",
                                  "yref": "y"
                                }
                              ],
                              autosize = False,
                              width = 200,
                              height = 150,
                              hovermode = "closest",
                              margin = {
                                "r": 30,
                                "t": 20,
                                "b": 20,
                                "l": 30
                              },
                              shapes = [
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rectangle",
                                  "x0": 0,
                                  "x1": 0.33,
                                  "xref": "paper",
                                  "y0": 0,
                                  "y1": 0.33,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "dash": "solid",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rectangle",
                                  "x0": 0.33,
                                  "x1": 0.66,
                                  "xref": "paper",
                                  "y0": 0,
                                  "y1": 0.33,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rectangle",
                                  "x0": 0.66,
                                  "x1": 0.99,
                                  "xref": "paper",
                                  "y0": 0,
                                  "y1": 0.33,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rectangle",
                                  "x0": 0,
                                  "x1": 0.33,
                                  "xref": "paper",
                                  "y0": 0.33,
                                  "y1": 0.66,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rectangle",
                                  "x0": 0.33,
                                  "x1": 0.66,
                                  "xref": "paper",
                                  "y0": 0.33,
                                  "y1": 0.66,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rectangle",
                                  "x0": 0.66,
                                  "x1": 0.99,
                                  "xref": "paper",
                                  "y0": 0.33,
                                  "y1": 0.66,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rectangle",
                                  "x0": 0,
                                  "x1": 0.33,
                                  "xref": "paper",
                                  "y0": 0.66,
                                  "y1": 0.99,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(255, 127, 14)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 1
                                  },
                                  "opacity": 0.9,
                                  "type": "rectangle",
                                  "x0": 0.33,
                                  "x1": 0.66,
                                  "xref": "paper",
                                  "y0": 0.66,
                                  "y1": 0.99,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rectangle",
                                  "x0": 0.66,
                                  "x1": 0.99,
                                  "xref": "paper",
                                  "y0": 0.66,
                                  "y1": 0.99,
                                  "yref": "paper"
                                }
                              ],
                              xaxis = {
                                "autorange": True,
                                "range": [0.989694747864, 1.00064057995],
                                "showgrid": False,
                                "showline": False,
                                "showticklabels": False,
                                "title": "<br>",
                                "type": "linear",
                                "zeroline": False
                              },
                              yaxis = {
                                "autorange": True,
                                "range": [-0.0358637178721, 1.06395696354],
                                "showgrid": False,
                                "showline": False,
                                "showticklabels": False,
                                "title": "<br>",
                                "type": "linear",
                                "zeroline": False
                              }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )

                ], className="four columns"),

                html.Div([
                    html.P("Vanguard 500 Index Fund seeks to track the performance of\
                     a benchmark index that meaures the investment return of large-capitalization stocks."),
                    html.P("Learn more about this portfolio's investment strategy and policy.")
                ], className="eight columns middle-aligned"),

            ], className="row "),

            # Row 3

            html.Br([]),

            html.Div([

                html.Div([
                    html.H6(["Factor Exposures as of 01/31/2018"], className="gs-header gs-table-header tiny-header"),
                    html.Table(make_dash_table(df_equity_char), className="tiny-header")
                ], className=" twelve columns"),

            ], className="row "),

            # Row 4

            html.Div([

                html.Div([
                    html.H6(["Sector Active Weight"], className="gs-header gs-table-header tiny-header"),
                    html.Table(make_dash_table(df_equity_diver), className="tiny-header")
                ], className=" twelve columns"),

            ], className="row "),

        ], className="subpage")

    ], className="page")

feesMins = html.Div([  # page 4

        print_button(),

        html.Div([

            # Header

            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 1

            html.Div([

                html.Div([
                    html.H6(["Scorecard"],
                            className="gs-header gs-table-header padded")
                ], className="twelve columns"),

            ], className="row "),

            # Row 2

            html.Div([

                html.Div([
                    html.Strong(),
                    html.Table(make_dash_table(df_expenses)),
                    html.H6(["Minimums"],
                            className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(df_minimums))
                ], className="six columns"),

                html.Div([
                    html.Br([]),
                    html.Strong("Strategy Flows"),
                    dcc.Graph(
                        id = 'graph-6',
                        figure = {
                            'data': [
                                go.Bar(
                                    x = ["Category Average", "This fund"],
                                    y = ["2242", "329"],
                                    marker = {"color": "rgb(53, 83, 255)"},
                                    name = "A"
                                ),
                                go.Bar(
                                    x = ["This fund"],
                                    y = ["1913"],
                                    marker = {"color": "#ADAAAA"},
                                    name = "B"
                                )
                            ],
                            'layout': go.Layout(
                                annotations = [
                                    {
                                      "x": -0.0111111111111,
                                      "y": 2381.92771084,
                                      "font": {
                                        "color": "rgb(0, 0, 0)",
                                        "family": "Raleway",
                                        "size": 10
                                      },
                                      "showarrow": False,
                                      "text": "$2,242",
                                      "xref": "x",
                                      "yref": "y"
                                    },
                                    {
                                      "x": 0.995555555556,
                                      "y": 509.638554217,
                                      "font": {
                                        "color": "rgb(0, 0, 0)",
                                        "family": "Raleway",
                                        "size": 10
                                      },
                                      "showarrow": False,
                                      "text": "$329",
                                      "xref": "x",
                                      "yref": "y"
                                    },
                                    {
                                      "x": 0.995551020408,
                                      "y": 1730.32432432,
                                      "font": {
                                        "color": "rgb(0, 0, 0)",
                                        "family": "Raleway",
                                        "size": 10
                                      },
                                      "showarrow": False,
                                      "text": "You save<br><b>$1,913</b>",
                                      "xref": "x",
                                      "yref": "y"
                                    }
                                  ],
                                  autosize = False,
                                  height = 150,
                                  width = 340,
                                  bargap = 0.4,
                                  barmode = "stack",
                                  hovermode = "closest",
                                  margin = {
                                    "r": 40,
                                    "t": 20,
                                    "b": 20,
                                    "l": 40
                                  },
                                  showlegend = False,
                                  title = "",
                                  xaxis = {
                                    "autorange": True,
                                    "range": [-0.5, 1.5],
                                    "showline": True,
                                    "tickfont": {
                                      "family": "Raleway",
                                      "size": 10
                                    },
                                    "title": "",
                                    "type": "category",
                                    "zeroline": False
                                  },
                                  yaxis = {
                                    "autorange": False,
                                    "mirror": False,
                                    "nticks": 3,
                                    "range": [0, 3000],
                                    "showgrid": True,
                                    "showline": True,
                                    "tickfont": {
                                      "family": "Raleway",
                                      "size": 10
                                    },
                                    "tickprefix": "$",
                                    "title": "",
                                    "type": "linear",
                                    "zeroline": False
                                  }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="six columns"),

            ], className="row "),

            # Row 3

            html.Div([

                html.Div([
                    html.H6(["Summary"],
                            className="gs-header gs-table-header padded"),

                    html.Br([]),

                    html.Div([

                        html.Div([
                            html.Strong(["Firm"])
                        ], className="three columns right-aligned"),

                        html.Div([
                            html.P(["None"])
                        ], className="nine columns")


                    ], className="row "),

                    html.Div([

                        html.Div([
                            html.Strong(["People"])
                        ], className="three columns right-aligned"),

                        html.Div([
                            html.P(["None"])
                        ], className="nine columns")

                    ], className="row "),

                    html.Div([

                        html.Div([
                            html.Strong(["Performance"])
                        ], className="three columns right-aligned"),

                        html.Div([
                            html.P(["None"])
                        ], className="nine columns")

                    ], className="row "),

                    html.Div([

                        html.Div([
                            html.Strong(["Process"])
                        ], className="three columns right-aligned"),

                        html.Div([
                            html.Strong(["Multi manager quantitative approach"]),
                            html.P(["Closet Passive Active Manager"]),
                            html.Br([]),
                            html.Strong(["Return Expectations"]),
                            html.P(["Cheap beta relative to other CLoset Passive solutions"]),
                            html.Br([]),
                            html.Strong(["403(b)(7) plans"]),
                            html.P(["Equal weight DE Shaw, Vanguard QIS, and LA Capital are the current line up"]),
                            html.Br([]),
                            html.Strong(["Sub-advisor Lineup"]),
                            html.P(["Outperformance of 200bp over ANY period = Initiate watchlist; something is wrong.... "]),
                            html.Br([]),
                        ], className="nine columns")

                    ], className="row ")

                ], className="twelve columns")

            ], className="row "),

        ], className="subpage")

    ], className="page")

distributions = html.Div([  # page 5

        print_button(),

        html.Div([

            # Header

            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 1

            html.Div([

                html.Div([
                    html.H6(["Team"],
                            className="gs-header gs-table-header padded"),
                    html.Strong(["Multi-manager approach with strong sub adviser line up.  Value add for star managers is reduced investor relations/interactions"])
                ], className="twelve columns"),

            ], className="row "),

            # Row 2

            html.Div([

                html.Div([
                    html.Br([]),
                    html.H6(["Dividend and capital gains distributions"], className="gs-header gs-table-header tiny-header"),
                    html.Table(make_dash_table(df_dividend), className="tiny-header")
                ], className="twelve columns"),

            ], className="row "),

            # Row 3

            html.Div([

                html.Div([
                    html.H6(["Realized/unrealized gains as of 01/31/2018"], className="gs-header gs-table-header tiny-header")
                ], className=" twelve columns")

            ], className="row "),

            # Row 4

            html.Div([

                html.Div([
                    html.Table(make_dash_table(df_realized))
                ], className="six columns"),

                html.Div([
                    html.Table(make_dash_table(df_unrealized))
                ], className="six columns"),

            ], className="row "),

        ], className="subpage")

    ], className="page")


newsReviews = html.Div([  # page 6

        print_button(),

        html.Div([

            # Header

            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 1

            html.Div([

                html.Div([
                    html.H6('News',
                            className="gs-header gs-text-header padded"),
                    html.Br([]),
                    html.P('10/25/16    Firm completed purchase of XYZ Capital, increasing product suite.'),
                    html.Br([]),
                    html.P("08/31/16    CFO Joe Blow has left the firm; no impact day to day operations.")
                ], className="six columns"),

                html.Div([
                    html.H6("Reviews",
                            className="gs-header gs-table-header padded"),
                    html.Br([]),
                    html.Li('Launched in 1976.'),
                    html.Li('On average, has historically produced returns that have far outpaced the rate of inflation.*'),
                    html.Li("Vanguard Quantitative Equity Group, the fund's advisor, is among the world's largest equity index managers."),
                    html.Br([]),
                    html.P("ABC"),
                    html.Br([]),
                    html.P("DEF"),
                    html.Br([]),
                    html.P("G"),
                    html.Br([]),
                    html.P("HIJK"),
                    html.Br([]),
                    html.P("LMNOP")
                ], className="six columns"),

            ], className="row ")

        ], className="subpage")

    ], className="page")
noPage = html.Div([  # 404

    html.P(["404 Page not found"])

    ], className="no-page")



# Describe the layout, or the UI, of the app
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Update page
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/' or pathname == '/overview':
        return overview
    elif pathname == '/price-performance':
        return pricePerformance
    elif pathname == '/portfolio-management':
        return portfolioManagement
    elif pathname == '/fees':
        return feesMins
    elif pathname == '/distributions':
        return distributions
    elif pathname == '/news-and-reviews':
        return newsReviews
    elif pathname == '/full-view':
        return overview,pricePerformance,portfolioManagement,feesMins,distributions,newsReviews
    else:
        return noPage


external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://rawgit.com/RJPalacios/dash-vanguard-report/master/css_files/KQrXdb.css",
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

local_css = ["C:\\Users\\rick\github\dash-vanguard-report\css\KQRXdb.css"]

for css in external_css:
    app.css.append_css({"external_url": css})

external_js = ["https://code.jquery.com/jquery-3.2.1.min.js",
               "https://codepen.io/bcd/pen/YaXojL.js"]

for js in external_js:
    app.scripts.append_script({"external_url": js})


if __name__ == '__main__':
    app.run_server(debug=True)
