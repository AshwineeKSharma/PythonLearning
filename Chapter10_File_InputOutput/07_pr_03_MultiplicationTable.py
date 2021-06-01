# WAP to generate Multiplication Tables from 2 to 20 and write it to the different files.
# place these files in a folder for a 13 year old.

for i in range(2,21):
    with open(f"D:\\Python Learning\\Chapter10_File_InputOutput\\Tables\\Multiplication_Table_Of_{i}.txt","w") as tab:
        for j in range(1,11):
             tab.write(f"{i} X {j} = {i*j} \n")

