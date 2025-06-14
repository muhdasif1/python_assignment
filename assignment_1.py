# Party Estimation Report

# Step 1: Define the counts
faculty_members = 12
administrative_staff_members = 4
institute_students = 100
absent_people = 15

# Step 2: Calculate total people and subtract absentees
total_people = faculty_members + administrative_staff_members + institute_students
present_people = total_people - absent_people

# Step 3: Calculate food requirement in grams
food_per_person_grams = 250
total_food_grams = present_people * food_per_person_grams

# Step 4: Convert grams to kilograms
total_food_kg = total_food_grams / 1000

# Step 5: Display the report
print("<==================** Party Estimation Report **==================>")
print("===> Faculty Members: ", faculty_members)
print("===> Administrative Staff Members: ", administrative_staff_members)
print("===> Students in Institute: ", institute_students)
print("===> Absent People: ", absent_people)
print("===> Total People (Before Absentees): ", total_people)
print("===> Total People (After Absentees): ", present_people)
print("===> Total Food Required: ", total_food_grams, "grams")
print("===> Total Food Required: ", total_food_kg, "kilograms")
print("<=================================================================>")
