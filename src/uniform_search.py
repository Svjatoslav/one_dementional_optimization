def uniform_search_method(self, n, accuracy):
    num_calls = 0  # initialize function call counter
    h = (self.right_border - self.left_border) / n
    x = [self.left_border + i * h for i in range(0, n)]
    while True:
        j, num_calls = fun_request(self, x, num_calls)
        if j == 0:
            x_new = [self.left_border + i*h for i in range(2)]
        elif j == n-1:
            x_new = [self.right_border - i*h for i in range(2)]
        else:
            x_new = [x[j-1], x[j+1]]
        if x_new[1] - x_new[0] < accuracy:
            return (x_new[0] + x_new[1]) / 2, num_calls
        h = (x_new[1] - x_new[0]) / n
        x = [x_new[0] + i * h for i in range(0, n)]


def fun_request(self, x, num_calls):
    f = [self.target_function(xi) for xi in x]
    num_calls += len(f)
    j = f.index(min(f))
    return j, num_calls
