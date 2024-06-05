# 1. Прочесть с помощью pandas файл
# california_housing_test.csv, который находится в папке
# sample_data
# 2. Посмотреть сколько в нем строк и столбцов
# 3. Определить какой тип данных имеют столбцы

# from pandas import read_csv

# data = read_csv("california_housing_test.csv") # функция read_csv в которую мы отдаем файл california_housing_test.csv

# print(data.shape) # показывает количество строки количество столбцов

# print(data) # dataframee т.е. таблица с данными

# print(data.dtypes) # показывает свойства (типизация) столбцов

# print(data.info())

# print(data.describe())

##################################################################################
# 1. Прочесть с помощью pandas файл
# california_housing_test.csv, который находится в папке
# sample_data
# 2. Посмотреть сколько в нем строк и столбцов
# 3. Определить какой тип данных имеют столбцы

# from pandas import read_csv

# # 1. Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке
# data = read_csv("california_housing_test.csv")


# # 2. Посмотреть сколько в нем строк и столбцов
# print(data.shape)


# # 3. Определить какой тип данных имеют столбцы
# print(data.dtypes)


####################################################################################
# 1. Проверить есть ли в файле пустые значения
# 2. Показать median_house_value где median_income < 2
# 3. Показать данные в первых 2 столбцах
# 4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000


# from pandas import read_csv

# data = read_csv("california_housing_test.csv")

# # 1. Проверить есть ли в файле пустые значения
# print(data.isnull().sum()) # .isnull() метод который показывает есть ли путые значения в таблице, .sum() метод который показывает их сумму


# # 2. Показать median_house_value где median_income < 2
# print(data[data['median_income'] < 2]['median_house_value'])


# # 3. Показать данные в первых 2 столбцах
# print(data[['longitude', 'latitude']])

# print(data.iloc[:,:2])


# # 4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000
# print(data[(data['housing_median_age'] < 20)&(data['median_house_value'] > 70000)])

#####################################################################################
# 1. Определить какое максимальное и минимальное значение median_house_value
# 2. Показать максимальное median_house_value, где median_income = 3.1250
# 3. Узнать какая максимальная population в зоне минимального значения median_house_value

# from pandas import read_csv

# data = read_csv("california_housing_test.csv")

# # 1. Определить какое максимальное и минимальное значение median_house_value
# print(data['median_house_value'].max(), data['median_house_value'].min())


# # 2. Показать максимальное median_house_value, где median_income = 3.1250
# print(data[data['median_income']==3.1250]['median_house_value'].max())


# # 3. Узнать какая максимальная population в зоне минимального значения median_house_value
# print(data[data['median_house_value'] == data['median_house_value'].min()]['population'].max())