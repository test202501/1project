import pandas as pd

from flask import Flask, render_template_string

app = Flask(__name__)

# read data from Excel file 

data = pd.read_excel('C:/Praktyczny_Python/ROBOCZE/tabela kursów NBP z dnia 2023-11-10.xlsx', na_filter = '', skiprows=1)

# transform data into HTML
html_table = data.to_html(classes='min-w-full divide-y divide-gray-100 hover:bg-green-100 border bold border-green-300', index=False, col_space=10)

@app.route('/')
def home():
    # HTML template
    html_template = '''
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dane z Excel</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css">

        <style>
            th {text-align: left;
            font-weight: bold;
            font-underlined: true;
            font-size: 13;
            background-color: #DF0050;}
        </style>    
    </head>
    <body>
        <div class="container mx-auto p-4">
            <h1>Dane z Excel</h1>
            {{ table|safe }}
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_template, table=html_table)

if __name__ == '__main__':
    app.run(debug=True)