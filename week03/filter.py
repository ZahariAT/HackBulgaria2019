import csv

'''
def my_filter(file_name,**kwargs):
    filtered_users=[]
    with open(file_name, 'r') as f_input:
        csv_input=csv.DictReader(f_input)

        for row in csv_input:
            current_user=[]
            has_all_args=True
            full_name = row['full_name'].split(' ')
            favourite_color = row['favourite_color']
            company_name = row['company_name']
            email = row['email']
            phone_number = row['phone_number']
            salary = row['salary']
            current_user.extend([full_name,favourite_color,company_name,email,phone_number,salary])

            for key in kwargs:
                if not any(kwargs[key] in filed for filed in current_user):
                    has_all_args=False
                    break
            if has_all_args:
                filtered_users.append(current_user)
    return filtered_users

#my_filter('data.csv','Walter Wang','red')
'''

def my_filter(file_name,**kwargs):
    lst = list()
    with open(file_name, 'r') as f_input:
        csv_input=csv.DictReader(f_input)
        for line in csv_input:
            if all(v == line[k] for k, v in kwargs.items()):
                lst.append(line)
    return lst


def main():
    print(my_filter("example.csv"))

if __name__ == '__main__':
    main()