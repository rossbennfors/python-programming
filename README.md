# python-programming
- Python program you read and calculate various averages, highest value etc from CSV, to read images (specific to ones attached), and do some calculations with data taken from LondonAir's AirQuality API
- All functions can be used by running the program and using the interactive terminal

# data
- 3 sets of pollution data: 
  - Harlington
  - Marylebone Road
  - North Kensington
- map.png:
  - map of roads (red) and pavements (cyan)
- map-red-pixels.png/map-cyan-pixels.png:
  - function in intellegence.py used to find all coloured pixels and make a new map of respective pixels 
- cc-top.png:
  - image of the two largest connected components (red pixels)
- cc-output-2a.txt/cc-output-2b.txt:
  - text files that display all the connected components with their size
  - 2b is the same as 2a but sorted in size of largest component to smallest

# main.py
- Contains the functions that make up the interactive termial

# intelligence.py
- Contains the functions that deal with the map.png eg creating the new map images, finding connected components etc

# monnitoring.py
- Contatains the functions that use the LondonAir API to make various calculations on data from a selection of available postcodes

# reporting.py
- Contains all the functions that manipulate the CSV data for the three weather stations

# utils.py
- Contains a few basic calulation functions 
