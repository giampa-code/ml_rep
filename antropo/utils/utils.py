import json

# functions
## load json
def load_json(path):
    # Opening JSON file
    f = open(path)
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    # Closing file
    f.close()
    return data


# loading mean and std json for scaling 
mean_f = load_json('antropo/data/mean_f.json')
std_f = load_json('antropo/data/std_f.json')
mean_m = load_json('antropo/data/mean_m.json')
std_m = load_json('antropo/data/std_m.json')

## z-scale functions
def z_scale(variable, sex, value):
    """
    Given a value, the sex a variable name, return it z-scaled
    """

    if sex=='f':
        return (value-mean_f[variable])/std_f[variable]
    if sex=='m':
        return (value-mean_m[variable])/std_m[variable]