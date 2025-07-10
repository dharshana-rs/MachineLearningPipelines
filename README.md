# MachineLearningPipelines

# CSV & ASCII Data Cleaning Pipeline

This project demonstrates how to convert exploratory notebook code into a reusable, script-based Python pipeline using modular design.
It loads data from both a standard CSV file and a fixed-width ASCII file, applies cleaning functions, and prints cleaned outputs.


project_root/
- main.py              # Entry point for running the pipeline
- loaders.py           # Functions to load CSV and ASCII files
- cleaners.py          # Reusable data cleaning functions
- requirements.txt     # Python package dependencies
- README.md            # Project overview and usage instructions
- data/
	- data.csv         	# Sample CSV input
	- data_ascii.txt   	# Sample ASCII (fixed-width) input


## How to Run

### Install dependencies
Run this in your terminal or inside PyCharm terminal:

```bash
pip install -r requirements.txt


python main.py --csv path/to/data.csv --ascii path/to/data_ascii.txt


Dependencies
	•	Python 3.x
	•	pandas
