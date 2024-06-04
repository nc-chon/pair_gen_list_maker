import csv
import re

def raw_stu_converter():
    '''
    Opens the raw student csv data, iterates through each row to remove 
    the line break `\t` and returns a list that Python can use.
    '''
    print('converting raw_student_data.csv...')
    with open('./data/raw_student_data.csv', encoding='utf-8') as c:
        reader = csv.reader(c, delimiter=',')
        raw_stu_data_list = []
        for row in reader:
            raw_stu_data_list.append(row)

        raw_stu_flipped_list = []
        for students_location in raw_stu_data_list:
            students_location[0] = re.sub('\t', '', students_location[0])
            students_location[1] = re.sub('\t', '', students_location[1])
            raw_stu_flipped_list.append([students_location[1], students_location[0]])
    return raw_stu_flipped_list

def sem_stu_converter():
    '''
    Opens the seminar student csv data, iterates through each row to remove 
    the line break `\t` and returns a list that Python can use.
    '''
    print('converting seminar_student_data.csv...')
    with open('./data/seminar_student_data.csv', encoding='utf-8') as c:
        reader = csv.reader(c, delimiter=',')
        sem_stu_data_list = []
        for row in reader:
            sem_stu_data_list.append(row)

        for students in sem_stu_data_list:
            students = re.sub('\t', '', students[0])
    return sem_stu_data_list

def pair_gen_list(raw_stu_list, sem_stu_list):
    '''
    Takes both of the new converted lists and filters the seminar students
    from the raw data, along with their location. Returns a list.
    '''
    filtered_stu_locations_list = []
    for students_location in raw_stu_list:
        for students in sem_stu_list:
            if students[0] in students_location:
                filtered_stu_locations_list.append(students_location)
    return filtered_stu_locations_list

def create_pair_gen_csv(pair_gen_func, raw_data, sem_data):
    '''
    Invokes the pair_gen_list function with the two sets of data and writes 
    a csv file with the correct seminar students and location, ready to be
    copied directly into our NC pair generator.
    '''
    with open('./output/student_pair_data.csv', 'a', encoding='utf-8') as c:
        writer_obj = csv.writer(c)
        print('filtering seminar students...')
        students_data = pair_gen_func(raw_data, sem_data)
        for students in students_data:
            writer_obj.writerow(students)
        print('creating output csv file...')

    print('done! check your output folder')
