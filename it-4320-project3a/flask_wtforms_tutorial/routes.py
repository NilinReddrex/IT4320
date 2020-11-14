from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash, session

from .forms import StockForm
from .charts import *
from .symbolValidation import SymbolValidation
from .chartTypeValidation import ChartTypeValidation
from .timeSeriesValidation import TimeSeriesValidation
from .dateValidation import DateValidation

@app.route("/", methods=['GET', 'POST'])
@app.route("/stocks", methods=['GET', 'POST'])
def stocks():
    global symbolsCache
    
    err = None
    chart = None
    si = SymbolValidation()
    try:
        si.symbols = symbolsCache
        print("Symbols loaded from cache.")
    except NameError:
        print("Loading symbols cache.")
        symbolsCache = si.loadSymbols()

    form = StockForm()
    form.setSymbolChoices(symbolsCache)
    if request.method == 'POST':
        if form.validate_on_submit():
            #Get the form data to query the api
            symbol = request.form['symbol']

            if (si.isInputValid(symbol) == False):
                err = si.error
            
            chart_type = request.form['chart_type']

            ct = ChartTypeValidation()
            if(ct.isInputValid(chart_type) == False):
                err = ct.error

            time_series = request.form['time_series']

            ts = TimeSeriesValidation()
            if(ts.isInputValid(time_series) == False):
                err = ts.error

            start_date = request.form['start_date']
            end_date = request.form['end_date']

            d = DateValidation()
            if(d.isInputValid(start_date, end_date) == False):
                err = d.error

            if err == None:
                chart = queryStockData(symbol, chart_type, time_series, start_date, end_date)

                if (chart == "throttled"):
                    chart = None
                    err = "We have reached our maximum call limit to Alpha Vantage. Please wait 1m and try again."

            return render_template("stock.html", form=form, template="form-template", err = err, chart = chart)
    
    return render_template("stock.html", form=form, template="form-template")
