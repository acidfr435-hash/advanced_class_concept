import pandas as pd
import numpy as np
data = np.random.randint(10, size=10)
series = pd.Series(data)

print("original series: ", series)


print(f"\nFirst item: {series[0]}")
print(f"Fifth item: {series[4]}")


filtered = series[series > 5]
print("\n--- Numbers > 5 ---")
print(filtered)

# 4. Statistical Operations
print("\n--- Statistics ---")
print(f"Mean (Average): {series.mean()}")
print(f"Median:         {series.median()}")
print(f"Minimum:        {series.min()}")
print(f"Maximum:        {series.max()}")
