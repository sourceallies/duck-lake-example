import requests

##
## Once duckdb httpfs fixes making a head request this can be dropped
##

def download_file(url, local_path):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(local_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

def model(dbt, session):
    csv_file = 'stg_iowa_checkbook.csv'
    download_file('https://data.iowa.gov/resource/cyqb-8ina.csv?fiscal_year=2020&fiscal_year_period=1&$limit=1000000000', csv_file)
    return session.sql(f"from '{csv_file}'")
