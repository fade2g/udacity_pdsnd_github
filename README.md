>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.

### Date created
This project was created on December 30, 2023.

### Project Title
Udacity Nanodegree "Programming for Data Science" Bike Share Project 

### Description
This project provides same basic data analysis for bike sharing data of three US cities.

It uses Python 3, with numpy and pandas as analysis frameworks.

### Prerequisites
- Python 3.x installed
- numpy installed, see [Numpy installation](https://numpy.org/install/)
- pandas installed, see [Pandas installation](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html|)

### Usage
1. navigate to the folder with the file `bikeshare.py`
2. Enter `python bikeshare.py`
3. Follow the instructions

### Files used
- bikeshare.py: The python script for reading data and executing 
- data files (not shared on github, provided through udacity):
  - chicago.csv
  - new_york_city.csv
  - washington.csv

### Data Files
In order to manually create correctly structured data files, the following conventions must be used:
- The data files are expected to be in the folder ./data.
- They must be CSVs mit comma separated values
- The following columns must be present (including the first line as header:
  - id (unique ID, no label in the header)
  - `Start Time` (in the format YYYY-mm-DD HH:MM:SS)
  - `End Time` (in the format YYYY-mm-DD HH:MM:SS)
  - `Trip Duration` Duration in seconds
  - `Start Station` Name of the start station (no commas allowed)
  - `End Station` Name of the start station (no commas allowed)
  - `User Type` String indicating the category of the user
  - `Gender` Gender of the user (optional)
  - `Birth year` Birth year of the user (optional)

### Credits
The project is maily based on the instructions an course materials of the aforementioned Udacity Nano Degree [Programming for Data Science with Python](https://www.udacity.com/course/programming-for-data-science-nanodegree--nd104).

Other sources include the [Pandas Documentation](https://pandas.pydata.org/pandas-docs/dev/index.html) and [Numpy Documentation](https://numpy.org/).

Of course, various Stack Overflow resources where used to solve specific issues.  

