import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

def visualize_distribution():
    sample_means = pd.read_csv("outputs/sample_means.csv")["Sample Mean"].values

    plt.figure(figsize=(8, 6))
    plt.hist(sample_means, bins=30, density=True, alpha=0.6, label="Sample Means")

    mu, sigma = np.mean(sample_means), np.std(sample_means)
    x = np.linspace(min(sample_means), max(sample_means), 100)
    plt.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', label="Normal Curve")

    plt.xlabel("Sample Mean")
    plt.ylabel("Density")
    plt.title("Distribution of Sample Means")
    plt.legend()
    plt.savefig("outputs/analysis.png")
    plt.show()

if __name__ == "__main__":
    visualize_distribution()
