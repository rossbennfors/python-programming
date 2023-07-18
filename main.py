# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification
from reporting import *
from monitoring import *
from intelligence import *
import requests

def main_menu():

    print("\u2022 R - Access the PR module \n\u2022 I - Access the MI module \n\u2022 M - Access the RM module \n\u2022 A - Print the about text \n\u2022 Q - Quit the application")
    

def reporting_menu():

    choice = input("\nWhat would you like to do with the data from the monitoring station and pollutant you are going to choose?\n\u2022 DA - See daily average\n\u2022 DM - See daily median\n\u2022 HA - See hourly average\n\u2022 MA - See monthly average\n\u2022 PH - See the peak hour and its value for a certain date\n\u2022 MV - See how many missing data values there are\n\u2022 FD - Fill missing data with a new value\n**enter B to go back to main menu**\n").upper()

    if choice == 'B':
        return

    station = input("Please enter a monitoring staion: ").capitalize()
    while station not in ['Harlington', 'Marylebone', 'Kensington']:
        print("\nInvalid option, please try again.")
        station = input("Please enter a monitoring staion; Harlington, Marylebone, Kensington: ").capitalize() 

    pol = input("Please choose a pollutant: ").lower()
    while pol not in ['no', 'pm10', 'pm25']:
        print("\nInvalid option, please try again.")
        pol = input("Please choose a pollutant: ").lower()

    if choice == 'DA':
        print(daily_average(data, station, pol))

    elif choice == 'DM':
        print(daily_median(data, station, pol))

    elif choice == 'HA':
        print(hourly_average(data, station, pol))

    elif choice == 'MA':
        print(monthly_average(data, station, pol))

    elif choice == 'PH':
        day = input("Please choose a date you would like to see: ")
        print(peak_hour_date(data, day, station, pol))

    elif choice == 'MV':
        print(count_missing_data(data, station, pol))

    elif choice == 'FD':
        new_val = input("What value would you like to replace missing data with? ")
        print(fill_missing_data(data, new_val, station, pol))

    else:
        print("Invalid option, please try again.")
    reporting_menu()

def monitoring_menu():

    choice = input("\nIn this section there are 4 functions to choose from:\n\u2022 1 - Most recent reading (updated hourly)\n\u2022 2 - Current averge for today\n\u2022 3 - Today's peak data\n\u2022 4 - function 4\n\u2022 5 - View a list of sites or pollutants\n**enter B to go back to main menu**\nWhat function would you like to look at? ").upper()
    if choice == '5':
        info_list = input('Would you like to see the list of sites or pollutants, type S or P? ').upper()
        if info_list == 'S':
            print(sites)
        elif info_list == 'P':
            print(species)
    else:
        if choice == 'B':
            return
        site_code = input('Please enter a site code: ').upper()
        while site_code not in sites:
            print("\nInvalid option, please try again.")
            site_code = input('Please enter a site code: ').upper()

        species_code = input('Please enter a pollutant: ').upper()
        while species_code not in species:
            print("\nInvalid option, please try again.")    
            species_code = input('Please enter a pollutant: ').upper()
        
        if choice == '1':
            print(most_recent_value(site_code, species_code))
        elif choice == '2':
            print(current_daily_average(site_code, species_code))
        elif choice == '3':
            print(peak_data(site_code,species_code))
        elif choice == '4':
            print('Sorry I did not get to make a 4th function :(')
        else:
            print('\nInvalid option, please try again.')

    monitoring_menu()


def intelligence_menu():
    
    choice = input('\nPlease choose from the options below:\n\u2022 1 - Create a black and white image to show the red pixels and returns a 2D binary image array of maps.png\n\u2022 2 - Create a black and white image to show the cyan pixels and returns a 2D binary image array of maps.png\n\u2022 3 - Create text file listing the connected components of red pixels and see its 2D binary image array\n\u2022 4 - Create text file listing the connected components of red pixels in descending orderof pixels and creates an image of the two biggest components\n**enter B to go back to main menu**\nWhat function would you like to look at? ').upper()

    if choice == 'B':
        return
    elif choice == '1':
        print(find_red_pixels())
    elif choice == '2':
        print(find_cyan_pixels())
    elif choice == '3':
        print(detect_connected_components())
    elif choice == '4':
        print(detect_connected_components_sorted())
    else:
        print('\nInvalid option, please try again.')
    
    intelligence_menu()

def about():
    
    print("\nThis is a program built for module ECM1400")
    print("My candidate number is: 239806")


if __name__ == '__main__':
    data = {
    "Harlington" : pd.read_csv('data/Pollution-London Harlington.csv'),
    "Marylebone" : pd.read_csv('data/Pollution-London Marylebone Road.csv'),
    "Kensington" : pd.read_csv('data/Pollution-London N Kensington.csv')
    }

    main_menu()
    option = input("Please select one of the options: ").upper()

    while True:
        if option == 'R':
            reporting_menu()

        elif option == 'I':
            intelligence_menu()

        elif option == 'M':
            GROUPNAME='London'
            groups = "http://api.erg.ic.ac.uk/AirQuality/Information/MonitoringSites/GroupName={GROUPNAME}/Json"    
            info = groups.format(
                GROUPNAME = GROUPNAME,
            )
            sites = []
            res = requests.get(info)
            group_info = res.json()['Sites']['Site']
            for x in group_info:
                sites.append(x['@SiteCode'])

            pols = "http://api.erg.ic.ac.uk/AirQuality/Information/Species/Json"    
            info = pols.format(
            
            )
            species = []
            res = requests.get(info)
            group_info = res.json()['AirQualitySpecies']['Species']
            for x in group_info:
                species.append(x['@SpeciesCode'])
            
            monitoring_menu()

        elif option == 'A':
            about()

        elif option == 'Q':
            print("\nThank you for using my program. Goodbye!\n")
            quit()

        else:
            print("\nInvalid option, please try again.")
        
        print()
        main_menu()
        option = input("Please select one of the options: ").upper()