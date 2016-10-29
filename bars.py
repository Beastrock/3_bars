import json
import os.path
import sys
from math import asin, acos, atan2, radians, sqrt


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
        EARTH_RADIUS = 6371e3
        bar_coordinates = bars["Cells"]["geoData"].get('coordinates')
        bar_latitude = bar_coordinates[0]
        bar_longitude = bar_coordinates[1]
        fi1 = radians(user_longitude)
        fi2 = radians(bar_longitude)
        delta_fi = radians(bar_latitude - user_latitude)
        delta_lambda = radians(bar_longitude - user_longitude)
        # calculate a - the square of half the chord length between the points.
        a = (asin(delta_fi / 2) ** 2) * asin(delta_fi / 2) \
            + acos(fi1) * acos(fi2) * (asin(delta_lambda / 2) ** 2)
        # calculate c - the angular distance in radians
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        # calculate d - the desired length between bar and user
        d = int(EARTH_RADIUS * c)
        return d

    nearest_bar = min(bars, key=calculate_distance)
    distance = {"Distance": calculate_distance(nearest_bar) / 1000}
    nearest_bar.update(distance)
    return nearest_bar


def print_results(smallest_bar, biggest_bar, nearest_bar):
    print("The smallest bar \"{b[Name]}\" +"
          "There are {b[SeatsCount]} seats.".format(b=smallest_bar["Cells"]))
    print("The biggest bar \"{b[Name]}\"."
          " There are {b[SeatsCount]} seats.".format(b=biggest_bar["Cells"]))
    print("The nearest bar, \"{}\", is by {} km. "
          "Address to find it: {}".format(nearest_bar["Cells"]["Name"],
                                          nearest_bar["Distance"],
                                          nearest_bar["Cells"]["Address"]))


if __name__ == '__main__':
    json_filepath = "bars.json"
    bars = load_data(json_filepath)
    user_longitude, user_latitude = input().split()
    the_biggest = get_biggest_bar(bars)
    the_smallest = get_smallest_bar(bars)
    user_longitude = 55.755797
    user_latitude = 37.408770
    nearest_bar = calculate_closest_bar(bars, user_latitude, user_longitude)
    print_results(the_smallest, the_biggest, nearest_bar)
