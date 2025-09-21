import json

file = open("2015/12/input.json", "r")
input = file.readlines()[0]
file.close()

data = json.loads(input)

nums_list = []

def extract_data(data):
    if isinstance(data, dict):
        if "red" not in data.values():
            for item in data:
                extract_data(data[item])
    elif isinstance(data, str):
        pass # don't care about strings
    elif isinstance(data, list):
        for item in data:
            extract_data(item)
    elif isinstance(data, int):
        nums_list.append(data)

extract_data(data)

# we have to do this weirdness because the function won't
# add to a global sum variable directly for some reason
sum = 0
for i in nums_list:
    sum += i
print(sum)