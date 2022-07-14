"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    start_time = arrow.get(brevet_start_time)
    if control_dist_km > brevet_dist_km:
        if control_dist_km < (brevet_dist_km + brevet_dist_km * .2):
            control_dist_km = brevet_dist_km
        else:
            return -1
    temp = 0
    tmp2 = control_dist_km


    if control_dist_km > 1000:
        tmp2 -= 1000
        temp = 200/34 + 200/32 + 200/30 + 400/28 + tmp2/26
    elif control_dist_km > 600:
        tmp2 -= 600
        temp = 200/34 + 200/32 + 200/30 + tmp2/28
    elif control_dist_km > 400:
        tmp2 -= 400
        temp = 200/34 + 200/32 + tmp2/30
    elif control_dist_km > 200:
        tmp2 -= 200
        temp = 200/34 + tmp2/32
    elif control_dist_km > 0:
        temp = tmp2/34
    else:
        pass
        #print("THIS CASE SHOULD NOT HAPPEN! Maybe you input a negative number?")

    hrs = int(temp)
    mins = (temp * 60) % 60
    mins = round(mins)
    secs = (temp * 3600) % 60

    control_open_time = start_time
    control_open_time = control_open_time.shift(hours=+hrs)
    control_open_time = control_open_time.shift(minutes=+mins)
    control_open_time = control_open_time.replace(second=0)
    #control_open_time = control_open_time.replace(microsecond=0)
    #control_open_time = control_open_time.shift(seconds=+secs)

    return control_open_time.isoformat()


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    start_time = arrow.get(brevet_start_time)

    temp = 0
    tmp2 = control_dist_km

    if control_dist_km > (brevet_dist_km + brevet_dist_km * .2):
        return -1
    else:
        if control_dist_km > 1000:
            tmp2 -= 1000
            temp = 600/15 + 400/11.428 + tmp2/13.333
        elif control_dist_km > 600:
            if control_dist_km == 1000:
                temp = 75
            else:
                tmp2 -= 600
                temp = 600/15 + tmp2/11.428
        elif control_dist_km > 60:
            if control_dist_km == 600:
                temp = 40
            elif control_dist_km == 400:
                temp = 27
            elif control_dist_km == 300:
                temp = 20
            elif control_dist_km == 200:
                temp = 13.5
            else:
                temp = tmp2/15
        elif control_dist_km > 0:
            temp = tmp2/20 + 1
        else:
            pass
            #print("THIS CASE SHOULD NOT HAPPEN! Maybe you input a negative number?")

        hrs = int(temp)
        mins = (temp * 60) % 60
        mins = round(mins)
        secs = (temp * 3600) % 60

        control_close_time = start_time
        control_close_time = control_close_time.shift(hours=+hrs)
        control_close_time = control_close_time.shift(minutes=+mins)
        control_close_time = control_close_time.replace(second=0)
        control_close_time = control_close_time.replace(microsecond=0)
        #control_close_time = control_close_time.shift(seconds=+secs)

        return control_close_time.isoformat()