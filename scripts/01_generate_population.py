import numpy as np
import pandas as pd
import config

np.random.seed(42)

def generate_population():
    if config.DISTRIBUTION == "uniform":
        population = np.random.uniform(config.PARAM_LOW, config.PARAM_HIGH, config.POPULATION_SIZE)
    elif config.DISTRIBUTION == "exponential":
        population = np.random.exponential(config.PARAM_SCALE, config.POPULATION_SIZE)
    elif config.DISTRIBUTION == "poisson":
        population = np.random.poisson(config.PARAM_LAMBDA, config.POPULATION_SIZE)
    else:
        raise ValueError("Unsupported distribution type")

    df = pd.DataFrame(population, columns=["Value"])
    df.to_csv("outputs/population.csv", index=False)

if __name__ == "__main__":
    generate_population()
