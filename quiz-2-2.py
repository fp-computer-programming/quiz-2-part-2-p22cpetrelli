#author CJP 11/17/2021

sent = input("Enter a positive or negative sentence. ")

firstsent = sent
firstsent.lower()

if "not" not in firstsent:
    print("You're not " + sent + ". Now SCRAM!")
elif "not" in firstsent:
    if "not" == firstsent:
        print("Anything that does not include not.")
    else:
        print(sent)

