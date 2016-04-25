def from_DT_State_to_low_high(x):
    # 0 - 1 translated to low / high
    if str(x) == "0":
        return "low"
    if str(x) == "1":
        return "high"

