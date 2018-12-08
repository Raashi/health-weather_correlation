"""
sequence_max(x) - вычисление максимумов временного ряда x
sequence_distance(x, y, insert_zero) - вычисление расстояний от максимумов образца x до ближайшего максимума эталона y (c добавлением 0 в начало списка x или без)
(-)func(x, y) - Суммирование элементов двух разных списков
sum_list(x) - Почленное суммирование списков списка
concat_list(x) - Конкатенация списков списка x
stat_analysis_distances(x,y) - Статистический анализ ряда распределений расстояний от x до y
stat_analysis(z) - Статистический анализ ряда распределений z
visual_analysis(x) - Визуальный анализ ряда распределений (гистограмма, ядерная оценка плотности и кривая Гаусса)
visual_analysis2(x,y) - Визуальный анализ двух рядов распределений (два рисунка с гистограммой, ядерной оценкой плотности и кривой Гаусса)
test_normal(x, qq, base) - Тестирование распределения на нормальность
                           (100 прогонов теста К-С, без QQ-теста) или
                           (1000 прогонов теста К-С, с QQ-тестом и графиком)
graph_kde(xr1, xr2, xr3, xr4) - Построение 4-х ядерных оценок плотности и кривой Гаусса
graph_kde3(xr1, xr2, xr3) - Построение 3-х ядерных оценок плотности и кривой Гаусса
graph_kde_all(x, y, u, v, w) - Построение 4-х ядерных оценок плотности и кривой Гаусса для всех пациентов и эталона w
"""
from operator import add

import numpy as np
import scipy.stats as st

from matplotlib.figure import Figure

from science.classes import CATS


class StatComputingError(ValueError):
    pass


# TODO: этой функции больше не видно: убрать или переименовать или что вообще
def distrib(x):
    """функция вычисления распределения расстояний от максимумов ряда пациента до ближайшего максимума Kp"""
    y = []
    for i in range(7):
        y.append(x.count(i - 3))
    return y


def sequence_max(x):
    """Вычисление максимумов временного ряда"""
    y = []
    for i in range(1, len(x) - 1):
        if x[i - 1] <= x[i] and x[i + 1] <= x[i]:
            y.append(1)
        else:
            y.append(0)
    return y


def sequence_distance(x, y, *, insert_zero):
    """
    Вычисление расстояний от максимумов ряда пациента до ближайшего максимума Kp:
    "-" максимум Kp находится слева, "+" максимум Kp находится справа
    """
    if insert_zero:
        x.insert(0, 0)
    u = []
    for i in range(len(x)):
        if x[i] == 1:
            for j in range(len(y)):
                if (i - j >= 0 and y[i - j] == 1) and (i + j < len(y) and y[i + j] == 1):
                    if j == 0:
                        u.append(j)
                    else:
                        u.append(j)
                        u.append(-j)
                    break
                elif i - j >= 0 and y[i - j] == 1:
                    u.append(j)
                    break
                elif i + j < len(y) and y[i + j] == 1:
                    u.append(-j)
                    break
    return u


def sum_list(x):
    """Почленное суммирование списков списка"""
    y = [0] * len(x[0])
    for i in range(len(x)):
        y = list(map(add, y, x[i]))
    return y


def concat_list(x):
    """Конкатенация списков списка"""
    y = []
    for i in range(len(x)):
        y += x[i]
    return y


def stat_analysis_distances(x, y):
    """Статистический анализ ряда распределений расстояний от x до y"""
    z = sequence_distance(sequence_max(x), sequence_max(y), insert_zero=True)
    w = [np.mean(z), np.std(z), st.t.interval(0.95, len(z) - 1, loc=np.mean(z), scale=st.sem(z))]
    return w


def stat_analysis(z):
    """Статистический анализ ряда распределений"""
    return [np.mean(z), np.std(z), st.t.interval(0.95, len(z) - 1, loc=np.mean(z), scale=st.sem(z))]


def visual_analysis(x, base: Figure):
    """Визуальный анализ ряда распределений"""
    fig = base.subplots()
    _range = np.linspace(-3, 4, 100)
    # plt.style.use('seaborn-white')
    fig.hist(x, bins=7, range=(-3, 4), normed=True, alpha=0.5, histtype='stepfilled', color='steelblue',
             edgecolor='none')
    fig.plot(_range, st.norm.pdf(_range, np.mean(x), np.std(x)))
    fig.plot(_range, st.gaussian_kde(x)(_range))


def visual_analysis2(x, y, base: Figure):
    """Визуальный анализ двух рядов распределений"""
    fig = base.subplots(2)
    rng = np.linspace(-3, 4, 100)
    # plt.style.use('seaborn-white')
    fig[0].hist(x, bins=11, range=(-3, 4), normed=True, alpha=0.5, histtype='stepfilled', color='steelblue',
                edgecolor='none')
    fig[0].plot(rng, st.norm.pdf(rng, np.mean(x), np.std(x)))
    fig[0].plot(rng, st.gaussian_kde(x)(rng))
    fig[1].hist(y, bins=11, range=(-3, 4), normed=True, alpha=0.5, histtype='stepfilled', color='steelblue',
                edgecolor='none')
    fig[1].plot(rng, st.norm.pdf(rng, np.mean(y), np.std(y)))
    fig[1].plot(rng, st.gaussian_kde(y)(rng))


def test_normal(x, *, qq: bool, base: Figure = None):
    """Тестирование распределения на нормальность"""
    report = {}
    alpha = 0.05
    # print("Тест нормальности Шапиро-Вилка")
    # stat, p = shapiro(x)
    # print('Statistics=%.3f, p=%.3f' % (stat, p))
    # alpha = 0.05
    # if p > alpha:
    #     print('Образец выглядит гауссовским (не может отклонить гипотезу H0)')
    # else:
    #     print('Образец не выглядит гауссовским (отклонить гипотезу H0)')
    stat, p = st.shapiro(x)
    report["shapiro-wilk"] = {
        "name": "Shapiro-Wilk Test",
        "alpha": alpha,
        "stat": stat,
        "p": p,
        "res": p > alpha
    }

    # print("Тест нормальности Д'Агостино-Пирсона")
    # if len(x) > 19:
    #     x1 = x
    # else:
    #     x1 = []
    #     for i in range(50):
    #         x1.append(random.choice(x))
    # stat, p = normaltest(x1)
    # print('Statistics=%.3f, p=%.3f' % (stat, p))
    # if p > alpha:
    #     print('Образец выглядит гауссовским (не может отклонить гипотезу H0)')
    # else:
    #     print('Образец не выглядит гауссовским (отклонить H0)')
    stat, p = st.normaltest(x)
    report["agostino_pearson"] = {
        "name": "D'Agostino and Pearson's Test",
        "alpha": alpha,
        "stat": stat,
        "p": p,
        "res": p > alpha
    }

    # print("Тест нормальности Андерсона-Дарлинга")
    # result = anderson(x)
    # print('Statistic: %.3f' % result.statistic)
    # p = 0
    # for i in range(len(result.critical_values)):
    #     sl, cv = result.significance_level[i], result.critical_values[i]
    #     if result.statistic < result.critical_values[i]:
    #         print('%.3f: %.3f, Образец выглядит гауссовским (не может отклонить гипотезу H0)' % (sl, cv))
    #     else:
    #         print('%.3f: %.3f, Образец не выглядит гауссовским (отклонить H0)' % (sl, cv))

    # result[0] = result.statistic
    # result[1] = result.critical_values
    # result[2] = result.significance_level
    # result = anderson(data_reference)
    statistic, critical_values, significance_level = st.anderson(x)
    report["anderson"] = {
        "name": "Anderson-Darling Test",
        "statistic": statistic,
        "critical": critical_values,
        "res": []
    }
    for sl, cv in zip(significance_level, critical_values):
        report["anderson"]["res"].append((sl, cv, statistic < cv))

    # print("Тест нормальности Колмогорова-Смирнова")
    # num_tests = 10 ** 2
    # num_rejects = 0
    # for i in range(num_tests):
    #     normed_data = (x - mean(x)) / std(x)
    #     D, pval = stats.kstest(normed_data, 'norm')
    #     if pval < alpha:
    #         num_rejects += 1
    # ratio = float(num_rejects) / num_tests
    # print("Результаты теста Колмогорова-Смирнова: ", "из 100 прогонов доля",
    #       '{}/{} = {:.2f} отклоняет гипотезу H0 на уровне отклонения {}'.format(num_rejects, num_tests, ratio, alpha))
    # print("Результаты теста Колмогорова-Смирнова: ", "из 1000 прогонов доля",
    #       '{}/{} = {:.2f} отклоняет гипотезу H0 на уровне отклонения {}'.format(num_rejects, num_tests, ratio, alpha))
    num_tests = 10 ** (3 if qq else 2)
    num_rejects = 0
    for i in range(num_tests):
        normed_data = (x - np.mean(x)) / np.std(x)
        D, pval = st.kstest(normed_data, 'norm')
        if pval < alpha:
            num_rejects += 1
    ratio = float(num_rejects) / num_tests
    report["ks"] = {
        "name": "Kolmogorov-Smirnov Test",
        "num_tests": num_tests,
        "num_rejects": num_rejects,
        "ratio": ratio,
        "alpha": alpha
    }
    if qq and base is None:
        raise StatComputingError('Не передана фигура для рисования графика')
    if qq:
        st.probplot(x, dist="norm", plot=base)
    return report


def graph_kde(xr: list, base: Figure):
    """Построение 4-х ядерных оценок плотности и кривой Гаусса"""
    fig = base.subplots(1)
    # инициализация цветов
    colors = [("blue", "синий"),
              ("red", "красный"),
              ("green", "зеленый"),
              ("yellow", "желтый")]
    # задаем заголовки
    titles = ["{} график – {}".format(colors[idx][1], CATS[idx][1])
              for idx in range(4) if xr[idx] is not None]
    titles.append("черный штрихпунктирный график – стандартная кривая Гаусса")
    # отфлитровываем отсутствующие категории
    colors = [colors[idx][0] for idx in range(4) if xr[idx] is not None]
    xr = [el for el in xr if el is not None]
    rng = np.linspace(0.9 * np.min(xr[0]), 1.1 * np.max(xr[0]), 106)
    for xi, c in zip(xr, colors):
        fig.plot(rng, st.gaussian_kde(xi)(rng), color=c)

    fig.plot(rng, st.norm.pdf(rng, 0, 1), '-.k')
    title = '\n'.join([titles[idx] + ', ' + titles[idx + 1] if idx < len(titles) - 1 else titles[idx]
                       for idx in range(0, len(titles) - 1, 2)]) + '\n' + titles[-1]
    fig.set(xlim=(-4, 4), ylim=(0, 0.5), xlabel='x', ylabel='', title=title)
    # fig.set_title(title)
    # fig.set_xlim((-4, 4)), fig.set_ylim((0, 0.5))
    # fig.set_xlabel('x'), fig.set_ylabel('')

# def graph_kde3(xr1, xr2, xr3):
#     """Построение 3-х ядерных оценок плотности и кривой Гаусса"""
#     _range = np.linspace(0.9 * np.min(xr1), 1.1 * np.max(xr1), 100)
#     plt.plot(_range, st.gaussian_kde(xr1)(_range), color='blue')
#     plt.plot(_range, st.gaussian_kde(xr2)(_range), color='red')
#     plt.plot(_range, st.gaussian_kde(xr3)(_range), color='green')
#     plt.plot(_range, norm.pdf(_range, 0, 1), '-.k')
#     plt.style.use('seaborn-white')
#     ax.set(xlim=(-4, 4), ylim=(0, 0.5),
#            xlabel='x', ylabel='',
#            title='синий график - с физ.нагрузкой, красный график - после отдыха , \n зеленый график - с эмоц.нагрузкой, \n черный штрихпунктирный график - стандартная кривая Гаусса')
#     plt.show()


# def graph_kde_all(x, y, u, v, w):
#     """Построение 4-х ядерных оценок плотности и кривой Гаусса для всех пациентов и эталона w"""
#     for j in range(len(x)): graph_kde(sequence_distance(sequence_max(x[j]), sequence_max(w)),
#                                       sequence_distance(sequence_max(y[j]), sequence_max(w)),
#                                       sequence_distance(sequence_max(u[j]), sequence_max(w)),
#                                       sequence_distance(sequence_max(v[j]), sequence_max(w)))
