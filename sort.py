import json

# Let's sort the data from the most popular download to least popular

def sort_data(package):
    return package["analytics"]["365d"]

with open('analytics.json', 'r') as f:
    data = json.load(f)

sorted_data = []

data.sort(key=sort_data, reverse=True)
sorted_data.append(data)
# print(sorted_data)

# Let's open another JSON file with the sorted data
with open('sorted_analytics.json', 'w') as f:
    json.dump(sorted_data, f, indent=2)

print("Sorted data added to new file!")
