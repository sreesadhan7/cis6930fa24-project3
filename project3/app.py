from flask import Flask, request, render_template, redirect
import os
from project3 import fetch_incidents, extract_incidents, createdb, populatedb, status
import pandas as pd
from clustering import cluster_and_visualize
from flask import send_from_directory

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        pdf_path = None

        # Handle URL input
        if url:
            pdf_path = fetch_incidents(url)
        elif 'file' in request.files:
            uploaded_file = request.files['file']
            if uploaded_file.filename != '':
                pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
                uploaded_file.save(pdf_path)

        # Process the PDF and visualize
        if pdf_path:
            incidents_df = extract_incidents(pdf_path)
            db_conn = createdb()
            populatedb(db_conn, incidents_df)

            # Generate visualizations and get status output
            status_output = cluster_and_visualize(incidents_df)
            return render_template('result.html', status_output=status_output.to_dict(orient='records'))

    return render_template('index.html')

@app.route('/result')
def result():
    # Provide default empty status_output if accessed directly
    return render_template('result.html', status_output=[])

if __name__ == '__main__':
    app.run(debug=True)