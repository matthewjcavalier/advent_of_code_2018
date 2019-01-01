"""
Advent of Code 2018 problem 1
"""

def tune(change_list):
    """
    go through the list and set the tune
    """
    current_tune = 0
    for item in change_list:
        current_tune = tune_by_string(current_tune, item)
    return current_tune

def dupe_tune(change_list):
    """
    tune the station looking for the resulting station that is
    tuned to twice
    """
    station_map = set()
    current_tune = 0
    station_found = False
    while not station_found:
        for item in change_list:
            current_tune = tune_by_string(current_tune, item)
            if current_tune in station_map:
                station_found = True
                break
            station_map.add(current_tune)
    return current_tune


def tune_by_string(current_tune, instruciton):
    '''
    Either add to or subtract from the current_tune based upon
    if the instruction contains a +/- and return the new tune
    '''
    if '+' in instruciton:
        current_tune = current_tune + int(instruciton.replace('+', ''))
    else:
        current_tune = current_tune - int(instruciton.replace('-', ''))
    return current_tune


lines = []
with open('one_input.txt', 'r') as f:
    for line in f:
        lines.append(line)
f.close()

print(tune(lines))
print(dupe_tune(lines))
