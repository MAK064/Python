cur_x = 1 # The algorithm starts at x =
gamma = 10**-0 # step size multiplier
precision = 0.00001
previous_step_size = 1
max_iters = 10**5 # maximum number of iterations
iters = 0 #iteration counter

df = lambda x: x**2

while (previous_step_size > precision) & (iters < max_iters):
    prev_x = cur_x
    cur_x -= gamma * df(prev_x)
    previous_step_size = abs(cur_x - prev_x)
    iters+=1

print("The local minimum occurs at", cur_x)
