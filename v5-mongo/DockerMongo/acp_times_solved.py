"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

# Minimum times as [(from_dist, to_dist, speed),
#                   (from_dist, to_dist, speed), ... ]
min_speed = [(0, 200, 15), (200, 400, 15), (400, 600, 15),
             (600, 1000, 11.428), (1000, 1300, 13.333)]
max_speed = [(0, 200, 34), (200, 400, 32), (400, 600, 30),
             (600, 1000, 28), (1000, 1300, 28)]

# Final control times (at or exceeding brevet distance) are special cases
final_close = {200: 13.5, 300: 20, 400: 27, 600: 40, 1000: 75}
max_dist = 1300


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
       in kilometers, which must be one of 200, 300, 400, 600, or
           1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string
           indicating the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    start_time = arrow.get(brevet_start_time)
    elapsed_hours = 0
    distance_left = control_dist_km
    for from_dist, to_dist, speed in max_speed:
        seg_length = to_dist - from_dist
        if distance_left > seg_length:
            elapsed_hours += seg_length / speed
            distance_left -= seg_length
        else:
            elapsed_hours += distance_left / speed
            hrs = int(elapsed_hours)
            mins = (elapsed_hours * 60) % 60
            mins = round(mins)
            secs = (elapsed_hours * 3600) % 60
            #open_time = start_time.replace(hour=elapsed_hours)
            open_time1 = start_time.replace(hour=hrs)
            open_time2 = open_time1.replace(minute=mins)
            return open_time2.isoformat()


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    start_time = arrow.get(brevet_start_time)
    if control_dist_km >= brevet_dist_km:
        duration = final_close[brevet_dist_km]
        hrs = int(duration)
        mins = (duration * 60) % 60
        mins = round(mins)
        secs = (duration * 3600) % 60
        #finish_time = start_time.replace(hour=duration)
        finish_time1 = start_time.replace(hour=hrs)
        finish_time2 = finish_time1.replace(minute=mins)
        return finish_time2.isoformat()
    elapsed_hours = 0
    distance_left = control_dist_km
    for from_dist, to_dist, speed in min_speed:
        seg_length = to_dist - from_dist
        if distance_left > seg_length:
            elapsed_hours += seg_length / speed
            distance_left -= seg_length
        else:
            elapsed_hours += distance_left / speed
            hrs = int(elapsed_hours)
            mins = (elapsed_hours * 60) % 60
            mins = round(mins)
            secs = (elapsed_hours * 3600) % 60
            #cut_time = start_time.replace(hour=elapsed_hours)
            cut_time1 = start_time.replace(hour=hrs)
            cut_time2 = cut_time1.replace(minute=mins)
            return cut_time2.isoformat()

    return arrow.now().isoformat()
