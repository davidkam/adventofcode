f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()


max_seat_num = 0
for line in data:
    seat = line[-3:]
    row = line.replace(seat, "")
    row_bin = row
    row_bin = row_bin.replace('F','0')
    row_bin = row_bin.replace('B','1')
    row_num = int(row_bin,2)

    seat_bin = seat
    seat_bin = seat_bin.replace('R','1')
    seat_bin = seat_bin.replace('L','0')
    seat_num = int(seat_bin, 2)

    seat_sum = 8 * row_num + seat_num
    if seat_sum > max_seat_num:
        max_seat_num = seat_sum


print(max_seat_num)
