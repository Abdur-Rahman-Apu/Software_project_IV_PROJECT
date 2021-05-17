import json
import os
import time

# show options which can be performed by this project
def option():
    time.sleep(2)

    select = int(input("Choose option:"))
    return select


# add students

def course():
    cs = input('Enter course and section(cse234(A)) separated by comma(,):\n').split(',')
    return cs


#Add student
def add():
    print("\n***********Add new registration data*********************\n")
    id = input("Student ID:")
    record['ID'] =id
    name = input("Student name:")
    record['name'] = name
    reg = course()
    record['Courses'] = reg
    status = input("Registration status:")
    record['status'] = status
    try:

        f = os.path.getsize("registration.json")
    except FileNotFoundError:
        file=open('registration.json','w')
        f = os.path.getsize("registration.json")
    if f == 0:
        s.append(record)

        # python to json
        file=open('registration.json','w')
        json_data = json.dumps(s, indent=4)
        file.write(json_data)
        file.close()
    else:
        read_file=open('registration.json','r')
        json_new = read_file.read()
        new = json.loads(json_new)

        new.append(record)

        write_file=open('registration.json','w')
        data=json.dumps(new,indent=4)
        write_file.write(data)
        write_file.close()




# Start main task
print("Welcome.Which option do you want to select?\n1.Add new registration data\n2.Search student using ID\n3.Update registration status.\n4.Delete registration record\n5.Exit\n")
while True:

    s = []
    record = {}

    got = option()

    if got == 1:
        add()
        print("\nAdd Successfully.\n")

    if got == 2:
        try:
            file = open('registration.json', 'r')
            print("\n*************************Search student's information****************************\n")
            find = input("Student ID:")


            json_data = file.read()
            obj = json.loads(json_data)
            flag = 0
            for i in range(len(obj)):
                d = obj[i]
                if d.get('ID') == find:
                    print(f"Student ID={str(d['ID'])}")
                    print(f"Student name ={str(d['name'])}")
                    print("Courses:")
                    c = d['Courses']
                    for i in range(len(c)):
                        print(c[i])
                    print(f"Status={str(d['status'])}")
                    print("\n\n")
                    flag = 1
            if flag == 0:
                print("This Student's record is not available.\n\n\n")

        except FileNotFoundError:
            print("\nFile not found.\n")

    if got == 3:
        try:
            file = open('registration.json', 'r')
            print("\n*************************UPDATE REGISTRATION STATUS****************************\n")
            find = input("Student ID:")


            json_data = file.read()
            obj = json.loads(json_data)
            flag = 0
            for i in range(len(obj)):
                d = obj[i]

                if d.get('ID') == find:
                    reg_status = input("Registration Status:")
                    d['status'] = reg_status
                    flag = 1
            if flag == 0:
                print("This Student's record is not available.\n")
            else:
                file = open('registration.json', 'w')
                json_data = json.dumps(obj, indent=4)
                file.write(json_data)
                file.close()
                print("Update registration status successfully.\n")

        except FileNotFoundError:
            print("File not found.\n")

    if got == 4:
        try:
            file = open('registration.json', 'r')
            print("\n*************************DELETE REGISTRATION RECORD****************************\n")
            find = input("Student ID:")
            json_data = file.read()
            obj = json.loads(json_data)

            flag = 0
            for i , value in enumerate(obj):
                if value['ID'] == find:
                    del obj[i]
                    flag = 1


            if flag == 0:
                print("This Student's record is not available.\n")
            else:
                file = open('registration.json', 'w')
                json_data = json.dumps(obj, indent=4)
                file.write(json_data)
                file.close()
                print("Delete successfully.\n")

        except FileNotFoundError:
            print("File not found.\n")

    if got == 5:
        print("Thank you. Come back again.")
        quit()



