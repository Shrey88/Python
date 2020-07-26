# =====================================================================================================================
# we can get information on the current time zone via time.timezone and rime,tzedname now these aren't functions.
# timezone returns a number of seconds offset from UTC so in other words it will be negative fo country's east of the
# Greenwich Meridian and most of Western Europe  and positive for the country's west of Greenwich in the UK
#
# tzedname returns a tuple containing two strings the name of the non dst timezone and also the name of the dst timezone
# now before relying on the dst timezone name, we need to check the value of time.daylight, if this is non-zero then a
# dst timezone is defined and you can trust that at that point the second string in the tzedname tuple otherwise you
# shouldn't use the second string
# =====================================================================================================================
import time

# print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))
#
# print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))
#
#
# if time.daylight != 0:
#     print("\tDaylight Saving Time is in effect for this location")
#     print("\tThe DST timezone is " + time.tzname[1])
#
# print("Local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# print("UTC time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))


# ======================================================================================================================
# DATE - TIME
# these are naive as there's no time zone information associated with them, all we gor was the local time or the UTC
# times
# always work in UTC format, but convert it to local time when you want to display it to users
# pytz is there to help us and it provides a localized function that can be used to convert naive local datetime
# into an aware date time
# ======================================================================================================================
import datetime
print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
