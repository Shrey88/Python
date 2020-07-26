# =======================================================================================
# create a program that allows user to choose one of
# 9 time zones from a menu. You can choose any zones
# you want from the all_timezones list
#
# The program will then display the time in that timezone,
# as well as local time and UTC time
#
# entering 0 as the choice will quit the program.
#
# display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.
# =======================================================================================

import datetime
import pytz

country_timezone = {"Andorra": "Europe/Andorra",
                    "United Arab Emirates": "Asia/Dubai",
                    "Belgium": "Europe/Brussels",
                    "Germany": "Europe/Berlin",
                    "India": "Asia/Kolkata"}

country_code = {"AD": "Andorra",
                "AE": "United Arab Emirates",
                "BE": "Belgium",
                "DE": "Germany",
                "IN": "India"}

country_list = {1: "AD",
                2: "AE",
                3: "BE",
                4: "DE",
                5: "IN"}


print("\t\t1. Andorra")
print("\t\t2. United Arab Emirates")
print("\t\t3. Belgium")
print("\t\t4. Germany")
print("\t\t5. India")
print("\t\t6. Quit")
print("Please select the timezone : ", end='')
selection = int(input())

if selection != 0:
    if selection in country_list.keys():
        print("Time Zone : ", country_timezone.get(country_code.get(country_list.get(selection))))
        print("World Time : ", datetime.datetime.now(tz=pytz.timezone(country_timezone.get(country_code.get(country_list.get(selection))))).strftime('%A %d-%m-%Y %H:%M:%S %z'),
              datetime.datetime.now(tz=pytz.timezone(country_timezone.get(country_code.get(country_list.get(selection))))).tzname())

        print("Local Time : ", datetime.datetime.now().strftime('%A %d-%m-%Y %H:%M:%S'))

        print("UTC Time : ", datetime.datetime.utcnow().strftime('%A %d-%m-%Y %H:%M:%S'))
    else:
        print("Invalid Selection")
else:
    print("End Of Program")
