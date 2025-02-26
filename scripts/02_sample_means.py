import numpy as np
import pandas as pd
import config

np.random.seed(42)

def compute_sample_means():
    population = pd.read_csv("outputs/population.csv")["Value"].values
    sample_means = [np.mean(np.random.choice(population, config.SAMPLE_SIZE, replace=True))
                    for _ in range(config.NUM_SAMPLES)]

    df = pd.DataFrame(sample_means, columns=["Sample Mean"])
    df.to_csv("outputs/sample_means.csv", index=False)

if __name__ == "__main__":
    compute_sample_means()
