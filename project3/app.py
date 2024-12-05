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
    """
    Renders the main page and handles data submission (via URLs or multiple file uploads).
    """
    if request.method == 'POST':
        urls = request.form.get('urls')  # Get URLs (comma-separated)
        files = request.files.getlist('files')  # Get multiple uploaded files

        combined_data = pd.DataFrame()  # Initialize an empty DataFrame

        # Process URLs
        if urls:
            url_list = [url.strip() for url in urls.split(',')]
            for url in url_list:
                try:
                    pdf_path = fetch_incidents(url)  # Download PDF from URL
                    incidents_df = extract_incidents(pdf_path)
                    combined_data = pd.concat([combined_data, incidents_df], ignore_index=True)
                except Exception as e:
                    print(f"Error processing URL {url}: {e}")

        # Process Uploaded Files
        if files:
            for file in files:
                try:
                    pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                    file.save(pdf_path)  # Save uploaded file
                    incidents_df = extract_incidents(pdf_path)
                    combined_data = pd.concat([combined_data, incidents_df], ignore_index=True)
                except Exception as e:
                    print(f"Error processing file {file.filename}: {e}")

        # Ensure combined data is not empty
        if combined_data.empty:
            return "No valid data processed from the provided inputs."

        # Store data in SQLite and generate visualizations
        db_conn = createdb()
        populatedb(db_conn, combined_data)

        # Generate visualizations and get status output
        status_output = cluster_and_visualize(combined_data)
        return render_template('result.html', status_output=status_output.to_dict(orient='records'))

    return render_template('index.html')

@app.route('/result')
def result():
    # Provide default empty status_output if accessed directly
    return render_template('result.html', status_output=[])

if __name__ == '__main__':
    app.run(debug=True)