# Writing and appending data to a file
with open("log.txt", "w") as f:
    f.write("First entry.\n")

with open("log.txt", "a") as f:
    f.write("Second entry appended.")