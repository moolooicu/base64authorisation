import base64

usernamefile = input("Enter name of username file: ")
passwordfile = input("Enter name of password file: ")
outfile = input("Enter name of output file: ")

user_array = []
userfile = open(usernamefile, 'r')
for line in userfile:
    user_array.append(line.rstrip("\n"))

pass_array = []
passfile = open(passwordfile, 'r')
for line in passfile:
    pass_array.append(line.rstrip("\n"))

outputfile = open(outfile, "w+")
for x in user_array:
    for y in pass_array:
        raw_complete = (x + ":" + y)
        raw_complete_bytes = raw_complete.encode('ascii')
        base64_bytes = base64.b64encode(raw_complete_bytes)
        base64_message = base64_bytes.decode('ascii')
        outputfile.write(base64_message + "\n")
userfile.close()
passfile.close()
outputfile.close()


