import pickle
import sys
import json

def process_token(token):
    if (token[0], token[-1]) == ('"', '"'):
        return token[1:-1]
    return '<%s>' % token

def process_body(body):
    assert isinstance(body, list)
    return [process_token(token) for token in body]


def process_grammar(gv):
    keys = [k for k in gv.keys()]
    #for k in gv: print(gv[k].pretty_print())
    my_dict = {}
    for k in gv:
        v = gv[k]
        key = v.start
        my_dict[process_token(key)] = [process_body(b) for b in v.bodies]
    return my_dict


def main(grammar_file):
    with open(grammar_file, 'rb') as f:
        x = pickle.load(f)
        d = process_grammar(x)
        print(json.dumps(d, indent=4))

main(sys.argv[1])
