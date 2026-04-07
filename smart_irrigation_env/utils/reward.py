def compute_reward(soil):
    if 40 <= soil <= 70:
        return 10, "Optimal Moisture"
    elif soil < 40:
        return -5, "Too Dry"
    else:
        return -7, "Overwatered"