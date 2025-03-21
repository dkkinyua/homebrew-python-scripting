# Homebrew Python Scripting

This repository contains two Python scripts, `analytics.py` and `sort.py`, that analyze the most downloaded packages on Homebrew. This README will guide you through the steps taken to create these scripts, explaining their functionality and how to use them.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Script Overview](#script-overview)
  - [analytics.py](#analyticspy)
  - [sort.py](#sortpy)
- [Usage](#usage)
- [Conclusion](#conclusion)

## Introduction

The goal of this project is to provide insights into the most popular packages on Homebrew by analyzing download statistics. The scripts are designed to be simple yet effective, allowing users to easily understand and modify them as needed. The major difference between the analytics offered in this JSON files and the analytics offered by Homebrew in the API is that their API for all packages doesn't contain analytics for each package, plus what each package is all about.

Check out their official API: https://formulae.brew.sh/api/formula.json

## Prerequisites

Before running the scripts, ensure you have the following installed:

- Python 3.x
- Required Python packages (listed in `requirements.txt`)

You can install the required packages using:

```bash

pip install -r requirements.txt

```

## Script Overview

### analytics.py

The `analytics.py` script is responsible for fetching and analyzing download data from Homebrew. Here are the steps taken to create this script:

1. **Data Collection**: The script uses the Homebrew API to fetch download statistics for various packages.
2. **Data Processing**: It processes the fetched data to extract relevant information, such as package names and their download counts.
3. **Data Analysis**: The script performs analysis to identify trends and insights, such as the most downloaded packages over a specific period, that is 30 days, 90 days, and 365 days.
4. **Output**: Finally, it outputs the analysis results into a JSON file, analytics.json.

### sort.py

The `sort.py` script is designed to sort the data generated by `analytics.py` from the most to least popular downloads by request/download. Here's how it was developed:

1. **Input Handling**: The script takes the output file `data` from `analytics.py` as input.
2. **Sorting Logic**: It implements the ```sort()``` function from Python to sort the data in reverse order, that is, in descending order.

```python

def sort_data(package):
    return package["analytics"]["365d"]

with open('analytics.json', 'r') as f:
    data = json.load(f)

sorted_data = []

data.sort(key=sort_data, reverse=True)

```
3. **Output Generation**: The sorted data is then saved to a new file, making it easy for users to view the most popular packages.

```python

with open('sorted_analytics.json', 'w') as f:
    json.dump(sorted_data, f, indent=2)

```

## Usage

To run the scripts, follow these steps:

1. Clone the repository:

```bash

git clone https://github.com/dkkinyua/homebrew-python-scripting.git
cd homebrew-python-scripting

```

2. Run `analytics.py` to fetch and analyze the download data:

```bash

python analytics.py

```

*NOTE: When running the `analytics.py` script in the terminal, it'll take time to completely analyse the packages. There are 7500 packages at the time of writing this README and that took me 5400s, 1hr 30 minutes. The reason being, in the for loop, we are getting all the package names and this might cause a huge load on the Homebrew server. To be courteous (always remember to be, hehe) I put a sleep timer equal to the server's response time as shown in the code snippet below o avoid overloading the Homebrew server.* 

```python

for i in data:

    # code
    time.sleep(response.elapsed.total_seconds())

```

3. After running `analytics.py`, execute `sort.py` to sort the results:

```bash

python sort.py

```

4. Check the output files for the analysis and sorted data. You can use different file names if you want to!


## Conclusion

This repository serves as a practical example of using Python for data analysis and sorting. Feel free to modify the scripts to suit your needs or to enhance their functionality. If you have any questions or suggestions, please open an issue or submit a pull request.

I will add this on my blog https://dev.to/dkkinyua soon. Be on the lookout!

Happy coding!
