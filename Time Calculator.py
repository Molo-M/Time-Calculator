def add_time(start, duration, d=False):

    # Convert day and time into numerical values
    convert_day = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6,
                   'Sunday': 7}
    convert_time = {12: '12', 13: 1, 14: 2, 15: 3, 16: 4, 17: 5, 18: 6, 19: 7, 20: 8, 21: 9, 22: 10, 23: 11}

    x_hr = 0
    n_day = 0
    new_time = ''

    # Calculate Time
    start = start.split()
    meridiem = start[1]
    fst_time = start[0]
    fst_time = fst_time.split(':')
    sec_time = duration.split(':')

    # Calculate minutes
    st_min = int(fst_time[1])
    sec_min = int(sec_time[1])
    new_min = (st_min + sec_min)
    while new_min > 59:
        x_hr += 1
        new_min -= 60
    if new_min < 10:
        new_min = '0' + str(new_min)
    else:
        new_min = str(new_min)

    # Calculate hour
    st_hr = int(fst_time[0])
    sec_hr = int(sec_time[0]) + x_hr
    new_hr = (st_hr + sec_hr)
    while new_hr >= 24:
        n_day += 1
        new_hr -= 24

    if 12 < new_hr < 24 and meridiem == 'AM':
        new_hr = convert_time[new_hr]
        new_hr = str(new_hr)
        new_time += new_hr + ':'
        new_time += new_min + ' PM'
    elif 12 < new_hr < 24 and meridiem == 'PM':
        n_day += 1
        new_hr = convert_time[new_hr]
        new_hr = str(new_hr)
        new_time += new_hr + ':'
        new_time += new_min + ' AM'
    elif new_hr == 12 and meridiem == 'AM' and sec_hr != 0:
        new_hr = str(new_hr)
        new_time += new_hr + ':'
        new_time += new_min + ' ' + 'PM'
    elif new_hr == 12 and meridiem == 'PM' and sec_hr != 0:
        n_day += 1
        new_hr = convert_time[new_hr]
        new_time += new_hr + ':'
        new_time += new_min + ' ' + 'AM'

    elif new_hr <= 11:
        new_hr = str(new_hr)
        new_time += new_hr + ':'
        new_time += new_min + ' ' + meridiem

    # Calculate Days
    if d:
        # Convert day of the week into proper name
        day = d.lower()
        day_m = list(day)
        day_m[0] = day_m[0].upper()
        day = ''.join(day_m)

        day_val = convert_day[day]
        next_day = day_val + 1
        n_day = int(n_day) + day_val
        x_day = str(n_day - day_val)
        fin_day_val = n_day
        while fin_day_val > 7:
            fin_day_val -= 7

        for k, v in convert_day.items():
            if v == fin_day_val:
                fin_day = str(k)
        if n_day == day_val:
            new_time += ', ' + fin_day
        elif n_day == next_day:
            new_time += ', ' + fin_day + ' (next day)'
        else:
            new_time += ', ' + fin_day + ' (' + x_day + ' days later)'
        return new_time
    if not d:
        if n_day == 1:
            new_time += ' (next day)'
        elif n_day > 1:
            n_day = str(n_day)
            new_time += ' (' + n_day + ' days later)'
        return new_time


print(add_time("11:59 PM", "24:05", "Wednesday"))
print(add_time("11:00 PM", "2:00", 'tuesday'))
