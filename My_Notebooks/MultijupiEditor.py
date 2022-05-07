import json
import os
from pprint import pprint
import codecs

# Start on day 2 cause I made this on my second day.
day = 2

for filename in os.scandir("../notebooks/"):
    x = 0
    if filename.is_file():
        with codecs.open(filename.path, 'r') as r:
            # load data in json to manipulate
            data = json.load(r)
            # items in data all tuples
            tupl, v1, v2, v4 = data.items()
            # cells is a list of dictionaries
            cells = tupl[1]
            for item in cells:
                if item['cell_type'] == 'code':
                    del cells[x]
                    x += 1
                else:
                    try:
                        # trys to remove solutions if its not there then continue
                        if item['cell_type'] == 'markdown':
                            cells[x]['source'].remove('**Solutions:**')
                        else:
                            x += 1
                            continue
                    except ValueError:
                        x += 1
                        continue
                    x += 1

            # dump data into new file
            out_file = codecs.open(f"./My_Day{day}.ipynb", "w")
            json.dump(data, out_file, indent="")

    day += 1
