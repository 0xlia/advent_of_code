


# calculate size of rectangle between two red tiles
def getRectangleArea(tile0, tile1):
    """
    Docstring for getRectangleArea
    
    :param tile0: (x0, y0)
    :param tile1: (x1, y1)

    >>> getRectangleArea((2,5), (9,7))
    24
    >>> getRectangleArea((7,1),(11,7))
    35
    >>> getRectangleArea((7,3),(2,3))
    6
    """

    return (abs(tile1[0] - tile0[0]) + 1) * (abs(tile1[1] - tile0[1]) + 1)

    
def main():
    red_tiles = []
    green_tiles = []

    with open("input9.txt") as f:
        for line in f.readlines():
            red_tile = line.strip().split(",")
            x, y = red_tile
            red_tiles.append((int(x), int(y)))

    # green tiles 
    for (x0, y0), (x1, y1) in zip(red_tiles, red_tiles[1:] + [red_tiles[0]]):
        # x0 == x1
        if x0 == x1:
            y_min = min(y0, y1)
            y_max = max(y0, y1)
            for y in range(y_min +1, y_max):
               green_tiles.append((x0, y)) 
        # y0 == y1
        elif y0 == y1:
            x_min = min(x0, x1)
            x_max = max(x0, x1)
            for x in range(x_min+1, x_max):
                green_tiles.append((x,y0))
        

    # area size, tile0, tile1
    largest_area = (0,0,0)

    for tile0_index in range(len(red_tiles)):
        for tile1_index in range(tile0_index):
            area_size = getRectangleArea(red_tiles[tile0_index], red_tiles[tile1_index])
            if area_size > largest_area[0]:
                largest_area = (area_size, tile0_index, tile1_index)

    print(largest_area)
    print(green_tiles)




if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()