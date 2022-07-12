def bouncing_ball(h, bounce, window):
    if h < 0 or bounce > 1 or bounce < 0 or window > h:
        return -1
    ball_height = h
    count = 0
    while ball_height > window:
        count += 1
        ball_height *= bounce
        if ball_height > window:
            count += 1
    return count 

print(bouncing_ball(30, 0.75, 1.5))