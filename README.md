# statistical-simulation-central-limit-theorem

## Project Overview

The Central Limit Theorem (CLT) states that the distribution of the sample mean of a sufficiently large number of independent and identically distributed (i.i.d.) random variables approaches a normal distribution, regardless of the original population distribution.

Mathematically, let $\( X_1, X_2, ..., X_n \)$ be a random sample of size $\( n \)$ drawn from a population with mean $\( \mu \)$ and variance $\( \sigma^2 \)$. The sample mean is defined as:

$$\bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_i$$

According to the CLT, as \( n \to \infty \), the standardized sample mean follows a standard normal distribution:

$$Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim N(0,1)$$

### Proof Outline

#### Expectation and Variance of the Sample Mean
Using the properties of expectation and variance:

$$E[\bar{X}] = E\left[\frac{1}{n} \sum_{i=1}^{n} X_i \right] = \frac{1}{n} \sum_{i=1}^{n} E[X_i] = \mu$$

$$Var(\bar{X}) = Var\left( \frac{1}{n} \sum_{i=1}^{n} X_i \right) = \frac{1}{n^2} \sum_{i=1}^{n} Var(X_i) = \frac{\sigma^2}{n}$$

#### Convergence to Normal Distribution
By the Lyapunov or Lindeberg condition, the sum of i.i.d. random variables properly standardized converges in distribution to the standard normal distribution:

$$\frac{\sum_{i=1}^{n} (X_i - \mu)}{\sigma \sqrt{n}} \to N(0,1) \text{ as } n \to \infty$$

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