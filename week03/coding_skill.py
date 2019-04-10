import json
import sys


def coding_skill(file_name):
    with open(file_name) as f:
        data = json.load(f)

    best_in = dict()
    for human in data['people']:
        #print(human['first_name'], human['last_name'])
        for skill in human['skills']:
            if skill['name'] not in best_in.keys():
                best_in[skill['name']] = (skill['level'], human['first_name'] + ' ' + human['last_name'])
            elif best_in[skill['name']][0] < skill['level']:
                best_in[skill['name']] = (skill['level'], human['first_name'] + ' ' + human['last_name'])
    return best_in

if __name__ == '__main__':
    data = sys.argv[1]
    print(coding_skill(data))