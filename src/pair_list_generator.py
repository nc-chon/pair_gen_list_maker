from src.utils import raw_stu_converter, sem_stu_converter, pair_gen_list, create_pair_gen_csv


def pair_list_generator():
    raw_data_list = raw_stu_converter()
    sem_data_list = sem_stu_converter()
    create_pair_gen_csv(pair_gen_list, raw_data_list, sem_data_list)

pair_list_generator()