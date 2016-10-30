import json
import os.path
import sys
from math import sin, cos, atan2, radians, sqrt, fabs


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding="UTF-8") as file_handler:
        return json.load(file_handler)


def get_smallest_bar(bars):
    smallest_bar = min(bars, key=lambda bars: bars["Cells"]["SeatsCount"])
    return smallest_bar


def get_biggest_bar(bars):
    biggest_bar = max(bars, key=lambda bars: bars["Cells"]["SeatsCount"])
    return biggest_bar


def calculate_closest_bar(bars, user_latitude, user_longitude):
    def calculate_distance(bars):
        bar_longitude = bars["Cells"]["geoData"]["coordinates"][0]
        bar_latitude = bars["Cells"]["geoData"]["coordinates"][1]
        # sin and cos of latitudes
        cosl1 = cos(radians(user_latitude))
        cosl2 = cos(radians(bar_latitude))
        sinl1 = sin(radians(user_latitude))
        sinl2 = sin(radians(bar_latitude))
        # sin and cos of longitude difference
        longitude_delta = radians(bar_longitude - user_longitude)
        cos_delta = cos(longitude_delta)
        sin_delta = sin(longitude_delta)
        # haversine formula
        numerator = sqrt(pow(cosl2 * sin_delta, 2) +
                         pow(cosl1 * sinl2 - sinl1 * cosl2 * cos_delta, 2))
        denominator = sinl1 * sinl2 + cosl1 * cosl2 * cos_delta
        # result of haversine formula(angle)
        angular_disparity = atan2(numerator, denominator)
        earth_radius = 6372795  # in metres
        distance = angular_disparity * earth_radius
        return round(distance)

    nearest_bar = min(bars, key=calculate_distance)
    nearest_bar.update({"Distance": calculate_distance(nearest_bar)})
    return nearest_bar


def print_results(smallest_bar, biggest_bar, nearest_bar):
    print("The smallest bar \"{b[Name]}\":"
          " {b[SeatsCount]} seats.".format(b=smallest_bar["Cells"]))
    print("The biggest bar \"{b[Name]}\:"
          " {b[SeatsCount]} seats.".format(b=biggest_bar["Cells"]))
    print("The nearest bar \"{}\" is in {} metres."
          " Address to find it: {}".format(nearest_bar["Cells"]["Name"],
                                           nearest_bar["Distance"],
                                           nearest_bar["Cells"]["Address"]))


if __name__ == '__main__':
    json_filepath = sys.argv[1]
    bars = load_data(json_filepath)
    the_biggest = get_biggest_bar(bars)
    the_smallest = get_smallest_bar(bars)
    user_latitude = float(input("Input your latitude in degrees:\n"))
    user_longitude = float(input("Input your longitude in degrees:\n"))
    nearest_bar = calculate_closest_bar(bars, user_latitude, user_longitude)
    print_results(the_smallest, the_biggest, nearest_bar)
