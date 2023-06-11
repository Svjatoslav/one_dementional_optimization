

def recursion_function(self, left, right, accuracy, iterations_tpm):

    if right - left < accuracy:
        return iterations_tpm, (right + left) / 2

    x_1 = (right - left)/4 + left
    x_2 = (right - left)/4 * 2 + left

    f_1 = self.target_function(x_1)
    f_2 = self.target_function(x_2)

    iterations_tpm += 2

    if f_1 <= f_2:
        return recursion_function(self, left, x_2, accuracy, iterations_tpm)
    else:
        x_3 = (right - left) / 4 * 3 + left
        f_3 = self.target_function(x_3)
        iterations_tpm += 1
        if f_2 <= f_3:
            return recursion_function(self, x_1, x_3, accuracy, iterations_tpm)
        else:
            return recursion_function(self, x_2, right, accuracy, iterations_tpm)


def trial_point_method(self, accuracy):
    return recursion_function(self, self.left_border, self.right_border, accuracy, 0)


