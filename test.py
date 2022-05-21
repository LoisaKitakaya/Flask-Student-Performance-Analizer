import requests

BASE = 'http://127.0.0.1:5000'

def get_all_students():

    response = requests.get(BASE + '/all_students')

    print(response.json())
    print('')
    print(response.url)

def get_student():

    response = requests.get(BASE + '/student/3')

    print(response.json())
    print('')
    print(response.url)

def get_student_grades():

    response = requests.get(BASE + '/student/grades/3')

    print(response.json())
    print('')
    print(response.url)

if __name__ == '__main__':

    get_student()

    print('')
    print('-----------------------------------')
    print('')

    get_student_grades()

    print('')
    print('-----------------------------------')
    print('')

    get_all_students()