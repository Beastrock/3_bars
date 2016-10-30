# 3_bars
This script works with [Moscow bars json data base](http://data.mos.ru/opendata/7710881420-bary/ "download source").  
It calculates three things:  
* the biggest bar, using a quantity of seats count  
* the smallest bar, using the same count  
* the nearest bar from  location inputted by user  

## launching the script  
You can run the script using following command: python bars.py `<path_to_json_file>`  
## formula for calculating distance between two gps coordinates
The information about formula and calculations you can find [there(rus)](http://gis-lab.info/qa/great-circles.html) and [there(eng)](https://en.wikipedia.org/wiki/Haversine_formula)  

