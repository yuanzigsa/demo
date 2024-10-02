import copy
import json

data = [
    {"7:00-12:00": 0.5},
    {"13:00-18:00": 0.3},
    {"19:00-24:00": 0.2}
  ]


speed_limit_list = copy.deepcopy(data)
speed_limit_list[0]["7:00-12:00"] = 1

speed_limit_info = [{json.dumps(info): False} for info in speed_limit_list]

with open('speed_limit.info', 'w') as file:
    json.dump(speed_limit_info, file, indent=4)

with open('speed_limit.info', 'r') as file:
    data = json.load(file)

print(data)

