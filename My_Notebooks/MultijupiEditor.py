import json
import os
from pprint import pprint
import codecs
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
            newcell = []
            for item in cells:
                if item['cell_type'] == 'code':
                    del cells[x]
                    x += 1
                else:
                    for words in range(len(item['source'])):
                        if 'Solutions' in item['source'][words]:
                            del cells[x]['source'][-1]
                    x += 1
            # dump data into new file

            out_file = codecs.open(f"./My_Day{day}.ipynb", "w")
            json.dump(data, out_file, indent="")
    day += 1
