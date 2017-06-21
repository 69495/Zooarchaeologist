import json
from datetime import datetime

def jsoner(data,filename_ahead):

    time = datetime.now().strftime("%Y-%m-%d-%H%M")
    filename = filename_ahead + "_" + time + "_.json"
    with open(filename, "w") as fp:
            json.dump(data,fp)

    print("complete!")

if __name__ == '__out_json__':
    out_json()
