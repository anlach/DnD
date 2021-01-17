from IPython import embed
import numpy as np
import re


def roll(specs):
    """
    Rolls dice when provide with a specification such as
    "2d8,3d10,1d100"
    """
    results = []
    matches = re.findall("(\d+d\d+)", specs)
    if len(matches) == 0:
        raise Exception("No dice! No matches in specs")
    for spec in matches:
        m = re.match("(\d+)d(\d+),?",spec)
        for d in range(int(m.groups()[0])):
            top = int(m.groups()[1])
            if top == 10:
                r = np.random.choice(range(10))
            else:
                r = np.random.choice(range(1,top+1))
            print(f"d{top}: {r}\n")
            results.append(r)
    return np.array(results)
