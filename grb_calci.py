

def levels(prev_open,prev_high,prev_low,prev_close,cur_high,cur_low):
    prev_range=prev_high-prev_low

    cur_range=cur_high-cur_low

    Range_factor=prev_range+cur_range

    Golden=Range_factor*0.618

    buy_level=prev_close+Golden
    sell_level=prev_close-Golden
    default=0
    buy_sl=0.995*buy_level
    sell_sl=1.005*sell_level
    if cur_high>buy_level or cur_low<sell_level:
        default=1
        buy_level=cur_high
        sell_level=cur_low
        if 0.995*buy_level<cur_low:
            buy_sl=cur_low
        else:
            buy_sl=0.995*buy_level
        if 1.005*sell_level>cur_high:
            sell_sl=cur_high
        else:
            sell_sl=1.005*sell_level
    return buy_level,buy_sl,sell_level,sell_sl


