import csv

def write_into_csv(info_list)
    with open('stu_info_csv', 'a', newline='') as csv_file
        writer = csv.writer(csv_file)
        
        if csv_file.tell() ==0;
            writer.writerow(["Name","Age","Contact Number","Email ID"])
        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True
    student-num = 1
    while(condition):
        student_info = input("Enter some student information in the format of (name age contact_no email-id: ")
        
        #split
        student_info_list = stu_info.split(' ')
        print("\nthe entered information is -\nName: {}\nAge: {}\nContact NO: {}\nEmail ID: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        
        choice_check = input("Is the entered info correct (yes/no): ")
        if choice_check == "yes":
            write_into_csv(student_info_list)
        
        condition_check = input("Enter yes or no to continue: ")
        if condition_check == "yes":
            condition = True
            student_num = student_num+1
        elif condition_check == "no":
            condition = False
        elif choice_check =="no":
            print("\n Please re enter the values:")
           
