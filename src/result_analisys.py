import numpy as np
import matplotlib.pyplot as plt
from One_D_Problem_file import One_D_Problem
from Trial_Point_Method_file import trial_point_method
import math


def super_target_function(self, x_, power, c1, c2, delta):
    return (x_ - delta) ** 2


def data_generating(accuracy, method):
    method_array = []

    for i in range(1000):
        pr1 = One_D_Problem()
        pr1.left_border = -2
        pr1.right_border = 2

        power = np.random.randint(low=1, high=4)
        c1 = np.random.randint(low=-10, high=10) / 10
        c2 = np.random.randint(low=-10, high=10) / 10
        delta_x = np.random.randint(low=-1, high=1) * (pr1.right_border - pr1.left_border) / 2

        #  delta_x = -2 => min
        #  delta_x = 0 or 2 => max
        pr1.target_function = lambda x_: super_target_function(pr1, x_, power, c1, c2, delta_x)

        method_array.append(method(pr1, accuracy)[0])  # возвращаю только количество итераций

    return np.mean(method_array)


def graphics():
    """
    Добавить сбда другие два метода
    :return:
    """
    accuracy_array = [-1, -3, -5, -7, -9, -11, -13, -15]
    tpm_method_array = []

    for accuracy in accuracy_array:
        tpm_method_array.append(data_generating(10 ** accuracy, trial_point_method))

    tpm_method_theory_min = []
    tpm_method_theory_max = []
    for accuracy in accuracy_array:
        tpm_method_theory_min.append(2 * math.log2(4 / (10 ** accuracy)))
        tpm_method_theory_max.append(3 * math.log2(4 / (10 ** accuracy)))

    plt.plot([10 ** x for x in accuracy_array], tpm_method_array, label='tpm')
    plt.plot([10 ** x for x in accuracy_array], tpm_method_theory_min, label='min tpm theory')
    plt.plot([10 ** x for x in accuracy_array], tpm_method_theory_max, label='max tpm theory')
    plt.xlabel('accuracy')
    plt.ylabel('function calculation')
    plt.legend()
    plt.semilogx()
    plt.show()


graphics()
