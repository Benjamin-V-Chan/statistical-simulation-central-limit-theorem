import pandas as pd
import scipy.stats as stats

def perform_tests():
    sample_means = pd.read_csv("outputs/sample_means.csv")["Sample Mean"].values
    results = []

    shapiro_test = stats.shapiro(sample_means)
    results.append(f"Shapiro-Wilk test: W={shapiro_test.statistic}, p={shapiro_test.pvalue}")

    ks_test = stats.kstest(sample_means, "norm", args=(sample_means.mean(), sample_means.std()))
    results.append(f"Kolmogorov-Smirnov test: D={ks_test.statistic}, p={ks_test.pvalue}")

    anderson_test = stats.anderson(sample_means, dist="norm")
    results.append(f"Anderson-Darling test: A2={anderson_test.statistic}, critical={anderson_test.critical_values}")

    with open("outputs/normality_tests.txt", "w") as f:
        f.write("\n".join(results))

if __name__ == "__main__":
    perform_tests()
