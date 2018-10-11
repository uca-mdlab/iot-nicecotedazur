import json
import requests
import sys
import time
import configparser

APIURL = 'https://api.nicecotedazur.org/nca/traffic/trafficflowobserved/'


def get_api_key(fname):
    config = configparser.ConfigParser()
    config.read(fname)
    return config['iotnca']['apikey']


def get_data(url, outfile):
    r = requests.get(url)
    return json.loads(r.content)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        exit('Usage:\n python3 {} conf_file runtime_in_hours outfile'.format(sys.argv[0]))
    conffile = sys.argv[1]
    hours_to_run = float(sys.argv[2])
    outfile = sys.argv[3]

    apikey = get_api_key(conffile)
    url = APIURL + '?api_key={}'.format(apikey)

    limit = int(60 * hours_to_run)

    run = 0
    res = []
    while run < limit:
        print('run {}/{}\r'.format(run, limit), end='\r')
        res.append(get_data(url, outfile))
        time.sleep(60)
        run += 1

    with open(outfile, 'w') as out:
        json.dump(res, out)
