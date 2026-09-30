"""creating a function add_time for time calculator project that takes a 
   initial time and duration to give the resulting time"""

def add_time(start, duration, starting_day=None):
    # Days of the week
    days= ["Monday", "Tuesday","Wednesday", "Thursday",
            "Friday" , "Saturday", "Sunday"]

    # read the start time, split the start time
    parts= start.split(" ")
    clock=  parts[0]
    period= parts[1]

    clock_parts = clock.split(":")
    hr=int(clock_parts[0])
    min= int(clock_parts[1])

    # changing to 24-hour time
    if period == "PM" and hr != 12:
        hr = hr +  12
    if period =="AM" and hr == 12:
        hr =0

    # 3read duration, split the duration to hr and min
    dur_parts =duration.split(":")
    dur_hr =int(dur_parts[0])
    dur_min= int(dur_parts[1])

    # add the minutes and hours
    new_hr= hr +dur_hr
    new_min=min + dur_min

    #if minuts >= 60, add one hr
    if new_min >= 60:
        new_min= new_min - 60
        new_hr= new_hr +1

    # no of days that passed
    days_later = new_hr //24
    new_hr = new_hr %24

    #change back to 12-hour time
    if new_hr >=12:
        new_period = "PM"
    else:
        new_period ="AM"

    if new_hr ==0:
        new_hr =12
    elif new_hr > 12:
        new_hr = new_hr - 12

    #build the time text
    if new_min <10:
        min_text = "0" + str(new_min)
    else:
        min_text = str(new_min)

    new_time = str(new_hr) + ":" + min_text + " " +new_period

    # add the day of week, if given
    if starting_day != None:
        day =starting_day.capitalize()
        position = days.index(day)
        new_position = (position + days_later) %7
        new_time =new_time + ", " + days[new_position]

    #add the days-later
    if days_later ==1:
        new_time = new_time + " (next day)"
    elif days_later >1:
        new_time=  new_time + " (" +str(days_later) + " days later)"

    return new_time

#print result
if __name__ == "__main__":
    print(add_time("3:30 PM", "2:12"))
    print(add_time("11:55 AM", "3:12"))
    print(add_time("2:59 AM", "24:00"))
    print(add_time("11:59 PM", "24:05"))
    print(add_time("3:30 PM", "24:00", "Monday"))
    print(add_time("8:16 PM", "466:02"))