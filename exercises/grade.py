# check letter grade
grade = 100
# check edge cases. Grade can't be > 100, can't be less than 0

if grade > 100 or grade < 0:
    print("Must be between 0 and 100")
    print("Exiting...")
    exit(0)
elif grade >= 90 and grade <= 100:
            print('A')
elif grade >=80 and grade <= 89:
        print('B')
elif grade >=70 and grade <= 79:
        print('C')
elif grade >=60 and grade <= 69:
        print('D')
else:
    print('F')
