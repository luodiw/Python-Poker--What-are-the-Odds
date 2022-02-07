"""
Output table of percent of hand rankings with
pairs, 2 pairs, flushes, and high card generated from
range of 10,000 - 100,000 hands
"""
from card_deck import *
from hand_rankings import *

if __name__ == "__main__":
    row_format_header = "{:>10} {:>15}   {:^5} {:>15}   {:^5} {:>15}   {:^5} {:>15}   {:^5}"
    row_format = "{:>10} {:>15}   {:0>5.2f} {:>15}   {:0>5.2f} {:>15}   {:0>5.2f} {:>15}   {:0>5.2f}"
    for run in range(10):
        deck = build_deck()
        hands = {'hands': 0, 'Flush': 0, 'Two pair': 0, 'Pair': 0, 'High card': 0}
        if run == 0:
            print(
                row_format_header.format("# of hands", "pairs", "%", "2 pairs", "%", "flushes", "%", "high card", "%"))
        for hand in range((run + 1) * 10000):
            _, deck = deal_cards(deck)
            if is_flush(deck, hands) or is_pair(deck, hands) or is_two_pair(deck, hands):
                hands["hands"] += 1
            else:
                hands["High card"] += 1
                hands["hands"] += 1
        print(row_format.format(f"{run + 1}0,000", hands["Pair"], round(hands["Pair"] / ((run + 1) * 10000) * 100, 2),
                                hands["Two pair"], round(hands["Two pair"] / ((run + 1) * 10000) * 100, 2),
                                hands["Flush"], round(hands["Flush"] / ((run + 1) * 10000) * 100, 2),
                                hands["High card"], round(hands["High card"] / ((run + 1) * 10000) * 100, 2)))
