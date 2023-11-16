sum = 0
with open("06-exam-rami.py", "r") as my_file:
    lines = my_file.readlines()
    for line in lines:
        if len(line) > 1:
            sum = sum + 1
print("Hello. The number of coded lines is:",sum)
