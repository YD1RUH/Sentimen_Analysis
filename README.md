# Sentimen_Analysis
## Depedencies
1. install python3: [download python](https://www.python.org/downloads/)
2. install python3 selenium: ```python3 -m pip install selenium```
3. install orange3: [download orange3](https://orangedatamining.com/download/)

## How to use
1. run ```crawl.py```, don't forget configura ```line 12``` for path chromedirver.exe and ```line 26``` for search youtube \(not link video\), chrome driver will choose the first video on the page serach result.
2. open orange3 data mining and open ```sentiment_indonesia.ows```.
3. on file input orange3, choose ```crawl.csv```, then open widget ```save data``` and save output process with name ```sentiment_output.csv```.
4. then run ```result.py``` to labeled every comment (if sentiment < 0 is negative, sentiment = 0 is neutral, sentiment > 0 is positive)
