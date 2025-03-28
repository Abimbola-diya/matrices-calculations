file="C:/Users/LENOVO L460/Documents/10m.txt"
with open(file) as file_object:
    digits=file_object.read()
pi_ten_million=digits.replace('/n','').replace(' ','')
DOB=input('input your date of birth in dd/mm/yyyy')
dob=DOB.replace('/',"")
if dob in pi_ten_million:
    print("\t-----congratulations-------")
    print("\nyour date of birth : ({}) is in the first ten million digits of pi".format(DOB))
else:
    print('date of birth ({}) is not in the first ten million digits of pi'.format(DOB))

