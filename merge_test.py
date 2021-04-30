import os, glob
import pandas as pd
from statistics import mean
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:1pepper2@localhost:5432/covid_19_fl')

path = "data/"

all_files = glob.glob(os.path.join(path, "*.csv"))
df_from_each_file = (pd.read_csv(f) for f in all_files)
df_merged = pd.concat(df_from_each_file, ignore_index=True)
df_merged.to_csv( "merged.csv", index = False)


#Read list of counties in
county_df = pd.read_csv("County_Control.csv")

#Read merged Df
main_df = pd.read_csv("merged.csv")

county_list = []
vaccination_rate_list = []
days_left_list = []
county_population_list = []
percent_insured_list = []
poverty_rate_list = []
population_density_list = []


#Loop though all counties from control sheet
for x in range(len(county_df)):
    #Set County Name
    county_name = county_df["County"].iat[x]
    #Filter Main DF to only include that county
    temp_calc_df = main_df[main_df["County"] == str(county_name)]
    
#Here we can get a rolling average of any amount of days
#(this one is for 7 howver needs 8 days)
    temp_calc_df_short = temp_calc_df[-8:]
    #Create list to store vaccinations per day
    change_list = []
    #Calculate Changes in vaccinated people
    for y in range(len(temp_calc_df_short)-1):
        prev_day = int(str(temp_calc_df_short["Vaccinated"].iat[y]).replace(",", ""))
        current_day = int(str(temp_calc_df_short["Vaccinated"].iat[y+1]).replace(",", ""))
        
        change = current_day - prev_day
            
        change_list.append(change)

    #Average Vaccinations Per Day
    average_change = int(mean(change_list))

    #Get Latest Population
    county_population = temp_calc_df["Total_Population"].iat[-1]

    #Get Latest % Uninsured
    percent_insured = temp_calc_df["Percent_Uninsured"].iat[-1]
    
    #Get Latest Poverty Rate
    poverty_rate = temp_calc_df["Poverty Rate"].iat[-1]

    #Population Density
    population_density = temp_calc_df["Population_Density"].iat[-1]
    
#Here we can adjust the % needed to reach herd immunity
    herd_immunity = int(str(county_population).replace(",", "")) * float(0.9)

    #Get most current number of people vaccinated
    total_vaccinated = int(str(temp_calc_df["Vaccinated"].iat[-1]).replace(",",""))

    #Account for people already vaccinated
    herd_immunity_pop_needed = herd_immunity - total_vaccinated
    
    #Calculate Days Until Reaching Herd Immunity
    days_left = int(herd_immunity_pop_needed / average_change)

    #Append County and Days Left to a Dataframe
    county_list.append(county_name)
    vaccination_rate_list.append(average_change)
    days_left_list.append(days_left)
    county_population_list.append(county_population)
    percent_insured_list.append(percent_insured)
    poverty_rate_list.append(poverty_rate)
    population_density_list.append(population_density)

columns = ["County", "Vaccination_Rate", "Days_Left", "Population", "Percent_Uninsured", "Poverty_Rate", "Population_Density"]

#Add calculations to dataframe
days_left_df = pd.DataFrame(list(zip(county_list, vaccination_rate_list, days_left_list,
                                     county_population_list, percent_insured_list, poverty_rate_list,
                                     population_density_list)),columns = columns)

days_left_df.to_csv("days_left.csv", index = False)
    

days_left_df.to_sql('calculations_output', engine, if_exists='replace', index=False)
