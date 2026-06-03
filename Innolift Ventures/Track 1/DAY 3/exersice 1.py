import numpy as np

# Create a NumPy array of 10 student marks
marks = np.array([78, 45, 92, 67, 34, 88, 55, 49, 73, 61])

# Calculate statistics
mean_marks = np.mean(marks)
highest_mark = np.max(marks)
lowest_mark = np.min(marks)
std_deviation = np.std(marks)

# Count students who passed (marks >= 50)
passed_count = np.sum(marks >= 50)

# Print summary report
print("===== Student Marks Summary Report =====")
print("Marks:", marks)
print("Mean Marks:", round(mean_marks, 2))
print("Highest Mark:", highest_mark)
print("Lowest Mark:", lowest_mark)
print("Standard Deviation:", round(std_deviation, 2))
print("Number of Students Passed (>=50):", passed_count)
