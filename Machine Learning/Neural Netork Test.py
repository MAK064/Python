def axon(ax_in):
    output = 1
    if ax_in <= 0:
        output = 0
    return output

def soma(speed, straight_legged, threshold, w1, w2):
    x = 0
    x = straight_legged*w1 + speed*w2 + threshold
    y = axon(x)
    return y

w1 = 2/3
w2 = 3/2
t = 0
sl = 0.6
sp = 0.8

print(soma(sp,sl,t,w1,w2))
