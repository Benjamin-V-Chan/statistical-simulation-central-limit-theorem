import os
from scripts import (
    generate_population,
    sample_means,
    analyze_distribution,
    statistical_tests
)

if not os.path.exists("outputs"):
    os.makedirs("outputs")

def run_simulation():
    generate_population.generate_population()
    sample_means.compute_sample_means()
    analyze_distribution.visualize_distribution()
    statistical_tests.perform_tests()
    print("Simulation complete. Check outputs/ for results.")

if __name__ == "__main__":
    run_simulation()
