def bouncing_ball(h, bounce, window):
    if h > 0 and 0 < bounce < 1 and window < h:
        ball_height = h
        count = 0
        while ball_height > window:
            count += 1
            ball_height *= bounce
            if ball_height > window:
                count += 1
        return count 
    return -1