import sys

ladder_height = sys.argv[1]


def draw_ladder(steps):

    # for i in range(1, steps+1):
    #     spaces = " " * (steps - i)
    #     hashes = "#"  * (i)
    #     print(spaces + hashes)

    for i in range(1, steps+1):
        hashes = "#"  * (i)
        print("{:>{steps}}".format(hashes, steps=steps))



if __name__ == "__main__":
    ladder_height = int(ladder_height)
    draw_ladder(ladder_height)