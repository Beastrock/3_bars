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
    # TODO:Сделать хороший вывод с помощью format
    return smallest_bar["Number"]


def get_biggest_bar(bars):
    biggest_bar = max(bars, key=lambda bars: bars["Cells"]["SeatsCount"])
    return biggest_bar["Number"]


def calculate_closest_bar(bars):
    # user_longitude, user_latitude = raw_input().split()
    user_longitude = 55.755797
    user_latitude = 37.408770
    def calculate_distance(bars):
        EARTH_RADIUS = 6371e3  # metres
        bar_coordinates = bars["Cells"]["geoData"].get('coordinates')
        bar_longitude, bar_latitude = bar_coordinates[0],bar_coordinates[1]
        fi1 = radians(user_longitude) # что это за угол
        fi2 = radians(bar_longitude)  #  а это и так далее TODO: расставить коменты
        delta_fi = radians(bar_latitude - user_latitude)
        delta_lambda = radians(bar_longitude - user_longitude)
        a = (asin(delta_fi / 2) ** 2) * asin(delta_fi / 2) \
            + acos(fi1) * acos(fi2) * (asin(delta_lambda / 2) ** 2)
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        d = int(EARTH_RADIUS * c)
        return d
    nearest_bar = min(bars, key=calculate_distance)
    return nearest_bar


def print_results():
    return


if __name__ == '__main__':
    json_filepath = "bars.json"
    bars = load_data(json_filepath)
    # print(get_smallest_bar(bars))
    # print(get_biggest_bar(bars))
    # print(input())
    # print (bars[1]["Number"])
    # print (bars[0]["Cells"])
    # print(bars[0]["Cells"]["SeatsCount"])
    nearest_bar = calculate_closest_bar(bars)
    print (nearest_bar)
    print (nearest_bar["Cells"]["geoData"]["coordinates"][0])
    print (nearest_bar["Cells"].get("AdmArea"))
    print(nearest_bar["Cells"].get("Name"))
