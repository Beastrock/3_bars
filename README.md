# 3_bars
This script works with [Moscow bars json data base](http://data.mos.ru/opendata/7710881420-bary/ "download source").  
It calculates three things:  
* the biggest bar  
* the smallest bar   
* the nearest bar from  location inputted by user  
  
Quantity of seats is used to get the first two tasks of the script. 

## launching  
You can run the script using following command: python bars.py `<path_to_json_file>`  
## formula for calculating distance between two GPS coordinates
The third task is achieved with a haversine formula. The information about formula and calculations you can find [there(rus)](http://gis-lab.info/qa/great-circles.html) and [there(eng)](https://en.wikipedia.org/wiki/Haversine_formula).

