# make a range from 45 to 210, using a for loop iterate over the sequence and print the elements. Skip the number 100 and break the loop at 205
for val in range(45,210):
    if val == 100:
        continue
    if val == 205:
        break
    print(val)

resultUser = int(input("what is the product of 7 * 24 ?"))
while not resultUser == 168:
    print("Your Answer is wrong try again..")
    resultUser = int(input("what is the product of 7 * 24 ?"))
else:
    print("You answered this Question correctly")