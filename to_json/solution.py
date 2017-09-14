import json
import functools

def to_json(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        # print(json.dumps(result))
        return json.dumps(result)
    return inner
