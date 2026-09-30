import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# STUDENT ACADEMIC PERFORMANCE ANALYSIS
# ============================================================

# Create output folder
output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)

# ------------------------------------------------------------
# 1. CREATE DATASET USING PANDAS
# ------------------------------------------------------------

subjects = [
    "Python",
    "DBMS",
    "Java",
    "Web Development",
    "Data Structures",
    "Mathematics"
]

data = {
    "Subject": subjects,
    "Semester 1": [72, 68, 75, 70, 65, 74],
    "Semester 2": [75, 72, 78, 73, 70, 76],
    "Semester 3": [78, 74, 80, 76, 73, 79],
    "Semester 4": [82, 79, 85, 80, 77, 83],
    "Semester 5": [85, 82, 88, 84, 80, 86],
    "Semester 6": [90, 86, 92, 88, 84, 89]
}

df = pd.DataFrame(data)

print("\n========== STUDENT DATASET ==========")
print(df)

# Save dataset
df.to_csv(os.path.join(output_dir, "student_marks.csv"), index=False)


# ------------------------------------------------------------
# 2. HOW MANY SEMESTERS?
# ------------------------------------------------------------

semester_columns = [
    "Semester 1",
    "Semester 2",
    "Semester 3",
    "Semester 4",
    "Semester 5",
    "Semester 6"
]

number_of_semesters = len(semester_columns)

print("\n2. Number of semesters:", number_of_semesters)


# ------------------------------------------------------------
# 3. HOW MANY SUBJECTS TOTAL?
# ------------------------------------------------------------

number_of_subjects = len(df["Subject"].unique())

print("3. Total subjects studied:", number_of_subjects)


# ------------------------------------------------------------
# 4. HIGHEST MARKS
# ------------------------------------------------------------

highest_marks = df[semester_columns].max().max()

print("4. Highest marks:", highest_marks)


# ------------------------------------------------------------
# 5. LOWEST MARKS
# ------------------------------------------------------------

lowest_marks = df[semester_columns].min().min()

print("5. Lowest marks:", lowest_marks)


# ------------------------------------------------------------
# 6. SEMESTER WITH HIGHEST TOTAL
# ------------------------------------------------------------

semester_totals = df[semester_columns].sum()

highest_total_semester = semester_totals.idxmax()
highest_total_marks = semester_totals.max()

print(
    "6. Semester with highest total:",
    highest_total_semester,
    "=",
    highest_total_marks
)


# ------------------------------------------------------------
# 7. SEMESTER WITH LOWEST TOTAL
# ------------------------------------------------------------

lowest_total_semester = semester_totals.idxmin()
lowest_total_marks = semester_totals.min()

print(
    "7. Semester with lowest total:",
    lowest_total_semester,
    "=",
    lowest_total_marks
)


# ------------------------------------------------------------
# 8. FIRST FIVE RECORDS
# ------------------------------------------------------------

print("\n8. First five records:")
print(df.head())


# ------------------------------------------------------------
# 9. AVERAGE MARKS FOR EACH SEMESTER
# ------------------------------------------------------------

semester_average = df[semester_columns].mean()

print("\n9. Average marks for each semester:")
print(semester_average)


# ------------------------------------------------------------
# 10. LINE GRAPH - SEMESTER-WISE AVERAGE
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    semester_average.index,
    semester_average.values,
    marker="o",
    linewidth=2
)

plt.axhline(
    y=75,
    linestyle="--",
    linewidth=2,
    label="Target = 75%"
)

plt.title("Semester-wise Average Marks")
plt.xlabel("Semester")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.grid(True)
plt.legend()

plt.tight_layout()

plt.savefig(
    os.path.join(output_dir, "Figure_1_Semester_Average.png"),
    dpi=300
)

plt.show()


# ------------------------------------------------------------
# 11. BAR GRAPH - SUBJECT-WISE AVERAGE
# ------------------------------------------------------------

subject_average = df.set_index("Subject")[semester_columns].mean(axis=1)

print("\n11. Subject-wise average:")
print(subject_average)

plt.figure(figsize=(10, 6))

plt.bar(
    subject_average.index,
    subject_average.values
)

plt.axhline(
    y=75,
    linestyle="--",
    linewidth=2,
    label="Target = 75%"
)

plt.title("Subject-wise Average Marks")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.xticks(rotation=30)
plt.legend()

plt.tight_layout()

plt.savefig(
    os.path.join(output_dir, "Figure_2_Subject_Average.png"),
    dpi=300
)

plt.show()


# ------------------------------------------------------------
# 12. HIGHEST-PERFORMING SUBJECT
# ------------------------------------------------------------

highest_subject = subject_average.idxmax()
highest_subject_average = subject_average.max()

print(
    "\n12. Highest-performing subject:",
    highest_subject,
    "=",
    round(highest_subject_average, 2)
)


# ------------------------------------------------------------
# 13. LOWEST-PERFORMING SUBJECT
# ------------------------------------------------------------

lowest_subject = subject_average.idxmin()
lowest_subject_average = subject_average.min()

print(
    "13. Lowest-performing subject:",
    lowest_subject,
    "=",
    round(lowest_subject_average, 2)
)


# ------------------------------------------------------------
# 14. BEST AND WORST SEMESTER
# ------------------------------------------------------------

best_semester = semester_average.idxmax()
worst_semester = semester_average.idxmin()

print("14. Best semester:", best_semester)
print("    Worst semester:", worst_semester)


# ------------------------------------------------------------
# 15. IMPROVEMENT BETWEEN SEMESTER 1 AND SEMESTER 6
# ------------------------------------------------------------

semester_1_average = semester_average["Semester 1"]
semester_6_average = semester_average["Semester 6"]

improvement = semester_6_average - semester_1_average

print(
    "\n15. Improvement from Semester 1 to Semester 6:",
    round(improvement, 2),
    "marks"
)


# ------------------------------------------------------------
# 16. NUMPY STATISTICS
# ------------------------------------------------------------

all_marks = df[semester_columns].values.flatten()

mean_marks = np.mean(all_marks)
median_marks = np.median(all_marks)
maximum_marks = np.max(all_marks)
minimum_marks = np.min(all_marks)
standard_deviation = np.std(all_marks)

print("\n16. NumPy Statistics")
print("Mean:", round(mean_marks, 2))
print("Median:", round(median_marks, 2))
print("Maximum:", maximum_marks)
print("Minimum:", minimum_marks)
print("Standard Deviation:", round(standard_deviation, 2))


# ------------------------------------------------------------
# 17. GRAPH - SUBJECT PERFORMANCE ACROSS SIX SEMESTERS
# ------------------------------------------------------------

plt.figure(figsize=(12, 7))

for subject in df["Subject"]:
    subject_row = df[df["Subject"] == subject][semester_columns].values[0]

    plt.plot(
        semester_columns,
        subject_row,
        marker="o",
        label=subject
    )

plt.axhline(
    y=75,
    linestyle="--",
    linewidth=2,
    label="Target = 75%"
)

plt.title("Subject Performance Across Six Semesters")
plt.xlabel("Semester")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.grid(True)
plt.legend()

plt.tight_layout()

plt.savefig(
    os.path.join(output_dir, "Figure_5_Subject_Performance.png"),
    dpi=300
)

plt.show()


# ------------------------------------------------------------
# 18. TARGET = 75%
# Already shown using axhline() above
# ------------------------------------------------------------

target = 75

print("\n18. Academic Target:", target, "%")


# ------------------------------------------------------------
# 19. CLASS AVERAGE
# ------------------------------------------------------------

# No class data was provided in the assignment.
# These are SAMPLE class averages only for demonstration.
# Replace these values with actual class data if available.

class_average = np.array([68, 71, 73, 76, 79, 82])

print("\n19. Sample Class Average:")
for sem, value in zip(semester_columns, class_average):
    print(sem, "=", value)


# ------------------------------------------------------------
# FIGURE 4 - STUDENT VS CLASS AVERAGE
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    semester_columns,
    semester_average.values,
    marker="o",
    linewidth=2,
    label="My Average"
)

plt.plot(
    semester_columns,
    class_average,
    marker="s",
    linewidth=2,
    label="Class Average"
)

plt.axhline(
    y=75,
    linestyle="--",
    linewidth=2,
    label="Target = 75%"
)

plt.title("My Performance vs Class Average")
plt.xlabel("Semester")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.grid(True)
plt.legend()

plt.tight_layout()

plt.savefig(
    os.path.join(output_dir, "Figure_4_My_vs_Class_Average.png"),
    dpi=300
)

plt.show()


# ------------------------------------------------------------
# 20. 2 x 2 MATPLOTLIB DASHBOARD
# ------------------------------------------------------------

fig, axes = plt.subplots(2, 2, figsize=(16, 11))

# Figure 1 - Semester Average
axes[0, 0].plot(
    semester_average.index,
    semester_average.values,
    marker="o"
)

axes[0, 0].axhline(
    y=75,
    linestyle="--",
    linewidth=2
)

axes[0, 0].set_title("Semester-wise Average")
axes[0, 0].set_ylim(0, 100)
axes[0, 0].grid(True)

# Figure 2 - Subject Average
axes[0, 1].bar(
    subject_average.index,
    subject_average.values
)

axes[0, 1].axhline(
    y=75,
    linestyle="--",
    linewidth=2
)

axes[0, 1].set_title("Subject-wise Average")
axes[0, 1].set_ylim(0, 100)
axes[0, 1].tick_params(axis="x", rotation=30)

# Figure 3 - Semester Total
axes[1, 0].bar(
    semester_totals.index,
    semester_totals.values
)

axes[1, 0].set_title("Semester-wise Total Marks")
axes[1, 0].tick_params(axis="x", rotation=30)

# Figure 4 - My vs Class Average
axes[1, 1].plot(
    semester_columns,
    semester_average.values,
    marker="o",
    label="My Average"
)

axes[1, 1].plot(
    semester_columns,
    class_average,
    marker="s",
    label="Class Average"
)

axes[1, 1].axhline(
    y=75,
    linestyle="--",
    linewidth=2,
    label="Target = 75%"
)

axes[1, 1].set_title("My Performance vs Class Average")
axes[1, 1].set_ylim(0, 100)
axes[1, 1].tick_params(axis="x", rotation=30)
axes[1, 1].legend()

fig.suptitle(
    "Student Academic Performance Dashboard",
    fontsize=18,
    fontweight="bold"
)

plt.tight_layout()

plt.savefig(
    os.path.join(output_dir, "Figure_6_2x2_Dashboard.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ------------------------------------------------------------
# 21. FIVE OBSERVATIONS
# ------------------------------------------------------------

print("\n========== 21. FIVE OBSERVATIONS ==========")

print(
    "1. Academic performance improved consistently from Semester 1 to Semester 6."
)

print(
    "2. Semester 6 is the best-performing semester based on average marks."
)

print(
    "3. Java is the highest-performing subject with an average of "
    f"{highest_subject_average:.2f} marks."
)

print(
    "4. Data Structures is the lowest-performing subject and needs more attention."
)

print(
    "5. The Semester 6 average is above the 75% academic target."
)


# ------------------------------------------------------------
# FINAL SUMMARY
# ------------------------------------------------------------

print("\n========== FINAL SUMMARY ==========")

print("Total Semesters:", number_of_semesters)
print("Total Subjects:", number_of_subjects)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Best Semester:", best_semester)
print("Worst Semester:", worst_semester)
print("Highest Subject:", highest_subject)
print("Lowest Subject:", lowest_subject)
print("Improvement S1 to S6:", round(improvement, 2))
print("Mean:", round(mean_marks, 2))
print("Median:", round(median_marks, 2))
print("Maximum:", maximum_marks)
print("Minimum:", minimum_marks)
print("Standard Deviation:", round(standard_deviation, 2))

print("\nAll files saved inside:", output_dir)