# cis6930fa24 -- Project3

Name: Sai Sree Sadhan Polimera

# Assignment Description 

This project involves developing a Python-based application that integrates data visualization with a user-friendly web interface. The application is built to process incident data extracted from PDFs issued by the Norman, Oklahoma Police Department. The goal is to create meaningful insights through clustering and comparison visualizations while providing users with an intuitive way to explore the data.

The Incident Sumamry data can be accessed from Norman, Oklahoma police department activity reports [here](https://www.normanok.gov/public-safety/police-department/crime-prevention-data/department-activity-reports).

**Assignment Objective:**
The primary objective of this project is to build a data pipeline with the following capabilities:

1) Data Extraction:
      - Accept one or more NormanPD-style incident PDFs via a web interface (URL or file upload).
      - Process and extract relevant fields from the PDFs, including:
          - Date/Time
          - Incident Number
          - Location
          - Nature of the Incident
          - Incident ORI
2) Data Storage:
      - Store the extracted data in a structured format using an SQLite database.
      - Insert the cleaned data into the database for efficient querying.
3) Data Analysis and Visualizations:
      - Generate three distinct visualizations to summarize and interpret the data:
          - Visualization 1: Clustering of records based on their encoded incident nature.
          - Visualization 1.1: Clustering of incident records based on their nature and frequency (count).
          - Visualization 2: Bar graph comparing the frequency of different incident types.
          - Visualization 3: Pie chart illustrating the proportional distribution of incident types.
4) Interactive Web Interface:
      - Display the generated visualizations on a web page with descriptive summaries.
      - Show a status table listing the incident nature and its count in a clear and structured format.
   
**Requirements:**
1) Web Interface:
      - Create a user-friendly web application using Flask.
      - The interface should allow:
          - PDF URL input: Accept URLs pointing to NormanPD-style incident PDFs.
          - File upload: Allow users to upload one or more PDFs directly.
      - Display the results (visualizations and status output) on the same page.
2) Data Extraction:
      - Extract the following fields from the NormanPD-style PDFs:
          - Date/Time of the incident.
          - Incident Number.
          - Location.
          - Nature of the Incident.
          - Incident ORI (originating agency identifier).
      - Ensure robust handling of various PDF structures and errors (e.g., malformed PDFs or missing fields).
3) Data Storage:
      - Store the extracted data in a structured SQLite database.
      - Create a table with appropriate columns:
          - `incident_time`, `incident_number`, `incident_location`, `nature`, `incident_ori`.
      - Insert the extracted data into the database for querying and analysis.
4) Data Analysis and Visualizations:
      - Generate three distinct visualizations:
          - Visualization 1: Clustering of records based on encoded nature and other features.
          - Visualization 1.1: Clustering of nature and its count to show incident patterns.
          - Visualization 2: A bar graph comparing incident types and their frequency.
          - Visualization 3: A pie chart illustrating the proportional distribution of incident types.
      - Each visualization must:
          - Be saved in the /static directory for display in the web interface.
          - Include labels, legends, and appropriate axis titles for clarity.

# How to install
Install pipenv using the command: 

      pip install pipenv

Install urllib3 library using the command: 

      pipenv install urllib3

Install PyPdf library using the command: 

      pipenv install pypdf

Install Flask Web Framework using the command: 

      pipenv install flask

Install scikit-learn library using the command: 

      pipenv install scikit-learn

Install matplotlib library using the command: 

      pipenv install matplotlib

Install pytest testing framework using the command: 

      pipenv install pytest 

## How to run
To execute the project, navigate to the project directory and run the following commands:

1) To output a page use command:

         python project3/app.py

## Test Cases run
Running the following pipenv command runs the pytest cases. This project have 1 test cases.
command to run test cases: 

      pipenv run python -m pytest -v

## Functions
### app.py

This module serves as the main entry point for the Flask-based web application. The application allows users to upload or provide a URL for NormanPD-style incident PDFs, processes the data to extract relevant fields, generates visualizations, and displays the results on a web page.

Functions:
- index() -> Renders the main page and handles PDF uploads or URLs for processing.
- result() -> Displays the visualizations and the status table.

1) **index()**
- Renders the main page and handles data submission (via URL or file upload).
- If the method is POST:
    - Accepts a URL or file upload.
    - Processes the incident PDF to extract relevant data fields.
    - Generates visualizations (clustering, bar chart, pie chart).
    - Displays the results on the results page.
- Returns: Rendered HTML page with either the input form (GET) or the visualizations and table (POST).

2) **result()**
- Displays the results page with visualizations and the status table.
- If accessed directly, provides an empty status output.
- Returns: Rendered HTML page displaying visualizations and the incident summary table.

### clustering.py

- This module contains functions for data visualization and clustering analysis. 
- The functions generate visualizations for the extracted incident data, including:
    - Clustering of incidents.
    - Bar graph for incident type frequency.
    - Pie chart for proportional distribution of incidents.
- Functions:
    - cluster_and_visualize(incidents_df) -> Processes incident data and generates visualizations.
- Saves all the graphs as a PNG image in the `static` directory.

1) **cluster_and_visualize(incidents_df)**
- Processes the given incident data and generates the following visualizations:
    - Clustering of incidents based on encoded nature.
    - Clustering of incident records based on nature and count.
    - Bar graph comparing incident types and their frequencies.
    - Pie chart showing proportional distribution of incident types.
- Parameters:
    - incidents_df (pandas.DataFrame): DataFrame containing extracted incident data.
- Outputs:
    - Saves generated visualizations as PNG images in the `static` directory:
        - `cluster_plot.png` for clustering of incidents.
        - `nature_clustering.png` for nature and count clustering.
        - `bar_graph.png` for bar chart of incident types.
        - `pie_chart.png` for pie chart of incident type distribution.
- Saves all the graphs as a PNG image in the `static` directory.

### Templates
1) **index.html**

- This template renders the input form for uploading or providing a URL for incident PDFs.
- Features:
    - A text input for entering a URL.
    - A file upload button for uploading PDFs.
    - A submit button to process the data.

2) **result.html**

- This template displays the generated visualizations and the incident summary table.
- Features:
    - Visualization 1: Incident Clusters.
    - Visualization 1.1: Clustering of incident records based on nature and count.
    - Visualization 2: Comparison of incident types (bar graph).
    - Visualization 3: Incident nature distribution (pie chart).
    - A status table displaying the nature of incidents and their counts.

## Interface and Visualization

The application begins by launching a Flask web server, providing a user-friendly interface accessible via a local web address. The user can access the web interface at `http://127.0.0.1:5000`. On the input page, users can either enter a URL to a NormanPD-style incident PDF or upload a PDF file directly from their system. Upon submission, the application processes the provided PDF by extracting key data fields such as incident time, location, nature, and identifiers. The extracted data is then stored in an SQLite database for structured analysis. Simultaneously, the application performs data clustering and visualization, generating various graphs, including a clustering scatter plot, a bar graph comparing incident frequencies, and a pie chart for incident type distribution. Finally, the results—visualizations and a status table summarizing incident counts—are displayed on a results page, providing users with clear insights into the processed data.

![image](https://github.com/user-attachments/assets/110b60bd-7867-445a-bfec-8cce95d10187). 

Norman data URL used in the below screenshots: https://www.normanok.gov/sites/default/files/documents/2024-11/2024-11-02_daily_incident_summary.pdf

**Visualization 1: Incident Clusters**

This scatter plot provides a visual representation of how incidents are grouped based on their encoded nature and incident numbers. Each point in the graph represents a unique incident, with its position determined by the incident number (X-axis) and the encoded nature of the incident (Y-axis). The incidents are grouped into clusters using the K-Means clustering algorithm, with each cluster represented by a distinct color. The purpose of this visualization is to uncover relationships and patterns among different incidents. For instance, similar incident types, such as traffic violations or thefts, might group together in clusters, indicating shared characteristics. This visualization is particularly useful for identifying commonalities or anomalies in incident data.

![image](https://github.com/user-attachments/assets/82d52d49-188b-4817-b43f-6e6fd7504975)

**Visualization 1.1: Clustering of Incident Records (Nature and Count)**

This scatter plot focuses on clustering incident types based on their encoded nature and the frequency (count) of their occurrences. Each point in the graph represents a specific type of incident (e.g., theft, assault), and its position is determined by its encoded nature (X-axis) and the number of times it appears in the dataset (Y-axis). Using K-Means clustering, incident types with similar frequencies are grouped into clusters, with each cluster represented by a distinct color. This visualization helps highlight which incident types are common, rare, or fall into similar patterns of occurrence. For example, a high-frequency cluster might include traffic violations and theft, while lower-frequency clusters might include rare crimes like arson. This graph is valuable for prioritizing resources by identifying frequently occurring incident types.
![image](https://github.com/user-attachments/assets/eb239791-d118-4089-9a4b-1dd8091b0093)

**Visualization 2: Comparison of Incident Types**

The bar graph provides a straightforward yet powerful comparison of the frequency of different incident types. Each bar represents a unique incident type (e.g., theft, assault), and its height corresponds to the total number of times that type appears in the dataset. This visualization is particularly effective for identifying the most and least frequent incident types at a glance. For instance, a tall bar for "Traffic Violations" indicates its predominance in the dataset, while a shorter bar for "Assault" suggests its relative rarity. This visualization is useful for stakeholders to understand the distribution of incidents and make data-driven decisions, such as allocating resources to address the most frequent types of incidents.

![image](https://github.com/user-attachments/assets/ba14ca62-5003-4643-b0ff-5de114c3b05e)

**Visualization 3: Incident Nature Distribution**

The pie chart provides a proportional breakdown of the incident types in the dataset, highlighting how each type contributes to the total number of incidents. Each slice of the pie represents a specific incident type, with the size of the slice corresponding to its proportion in the dataset. For example, if "Theft" accounts for 25% of the total incidents, its slice will occupy a quarter of the chart. This visualization is particularly useful for understanding the composition of the dataset and identifying dominant incident types. It complements the bar graph by offering a more intuitive and holistic view of the data's overall distribution, helping stakeholders quickly assess which types of incidents dominate or are negligible in the dataset.

![image](https://github.com/user-attachments/assets/c6b50df1-6029-48bd-a9b3-ac1cfb5e8dfb)

Each visualization serves a unique purpose in exploring and understanding the dataset:
- Incident Clusters (1): Identifies patterns and relationships between individual incidents.
- Nature and Count Clustering (1.1): Groups incident types based on their frequency for better prioritization.
- Bar Graph (2): Highlights the most and least common incident types for actionable insights.
- Pie Chart (3): Offers a proportional overview of the dataset, helping to understand the composition of incidents.

### main.py
**main(url)**

The main.py script is the main entry point for the incident data extraction and processing application. It accepts a URL to an incident summary PDF and performs the following actions:
**Functionality:**
1) Download Incident Data: Fetches the incident summary PDF from the specified URL.
2) Extract Incident Data: Extracts relevant fields such as date, incident number, location, nature, and incident ORI from the PDF.
3) Create and Populate SQLite Database: Creates a new SQLite database and stores the extracted data in the database.
4) Print Incident Report: Outputs a summary of incidents, grouped by their nature, and displays how many times each nature appears.

Arguments:

    --incidents (required): The URL of the incident summary PDF.

Code Breakdown:
1) Command-line Parsing: Uses argparse to handle command-line arguments, where the user must specify the URL of the incident summary PDF.

        parser = argparse.ArgumentParser()
        parser.add_argument("--incidents", type=str, required=True, help="Incident summary URL.")
        args = parser.parse_args()

2) Main Function: The **main(url)** function contains the execution of the script, performing the following steps:
    - Fetches the PDF using **project3.fetch_incidents**.
    - Extracts incident data from the PDF using **project3.extract_incidents**.
    - Creates a new SQLite database using **project3.createdb**.
    - Inserts the extracted data into the database using **project3.populatedb**.
    - Finally, prints the summary report of incidents using **project3.status**.

All the functions referenced in the **main()** function, such as **fetch_incidents, extract_incidents, createdb, populatedb, and status**, are defined in the **project3.py** module.

### project3.py
1) **fetch_incidents(url)**
    - Downloads an incident summary PDF from the provided URL and saves it to a temporary file.
    - Parameters:
        - url: The URL of the incident summary PDF.
    - Returns: The file path of the saved PDF in a temporary location.

   In this project, the incident summary PDF is downloaded and stored temporarily using Python’s built-in **tempfile** module. The reason for choosing this approach is:
    - Dynamic File Management: By using **tempfile.NamedTemporaryFile**, the file is stored in a temporary directory (often /tmp in Linux-based systems or a similar temp directory in other operating systems) that is managed by the operating system. This ensures that files are automatically cleaned up when no longer needed.
    - Automatic Cleanup: While the **delete=False** option is used to keep the file for further processing, it can be easily cleaned up programmatically after the data has been extracted.
    - Security and Safety: Storing the file in a temporary location ensures that sensitive data (like incident summaries) is not permanently stored in the file system, reducing the risk of leaving behind sensitive or personal information.
    - Next Step Readability: The function returns the path to the temporary file, allowing subsequent methods (such as extract_incidents()) to read the file directly without requiring any complex file path configurations or hardcoded paths. This ensures the file is always accessible to the next function in the process.

2) **extract_incidents(pdf_file_path)**
    - Extracts incident data from the provided PDF file that is stored as a temp file from the **fetch_incident()** function and structures it into a pandas DataFrame.
    - Parameters:
        - pdf_file_path (str): The file path to the PDF containing the incident data.
    - Returns:
        - pandas.DataFrame: A DataFrame containing the extracted incident data, with columns:
            - incident_time: The date and time of the incident.
            - incident_number: The unique number identifying the incident.
            - incident_location: The location where the incident occurred.
            - nature: The nature of the incident (e.g., Theft, Vandalism).
            - incident_ori: The ORI (Originating Agency Identifier) associated with the incident.
    - This function reads the PDF using a layout-based extraction method to preserve the structure of the data and splits the text into relevant fields using regular expressions.
    - Header information is extracted only from the first page, while subsequent pages are processed for incident details.
    - Incident data is validated to ensure that each row contains at least three valid fields, and any rows missing fields or values are filtered out.
    - The **extract_incidents()** function utilizes **PyPDF** library and its **PdfReader** module to read and extract text content from the incident summary PDFs. This allows for precise text extraction across multiple pages, maintaining the layout and structure of the PDF for accurate data parsing.

4) **createdb()**
    - Creates an SQLite database and returns the connection object.
    - The database will contain a table named `incidents` with the specified schema.
    - Returns:
        - sqlite3.Connection: A connection object to interact with the SQLite database.
    - Directory Creation: The function first ensures that a resources directory exists in the project root directory. If the directory is missing, it creates it dynamically.
    - Database Creation: It creates a new SQLite database file (normanpd.db) in the resources directory. If an existing database with the same name is present, it deletes the old file to ensure a fresh start.
    - Return Value: The function returns a connection object to interact with the database, allowing other parts of the application to insert and query data.
    - Automatic Directory Management: This function dynamically creates the resources directory if doesn’t exist, providing a clean and organized storage location for the database file.
    - Fresh Database: To avoid conflicts with existing data, any existing database is deleted at the start of the script’s execution, ensuring that the data is always fresh.

5) **populatedb(conn, incidents_df)**
    - Inserts incident data from a pandas DataFrame into the SQLite database.
    - Parameters:
        - conn: The SQLite database connection object.
        - incidents_df: A pandas DataFrame containing incident data to be inserted.
    - This function reads each row from the DataFrame (which contains the incident data) and inserts it into the incidents table in the database.
    - Transaction Safety: The function uses a transaction mechanism where changes are committed to the database only after all rows are inserted. In case of an error, the changes are rolled back to prevent partial or corrupt data insertion to ensure the database integrity.
        - This function uses **commit()** to ensure all data is saved after the full DataFrame is inserted. If an error occurs, **rollback()** is used to undo any incomplete changes, maintaining database consistency.
    - Cursor Management: The function uses a cursor to execute SQL queries and ensures it is properly closed after data insertion is completed. 
  
6) **status(conn)**

    - Prints a summary of the nature of incidents and the number of times each has occurred.
    - The list is sorted alphabetically by the nature of the incident.
    - Parameters
        - conn: The SQLite database connection object.
    - The status() function generates a report summarizing the incidents stored in the database. It retrieves the count of each type of incident (grouped by its nature) and prints the results in alphabetical order.
    - The results are printed to the console, showing the incident nature and its corresponding count, separated by a pipe (|).

### test_functions.py
1) **test_fetch_incidents()**

   - Tests the fetch_incidents() function to ensure it correctly downloads a PDF from a given URL.

## Database Development
This project uses an SQLite database to store and manage the incident data extracted from the incident summary PDFs. The following details outline how the database is created, structured, and used within the project.

**Database Creation:**
The SQLite database is created dynamically when the script is executed. It is stored in the resources directory of the project, and the database file is named normanpd.db. If an existing database with the same name is found, it is deleted and replaced with a fresh instance to avoid duplication and ensure clean data storage.

The database is created using the **createdb()** function, which defines the schema for storing incident data in a single table named incidents.

**Table Schema:**
The incidents table is structured with the following columns:
  - incident_time (TEXT): The date and time the incident occurred.
  - incident_number (TEXT): A unique identifier for the incident.
  - incident_location (TEXT): The location where the incident took place.
  - nature (TEXT): The nature or type of the incident (e.g., Theft, Vandalism).
  - incident_ori (TEXT): The ORI (Originating Agency Identifier) code representing the agency handling the incident.

Each row in this table represents a unique incident, and the table is designed to efficiently store and query incident records.

**Data Insertion:**
Data is inserted into the database using the **populatedb()** function, which reads rows from the pandas DataFrame (populated with incident data) and inserts them into the incidents table. For each row in the DataFrame, the relevant data fields are mapped to the appropriate columns in the table. The insertion process is handled within a transaction, ensuring that if an error occurs, any changes are rolled back to maintain the integrity of the database.

**Transaction Management:**
To ensure data integrity, all operations with the database are handled within transactions. The script commits the transaction once all rows are successfully inserted into the database. If an error occurs during insertion, a rollback is performed to revert any partial changes, preventing corrupt or incomplete data from being stored.

**Cleanup and Maintenance:**
At the end of the script execution, temporary files (such as the downloaded PDF) are deleted, and the SQLite database remains for further querying or analysis. If the script is run again, the database will be re-created, overwriting the existing file to ensure no duplicate data is stored.

## Bugs and Assumptions
1) Assumption: The script assumes that all incident summary PDFs follow a consistent structure, including field headers, row spacing, and column formatting. Any deviation from this format may require modifications to the extraction logic.
2) Simple Incident Structures: It is assumed that the incident data in the PDF is expected to follow a simple, table-like structure. Complex incident descriptions spanning multiple lines or columns could result in data parsing errors or incorrect extractions.
3) Inconsistent PDF Formatting: If the structure of the PDF differs from the expected format (e.g., different column spacing, missing headers), the extraction process might fail or produce incorrect data.
4) PDF Layout Extraction Issues: The use of PyPDF's layout mode for text extraction may not perfectly capture complex layouts or images embedded within the PDF. This can cause misalignment in the extracted data fields.
5) Temporary File Cleanup: In case of a script failure or crash, the temporary files created for downloading PDFs may not be properly cleaned up, leaving residual files in the temp directory.