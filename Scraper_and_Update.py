import re
import os
import glob
import time
import random
import string
import urllib
import requests
import numpy as np
import pandas as pd
from datetime import date
from statistics import mean
from datetime import datetime
from selenium import webdriver
from sqlalchemy import create_engine
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec



#Scrape New Data

#**** NEED LOGIC TO NOT REPEAT A DATE SCRAPED and TO NOT MISS A DATE****#

def get_county_data():
    driver_path = "chromedriver.exe"
    #Start Chrome Maximized
    opts = Options()
    opts.add_argument("--start-maximized")

    #Start Chrome Driver and open website
    driver = webdriver.Chrome(executable_path=driver_path, options=opts)
    driver.get("https://covid.cdc.gov/covid-data-tracker/#county-view")

    while True:
        try:
            time.sleep(1)
            WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="maincontent"]/div[1]')))
        except:
            break

    #Loop this for each state 
    WebDriverWait(driver, 15).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="list_select_state"]'))).click()

    time.sleep(1)
    WebDriverWait(driver, 15).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="list_select_state"]/option[11]'))).click()

    time.sleep(1)

    county_list = []
    level_of_transmission_list = []
    date_list = []
    case_rate_list = []
    total_population_list = []
    percentage_of_total_pop_list = []
    pop_over_18_list = []
    percentage_of_pop_over_18_list = []
    pop_over_65_list = []
    percentage_of_pop_over_65_list = []
    total_population_2019_list = []
    population_density_2019_list = []
    avg_hh_size_list = []
    percent_uninsured_2019_list = []
    poverty_rate_2019_list = []
    percent_65_plus_list = []
    svi_rank_list = []
    ccvi_score_list = []
    Metro_status_list = []
    NCHS_status_list = []

    countt_scraoe = "not complete"
    q = int(2)
    while countt_scraoe == "not complete":
        #Scroll to it
        target = driver.find_element_by_xpath('//*[@id="list_select_county"]')
        actions = ActionChains(driver)
        actions.move_to_element(target)
        actions.perform()

        #Loop this for each county
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="list_select_county"]'))).click()

        county_name = driver.find_element_by_xpath('//*[@id="list_select_county"]/option['+str(q)+']').text
        print("Scraping " + str(county_name))


        WebDriverWait(driver, 15).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="list_select_county"]/option['+str(q)+']'))).click()

        time.sleep(1)
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="datanote"]'))).click()

        while True:
            try:
                time.sleep(1)
                WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="maincontent"]/div[1]')))
            except:
                break

        #Vaccination Data
        #Scroll to it
        target = driver.find_element_by_xpath('//*[@id="people-vaccinated-information"]/div/div[1]/div/div/div[2]/div[2]/div')
        actions = ActionChains(driver)
        actions.move_to_element(target)
        actions.perform()

        time.sleep(3)
        #Scroll to it
        total_population = driver.find_element_by_xpath('//*[@id="people-vaccinated-information"]/div/div[1]/div/div/div[2]/div[2]/div').text

        percentage_of_total_pop = driver.find_element_by_xpath('//*[@id="people-vaccinated-information"]/div/div[1]/div/div/div[3]/div[2]/div').text

        pop_over_18 = driver.find_element_by_xpath('//*[@id="people-vaccinated-information"]/div/div[1]/div/div/div[4]/div[2]/div').text

        percentage_of_pop_over_18 = driver.find_element_by_xpath('//*[@id="people-vaccinated-information"]/div/div[1]/div/div/div[5]/div[2]/div').text

        pop_over_65 = driver.find_element_by_xpath('//*[@id="people-vaccinated-information"]/div/div[1]/div/div/div[6]/div[2]/div').text

        percentage_of_pop_over_65 = driver.find_element_by_xpath('//*[@id="people-vaccinated-information"]/div/div[1]/div/div/div[7]/div[2]/div').text

        
        total_population_list.append(total_population)
        percentage_of_total_pop_list.append(percentage_of_total_pop)
        pop_over_18_list.append(pop_over_18)
        percentage_of_pop_over_18_list.append(percentage_of_pop_over_18)
        pop_over_65_list.append(pop_over_65)
        percentage_of_pop_over_65_list.append(percentage_of_pop_over_65)
        

        #Community Charactaristics Data

        #Scroll to it
        target = driver.find_element_by_xpath('//*[@id="total_population_2019"]')
        actions = ActionChains(driver)
        actions.move_to_element(target)
        actions.perform()


        total_population_2019 = driver.find_element_by_xpath('//*[@id="total_population_2019"]').text

        population_density_2019 = driver.find_element_by_xpath('//*[@id="population_density_2019"]').text

        avg_hh_size = driver.find_element_by_xpath('//*[@id="avg_hh_size"]').text

        percent_uninsured_2019 = driver.find_element_by_xpath('//*[@id="percent_uninsured_2019"]').text

        poverty_rate_2019 = driver.find_element_by_xpath('//*[@id="poverty_rate_2019"]').text

        percent_65_plus = driver.find_element_by_xpath('//*[@id="percent_65_plus"]').text

        svi_rank = driver.find_element_by_xpath('//*[@id="svi_rank"]').text

        ccvi_score = driver.find_element_by_xpath('//*[@id="ccvi_score"]').text

        Metro_status = driver.find_element_by_xpath('//*[@id="Metro_status"]').text

        NCHS_status = driver.find_element_by_xpath('//*[@id="NCHS_status"]').text



        total_population_2019_list.append(total_population_2019)
        population_density_2019_list.append(population_density_2019)
        avg_hh_size_list.append(avg_hh_size)
        percent_uninsured_2019_list.append(percent_uninsured_2019)
        poverty_rate_2019_list.append(poverty_rate_2019)
        percent_65_plus_list.append(percent_65_plus)
        svi_rank_list.append(svi_rank)
        ccvi_score_list.append(ccvi_score)
        Metro_status_list.append(Metro_status)
        NCHS_status_list.append(NCHS_status)


        #Scroll to it
        target = driver.find_element_by_xpath('//*[@id="county-level-latest-header-icon"]')
        actions = ActionChains(driver)
        actions.move_to_element(target)
        actions.perform()


        target = driver.find_element_by_xpath('//*[@id="county-level-latest-header-icon"]').click()


        errors = "none"
        x = int(1)
        while errors == "none":
            
            try:

                county = driver.find_element_by_xpath('//*[@id="county-level-latest-table"]/tbody/tr['+str(x)+']/td[1]').text
                level_of_transmission = driver.find_element_by_xpath('//*[@id="county-level-latest-table"]/tbody/tr['+str(x)+']/td[2]').text
                dater = driver.find_element_by_xpath('//*[@id="county-level-latest-table"]/tbody/tr['+str(x)+']/td[3]').text
                #Out of 100k
                case_rate = driver.find_element_by_xpath('//*[@id="county-level-latest-table"]/tbody/tr['+str(x)+']/td[4]').text        

                
                if str(county).lower() in str(county_name).lower():
                    level_of_transmission_list.append(level_of_transmission)
                    county_list.append(county)
                    date_list.append(dater)
                    case_rate_list.append(case_rate)
                    
            except:
                try:
                    county = driver.find_element_by_xpath('//*[@id="county-level-latest-table"]/tbody/tr['+str(x)+']/td[1]').text
                    level_of_transmission = driver.find_element_by_xpath('//*[@id="county-level-latest-table"]/tbody/tr['+str(x)+']/td[2]').text
                    dater = driver.find_element_by_xpath('//*[@id="county-level-latest-table"]/tbody/tr['+str(x)+']/td[3]').text
                    #Out of 100k
                    case_rate = driver.find_element_by_xpath('//*[@id="county-level-latest-table"]/tbody/tr['+str(x)+']/td[4]').text        

                    
                    
                    if str(county).lower() in str(county_name).lower():
                        level_of_transmission_list.append(level_of_transmission)
                        county_list.append(county)
                        date_list.append(dater)
                        case_rate_list.append(case_rate)
                except:
                    errors = "yes"
                    print("Scraping Completed")
                    pass
                    


            x = x + 1
        q = q + 1


        columns = ["County",
                   "Level_Of_Transmission",
                   "Date_Updated",
                   "Infection_Rate",
                   "Vaccinated",
                   "Vaccinated_Percent",
                   "Over_18_Vacc",
                   "Over_18_Vacc_Percent",
                   "Over_65_Vacc",
                   "Over_65_Vacc_Percent",
                   "Total_Population",
                   "Population_Density",
                   "Avg_HH_Size",
                   "Percent_Uninsured",
                   "Poverty Rate",
                   "Over_65"]

        #Add all lists scraped to dataframe
        county_data_df = pd.DataFrame(list(zip(county_list,
                                               level_of_transmission_list,
                                               date_list,
                                               case_rate_list,
                                               total_population_list,
                                               percentage_of_total_pop_list,
                                               pop_over_18_list,
                                               percentage_of_pop_over_18_list,
                                               pop_over_65_list,
                                               percentage_of_pop_over_65_list,
                                               total_population_2019_list,
                                               population_density_2019_list,
                                               avg_hh_size_list,
                                               percent_uninsured_2019_list,
                                               poverty_rate_2019_list,
                                               percent_65_plus_list)), columns = columns)
        
        today = date.today()

        county_data_df.to_csv("data//"+str(today)+".csv")

        print("Finished Scraping " + str(county_name))


def merge_and_upload():

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
        
    #Send Df to SQL database - replace if already in and set index to false
    days_left_df.to_sql('calculations_output', engine, if_exists='replace', index=False)


    
get_county_data()
merge_and_upload()
