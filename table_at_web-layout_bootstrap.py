import pandas as pd

from flask import Flask, render_template_string

app = Flask(__name__)

# read data from Excel file 

data = pd.read_excel('C:/Praktyczny_Python/ROBOCZE/tabela kursów NBP z dnia 2023-11-10.xlsx', na_filter = '', skiprows=1)

# transform data into HTML
html_table = data.to_html(classes='table table-bordered table-hover', index=False, col_space=10, max_rows=8)

@app.route('/')
def home():
    # HTML template
    html_template = '''
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=2.0">
        <title>Dane z Excel</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">

        <style>
            th {text-align: left;
            font-weight: bold;
            background-color: #AEEEEE;}
        </style>    
    </head>
    <body>
        <div class="container">
            <h1>Dane z Excel</h1>
            {{ table|safe }}
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_template, table=html_table)

if __name__ == '__main__':
    app.run(debug=True)