from mastodon import Mastodon
import json

def main():

    filename = 'test.json'
    f = open(filename, 'r')
    json_dict = json.load(f)
    print(json.dumps((json_dict), sort_keys=True, indent=4))


if __name__ == '__main__':
    main()
