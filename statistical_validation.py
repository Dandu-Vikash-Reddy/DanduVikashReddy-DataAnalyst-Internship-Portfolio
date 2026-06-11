"""
ApexPlanet Data Analytics Internship
Task 4: Data Storytelling & Statistical Validation
File Name: statistical_validation.py
"""

import numpy as np
import scipy.stats as stats

def run_hypothesis_test():
    print("=" * 70)
    print("         TASK 4: HYPOTHESIS TESTING & STATISTICAL VALIDATION     ")
    print("=" * 70)

    # 1. Business Hypothesis Setup
    # Null Hypothesis (H0): The website layout change has no effect on conversion rates.
    # Alternative Hypothesis (H1): The website layout change significantly changes conversion rates.
    print("\n[1] HYPOTHESIS FORMULATION:")
    print("    H0: Conversion Rate (Legacy Layout) == Conversion Rate (New Layout)")
    print("    H1: Conversion Rate (Legacy Layout) != Conversion Rate (New Layout)")

    # 2. Mock A/B Test Contingency Matrix [Converted, Not Converted]
    # Control Group (Old UI): 1,000 visitors, 120 conversions (12% conversion rate)
    # Treatment Group (New UI): 1,000 visitors, 165 conversions (16.5% conversion rate)
    control_metrics = [120, 880]     
    treatment_metrics = [165, 835]   
    
    contingency_matrix = [control_metrics, treatment_metrics]

    print("\n[2] EXPERIMENT METRICS:")
    print(f"    Control Group (Legacy UI)  : Converted = {control_metrics[0]}, Left = {control_metrics[1]}")
    print(f"    Treatment Group (New UI)   : Converted = {treatment_metrics[0]}, Left = {treatment_metrics[1]}")

    # 3. Chi-Squared Contingency Test Execution
    chi2_stat, p_value, dof, expected_values = stats.chi2_contingency(contingency_matrix)

    print("\n[3] STATISTICAL ANALYSIS RESULTS:")
    print(f"    Chi-Square Statistic : {chi2_stat:.4f}")
    print(f"    Degrees of Freedom   : {dof}")
    print(f"    Calculated P-Value   : {p_value:.5f}")

    # 4. Significance Evaluation & Operational Verdict
    alpha = 0.05
    print("\n[4] BUSINESS INTERPRETATION & ACTIONABLE VERDICT:")
    print(f"    Significance Threshold (Alpha): {alpha}")

    if p_value < alpha:
        print(f"    Verdict: REJECT THE NULL HYPOTHESIS (p-value < {alpha})")
        print("    Conclusion: The conversion improvement in the treatment group is mathematically significant.")
        print("    Next Step: Deploy the optimized interface layout globally to all production servers.")
    else:
        print(f"    Verdict: FAIL TO REJECT THE NULL HYPOTHESIS (p-value >= {alpha})")
        print("    Conclusion: The difference observed could likely be a result of random sample variation.")
        print("    Next Step: Keep the baseline interface design; re-evaluate layout hypotheses.")

    print("\n" + "=" * 70)

if __name__ == "__main__":
    run_hypothesis_test()