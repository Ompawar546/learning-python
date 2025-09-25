def stdDetail():
    name = input("enter name ")
    rollno = int(input("enter roll no "))
    return name,rollno

def sub():
    sub1,sub2,sub3 = eval(input("Enter Subjects (comma seperated): "))
    return sub1,sub2,sub3

def Exams():
    msub1, msub2, msub3 = eval(input("enter marks : "))
    return msub1,msub2,msub3

def results(mrks1,mrks2,mrks3):
    if mrks1 and mrks2 and mrks3 < 20:
        return False
    else:
        return True
    
def report():
    stdDetail()
    sub()
    submarks1,submarks2,submarks3 = Exams()
    print(f'{submarks1},{submarks2},{submarks3}')
    stdres =  results(submarks1,submarks2,submarks3)
    if stdres == False:
        return "Fail"
    else:
        return "Pass"

Statuts = report()
print(Statuts)
