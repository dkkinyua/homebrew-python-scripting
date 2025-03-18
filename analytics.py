# This Python script gets the analytics for packages downloaded on Homebrew, and sort them in a JSON file according to popularity.
import json
import time
import requests

url = 'https://formulae.brew.sh/api/formula.json'

response = requests.get(url)
data = response.json()

results = [] # We will save the results in this list

t1 = time.perf_counter() 
total_packages = 0 # Initial counter for total packages analysed from API

# Looping through the packages to collect package name and description
for i in data:
    package_name = i['name']
    package_desc = i['desc']

    package_url = f'https://formulae.brew.sh/api/formula/{package_name}.json'
    r = requests.get(package_url)

    package_data = r.json()
    # print(package_data["analytics"]) # Get the analytics data from the URL
    # Save the analytics into variables for easier access
    install_30d = package_data["analytics"]["install_on_request"]["30d"][package_name]
    install_90d = package_data["analytics"]["install_on_request"]["90d"][package_name]
    install_365d = package_data["analytics"]["install_on_request"]["365d"][package_name]

    analytics_data = {
        'name': package_name,
        'desc': package_desc,
        'analytics': {
            '30d': install_30d,
            '90d': install_90d,
            '365d': install_365d
        }
    }

    results.append(analytics_data)

    time.sleep(response.elapsed.total_seconds()) # pausing the program for the amount of time it took to get the data from the server to avoid overloading it

    total_packages += 1

    print(f'{package_name} analysed in {response.elapsed.total_seconds()}s')


t2 = time.perf_counter()
print(f'{total_packages} packages analysed in {t2 - t1:.2f} s')

# Let's save this information into a JSON file
with open('analytics.json', 'w') as f:
    json.dump(results, f, indent=2)

