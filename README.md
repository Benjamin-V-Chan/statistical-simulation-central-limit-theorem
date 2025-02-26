# statistical-simulation-central-limit-theorem

## Folder Structure

```
project-root/
├── scripts/
│   ├── 01_generate_population.py   # Generate synthetic population datasets
│   ├── 02_sample_means.py          # Compute sample means from population
│   ├── 03_analyze_distribution.py  # Visualize the sample mean distribution
│   ├── 04_statistical_tests.py     # Perform normality tests
│   ├── 05_run_simulation.py        # Execute the full pipeline
├── outputs/                        # Stores generated population, samples, and results
│   ├── population.csv
│   ├── sample_means.csv
│   ├── analysis.png
│   ├── normality_tests.txt
├── config.py                        # Stores simulation parameters
├── requirements.txt                 # Required Python packages
├── README.md                        # Project documentation
```

## Usage

### 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file.
```sh
pip install -r requirements.txt
```

### 2. Generate the Population Dataset:
Run the script to generate a synthetic population based on a chosen probability distribution.
```sh
python scripts/01_generate_population.py
```

### 3. Compute Sample Means:
Extract multiple samples from the population and compute their means.
```sh
python scripts/02_sample_means.py
```

### 4. Analyze and Visualize Distribution:
Generate a histogram of the sample means to observe convergence to normality.
```sh
python scripts/03_analyze_distribution.py
```

### 5. Perform Normality Tests:
Run statistical tests to check for normality in the sample mean distribution.
```sh
python scripts/04_statistical_tests.py
```

### 6. Run Full Simulation:
Execute the entire pipeline sequentially.
```sh
python scripts/05_run_simulation.py
```

## Requirements

Ensure you have the following dependencies installed:

```
numpy
pandas
matplotlib
scipy
```

All dependencies can be installed using:
```sh
pip install -r requirements.txt
```

This project provides an in-depth simulation of the Central Limit Theorem by illustrating how sample means converge to a normal distribution through statistical visualization and hypothesis testing.