from collections.abc import Iterable
from pprint import pprint

def deep_find_dfs(data, key, depth=0):
    for k, v in data.items():
        pprint((f'key: {k}', f'value: {v}', f'depth: {depth}'))
        if k == key:
            return v
        if isinstance(v, dict):
            try:
                depth += 1
                return deep_find_dfs(v, key, depth)
            except:
                depth -= 1
        elif isinstance(v, Iterable) and not isinstance(v, str):
            for d in v:
                try:
                    return deep_find_dfs(d, key, depth)
                except:
                    continue
    raise Exception('No such key')

def deep_find_bfs(data, key):
    list_data = list(data.items())
    while list_data:
        data_key, data_value = list_data.pop()
        if data_key == key:
            return data_value
        if isinstance(data_value, dict):
            for value in tuple(data_value.items()):
                list_data.insert(0, value)
        elif isinstance(data_value, Iterable) and not isinstance(data_value, str):
            for value in data_value:
                for elem in tuple(value.items()):
                    list_data.insert(0, elem)
    raise Exception('No such key')

def deep_find_all_dfs(data, key):
    for k, v in data.items():
        if key == k:
            yield v
        if isinstance(v, dict):
            yield from deep_find_all_dfs(v, key) #equivalent solution: for result in deep_find_all(v, key): yield result
        elif isinstance(v, Iterable) and not isinstance(v, str):
            for d in v:
                yield from deep_find_all_dfs(d, key)

def deep_find_all_bfs(data, key):
    list_data = list(data.items())
    result = list()
    while list_data:
        data_key, data_value = list_data.pop()  #if it was pop(0) it would be dfs
        if data_key == key:
            result.insert(0, data_value)        #if it was append() it would be dfs
        if isinstance(data_value, dict):
            for value in tuple(data_value.items()):
                list_data.insert(0, value)
        elif isinstance(data_value, Iterable) and not isinstance(data_value, str):
            for value in data_value:
                for elem in tuple(value.items()):
                    list_data.insert(0, elem)
    return result[::-1]                         #if it was append and pop(0) it would still be bfs

if __name__ == '__main__':
    example = {'d':'v', 
                "global": {"peers": {"15.1.1.1": {"remote_id": "15.1.1.1",
                                                "address_family": {"ipv4": {"sent_prefixes": 1,
                                                                            "received_prefixes": 4,
                                                                            "accepted_prefixes": 4}},
                                                "remote_as": 65002,
                                                "uptime": 13002, 
                                                "is_enabled": True, 
                                                "is_up": True, 
                                                "description": "== R3 BGP Neighbor ==", 
                                                "local_as": 65002}}, 
                            "router_id": "15.1.1.2"},
                'a': 'n',
                "uptime": [{'uptime': 'aa'}, {'a': 'b'
                }]}
    print(deep_find_dfs(example, "uptime"))
    print(deep_find_bfs(example, "uptime"))
    print(list(deep_find_all_dfs(example, 'uptime')))
    print(deep_find_all_bfs(example, 'uptime'))