# Задача №63. Решение в группах
# 1. Изобразите отношение households к population с помощью точечного графика
# 2. Визуализировать longitude по отношения к median_house_value, используя линейный график
# 3. Представить гистограмму по housing_median_age
# 4. Изобразить гистограмму по median_house_value с оттенком housing_median_age


# 1. Изобразите отношение households к population с помощью точечного графика

# from pandas import read_csv
# from seaborn import scatterplot, relplot, histplot
# from matplotlib.pyplot import show

# data = read_csv("california_housing_test.csv")


# def firsr():
#     scatterplot(data=data, x='households', y='population')
#     show()
# firsr()


# 2. Визуализировать longitude по отношения к median_house_value, используя линейный график

# def second():
#     relplot(data=data, x='longitude', y='median_house_value', kind='line')
#     show()
# second()


# 3. Представить гистограмму по housing_median_age

# def third():
#     histplot(data=data, x='housing_median_age')
#     show()
# third()


# 4. Изобразить гистограмму по median_house_value с оттенком housing_median_age

# def fourth():
#     histplot(data=data, x='median_house_value', hue='housing_median_age')
#     show()
# fourth()

##############################################################################
# Задача №65. Решение в группах
# Написать EDA для датасета про пингвинов
# Необходимо:
# ● Использовать 2-3 точечных графика
# ● Применить доп измерение в точечных графиках, используя
# аргументы hue, size, stile
# ● Использовать PairGrid с типом графика на ваш выбор
# ● Изобразить Heatmap
# ● Использовать 2-3 гистограммы
# Чтобы подключить датасет с
# пингвинами, воспользуйтесь данным скриптом:
# penguins = sns.load_dataset("penguins")
# penguins.head()


# Написать EDA для датасета про пингвинов
# from seaborn import load_dataset, scatterplot, PairGrid, heatmap
# from matplotlib.pyplot import show
# from matplotlib import pyplot

# data = load_dataset('penguins')

# ● Использовать 2-3 точечных графика
# def first():
#     scatterplot(data=data, x="flipper_length_mm", y="body_mass_g")
#     show()
# first()


# ● Применить доп измерение в точечных графиках, используя аргументы hue, size, stile

# def second():
#     scatterplot(data=data, x="flipper_length_mm", y="body_mass_g", hue='sex', size='species', style='island')
#     show()
# second()


# ● Использовать PairGrid с типом графика на ваш выбор
# def third():
#     x_vars = ["body_mass_g", "bill_length_mm", "flipper_length_mm"]
#     y_vars = ['sex']
#     pg = PairGrid(data=data, x_vars=x_vars, y_vars=y_vars, hue='species')
#     pg.map(scatterplot)
#     show()
# third()


# ● Изобразить Heatmap
# def fourth():
#     pivot_table = data.pivot_table(index='species', columns='island', values='body_mass_g', aggfunc='mean')
#     heatmap_plot = heatmap(pivot_table)
#     heatmap_plot.set_xlabel('Остров', size='14')
#     heatmap_plot.set_ylabel('Вид пингвинов', size='14')
#     pyplot.show()

# fourth()


# ● Использовать 2-3 гистограммы
# def fifth():
#     data['bill_length_mm'].hist(bins=8)
#     show()
# fifth()


#############################################################################
# 1. Создать новый столбец в таблице с
# пингвинами, который будет отвечать за
# показатель длины клюва пингвина.
# high - длинный(от 42)
# middle - средний(от 35 до 42)
# low - маленький(до 35)

from pandas import read_csv

data = read_csv('penguins.csv')

# Устанавливаем значение 'low' для bill_length_mm < 35
data.loc[data['bill_length_mm'] < 35, 'height_group'] = 'low'

# Устанавливаем значение 'middle' для 35 <= bill_length_mm < 42
data.loc[(data['bill_length_mm'] >= 35) & (data['bill_length_mm'] < 42), 'height_group'] = 'middle'

# Устанавливаем значение 'high' для bill_length_mm >= 42
data.loc[data['bill_length_mm'] >= 42, 'height_group'] = 'high'

# Сохраняем обновленные данные в CSV-файл
data.to_csv('penguins.csv', index=False)