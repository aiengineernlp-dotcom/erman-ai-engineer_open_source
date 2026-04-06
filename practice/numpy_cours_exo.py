# 1. convert all into numpy arrays

# 2. convert all arrays into column format

# 3. cobine all feature into a datset

# 4. increase all salaries by 10%

# 5. Normalize salary (divide my max salary)

# 6. Extract all ages, first employee record

# 7. calculate mean salary, median experience and std dev of age

# 8. iterate through dataset and print each row


import numpy as np

age = [25, 30, 35, 40]

salary = [3000, 50000, 60000, 70000]

experience = [2, 5, 7, 10]


# # 1. convert all into numpy arrays // on passe en 1D
# def convert_to_numpy_array(lst: list) -> np.ndarray:
#     return np.array(lst)


# age = convert_to_numpy_array(age)
# salary = convert_to_numpy_array(salary)
# experience = convert_to_numpy_array(experience)


# # print(age)
# # print(age.shape)
# # print("="  *140 )
# # print(salary)
# # print("=" *140)
# # print(experience)
# # print("="  *140 )
# # print("="  *140 )


# # 2. convert all arrays into column format // en passe en 2D
# def convert_to_column_format(lst: tuple) -> np.ndarray:
#     return np.array(lst).reshape(-1, 1)


# age = convert_to_column_format(age)
# salary = convert_to_column_format(salary)
# experience = convert_to_column_format(experience)
# # print(age)
# # print(age.shape)
# # print("="  *140 )
# # print(salary)
# # print("=" *140)
# # print(experience)
# # print("="  *140 )
# # print("="  *140 )


# # 3. cobine all feature into a datset
# dataset = (age, salary, experience)


# def combine_to_dataset(dataset: tuple[list]) -> tuple:
#     return np.hstack(dataset)


# result = combine_to_dataset(dataset)


# # print(result)

# # 4. increase all salaries by 10% sans numpy

# def increase_salary_sans_numpy(sal: list) -> list[float]:
#     new_sal = []
#     for sal in salary:
#         sal_update = sal +  sal * (10/100)
#         new_sal.append(sal_update)
#     return new_sal


# increase_salary_10_percent = increase_salary_sans_numpy(salary)
# print(increase_salary_10_percent)
# print("=" * 140)

# 4. increase all salaries by 10% Avec numpy

def increase_salary_avec_numpy(lst: list) -> np.ndarray:
    sal = np.array(salary).reshape(-1, 1)
    return sal + (
                sal * 10 / 100)  # le probleme est que cetait la multiplication d'une liste avec 10/100 par contre il fallait utiliser le numpy directement  et c'est cette facon que il loop pour moi en ajouttant a chaque valeur 10%


increase_salary_10_percent = increase_salary_avec_numpy(salary)
# print(increase_salary_10_percent)
# print("=" * 140)

a = [1, 3, 4]
b = [2, 5, 6]
c = [a, b]
c = (a, b)
test_numpy = np.array(c) + 1


# print((test_numpy))
# print((test_numpy.shape))
# print(type(c))

# 5. Normalize salary (divide my max salary)

def normalise_salary(sal: list) -> np.ndarray:
    norm = np.array(sal).reshape(-1, 1)  # juste pour mettre en 2D et aussi bonne lecture en colonnne

    return norm / (np.max((sal)))


normalize_salary = normalise_salary(salary)


# print(normalize_salary)


# 6. Extract all ages, first employee record

def extraction(dataset):
    data_stack = np.hstack((dataset))
    data_all_age = data_stack[:, 0]
    first_employee_record = data_stack[0, :]
    return data_stack, data_all_age, first_employee_record


# data_stack, data_all_age,first_employee_record = extraction(dataset)
# print(data_stack)
# # print("\n")
# print(data_all_age) # dataset[:,0]
# print("\n")
# print(first_employee_record) # dataset[0,:]


# 7. calculate mean salary, median experience and std dev of age

def calculate_mean_median_std(salary: list, experience: list, age: list) -> np.ndarray:
    salary = np.array(salary).reshape(-1, 1)
    experience = np.array(experience).reshape(-1, 1)
    age = np.array(age).reshape(-1, 1)

    salary = np.mean(salary)
    experience = np.median(experience)
    age = np.std(age)

    return salary, experience, age


# salary,experience,age = calculate_mean_median_std(salary,experience,age)
# print(salary)
# print(experience)
# print(round(age,4))


# 8. iterate through dataset and print each row

def iterate_through(dataset: list[list]):
    dataset_init = np.array(dataset)
    for r in dataset_init:
        row = r
    return row


it = iterate_through([[salary, experience, age]])

print(it)
