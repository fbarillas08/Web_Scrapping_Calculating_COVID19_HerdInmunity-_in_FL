Objective:  Calculate the timeframe needed to reach a Herd Inmunity Threshold (HIT) based solely on vaccination against COVID-19 in each county in Florida.  

Data Source: CDC COVID-19 Vaccination Dashboard updated daily at 2000 EST

Methodology: 
  - Automatically scrape the CDC data to obtain the latest vaccinations per age group (Over 18 and Over 65) and total vaccinations
  - Move scrape data into a SQL database for storage
  - Extract values for computation including:
        - Number of new vaccinations
        - Total number of vaccinations per age group
  - Calculate vaccination rates per county based on the previous 7-days
  - Calculate number of days needed to reach the HIT
  - Save new daily data into dataframes and sql database
  - Convert data into json files for manipulation and calculations for html publication
  - Create an appropriate easy-to-read dashboard to drive the message

Challenges:
- Automating the scrapping 
- Manipulating the data from csv to json files for ease of publication
- css styling of the dashboard using bootstrap
