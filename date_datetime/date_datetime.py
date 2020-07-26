import pytz
import datetime

country = "Europe/Moscow"

# ====================================
# pytz only deals with time zone information
# by using pytz to create a tzinfo object
# ====================================
# tz_to_display = pytz.timezone(country)

# ====================================
# we use the above tzinfo object to calculate
# the local time in any country, so you could
# change this to any country and do the same
# ====================================
# local_time = datetime.datetime.now(tz=tz_to_display)
# print("The time in {} is {}".format(country, local_time))
# print("UTC is {}".format(datetime.datetime.utcnow()))


# ====================================
# print entire list of valid strings that
# pytz.timezone method accepts quite easily
# ====================================
# for x in pytz.all_timezones:
#     print(x)

# ====================================
# displaying the country names
# ====================================
# for x in sorted(pytz.country_names):
#     print(x + ": " + pytz.country_names[x])

# ===================================
# displaying the country names and the timezones
# when it hits the key BV(Bouvet Island) for which there is no time zone
# timezone data is coming from database that's maintained by IANA in which internet assigned names authority
# now its referred as Olsen database and that's named after its creator Arthur David Olsen
# so instead of crashing/terminating we can make use of get operation which returns none in the case of
# there being a to,e zone nonexistent for a particular country
# ===================================
# for x in sorted(pytz.country_names):
#     print("{}: {}: {}".format(x, pytz.country_names[x], pytz.country_timezones[x]))

# ===================================
# using dictionary
# ===================================
# for x in sorted(pytz.country_names):
#     print("{}: {}: {}".format(x, pytz.country_names.get(x), pytz.country_timezones.get(x)))

