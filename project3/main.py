import argparse
import project3

def main(url):
    # Download data
    incident_data = project3.fetch_incidents(url)

    # Extract data
    incidents = project3.extract_incidents(incident_data)
	
    # Create new database
    db = project3.createdb()
	
    # Insert data
    project3.populatedb(db, incidents)
	
    # Print incident counts
    project3.status(db)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, help="Incident summary url.")
     
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)