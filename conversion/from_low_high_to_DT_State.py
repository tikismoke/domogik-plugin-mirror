def from_low_high_to_DT_State(x):
    # low - high translated to 0 - 1
    if x == "low":
        return 0
    if x == "high":
        return 1