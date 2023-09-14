# File: Zeller.py
# 
# Course Name: CS303E
#
# Date: 2/3/2023

# this program will determine the day based on an inputed date.
def main():
    y = int(input("\nEnter year (e.g., 2008): "))
    # determine if year input is legal
    if y < 1753:
        print("Year must be > 1752.  Illegal year entered:", y, "\n")
        return

    m = int(input("Enter month (1-12): "))
    # determine if month input is legal
    if m < 1 or m > 12:
        print("Month must be in [1..12]. Illegal month entered: ", m, "\n")
        return
    # adjust month and year values if in January or February
    if m == 1 or m == 2:
        m = m + 12
        y = y - 1

    d = int(input("Enter day of the month (1-31): "))
    # determine if day input is legal
    if d < 1 or d > 31:
        print("Day must be in [1..31]. Illegal day entered: ", d, "\n")
        return

    # calculate year of the century
    k = y % 100
    # calculate which century
    j = y // 100
    # calculate variable h to find day of the week
    h = (d + (13 * (m + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7

    # print what day
    if h == 0:
        print("Day of the week is Saturday")

    if h == 1:
        print("Day of the week is Sunday")

    if h == 2:
        print("Day of the week is Monday")

    if h == 3:
        print("Day of the week is Tuesday")

    if h == 4:
        print("Day of the week is Wednesday")

    if h == 5:
        print("Day of the week is Thursday")

    if h == 6:
        print("Day of the week is Friday")


main()
