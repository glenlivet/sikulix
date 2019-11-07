for i in range(4):
    moveMouse(reg, 100 + ran_x, -75 - ran_y)
    if i%2 == 0:
        ran_x = - ran_x
        ran_y = - ran_y
    else:
        ran_x = randv(0, 20)
        ran_y = randv(0, 15)
    clickCurrentPoint(reg)
    wait(random.uniform(1.5, 2.0))
    print Env.getMouseLocation()