# 1. Define student scores (matching sample output)
scores = [85, 72, 91, 64, 78]

# 2. Display all student scores
print("Student Scores:")
for score in scores:
    print(score)
print()

# 3. Analyze each student's score and count pass/fail
passed_count = 0
failed_count = 0

for i, score in enumerate(scores, start=1):
    if score >= 90:
        interpretation = "Excellent - Passed"
        passed_count += 1
    elif score >= 80:
        interpretation = "Very Good - Passed"
        passed_count += 1
    elif score >= 75:
        interpretation = "Good - Passed"
        passed_count += 1
    else:
        interpretation = "Failed"
        failed_count += 1
        
    print(f"Student {i}: {score}\n{interpretation}")

print()

# 4. Perform summary calculations
total_score = sum(scores)
average_score = total_score // len(scores) if total_score % len(scores) == 0 else round(total_score / len(scores), 2)
highest_score = max(scores)
lowest_score = min(scores)

# 5. Display summary results
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")