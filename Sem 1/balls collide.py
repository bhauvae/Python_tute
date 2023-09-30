def balls_collide(b1, b2):
    if b1[2] + b2[2] > ((b1[0] - b2[0]) ** 2 + (b1[1] - b2[1]) ** 2) ** 0.5:
        return True
    else:
        return False

b1 = (1, 1, 3)
b2 = (2, 2, 6)

print(balls_collide(b1,b2))