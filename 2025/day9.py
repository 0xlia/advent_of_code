from collections import defaultdict, namedtuple
import numpy as np
import matplotlib.pyplot as plt
from shapely import Polygon

Tile = namedtuple('Tile', ['x', 'y'] )

# calculate size of rectangle between two red tiles
def getRectangleArea(tile0, tile1):
    """
    Docstring for getRectangleArea
    
    :param tile0: Tile(x0, y0)
    :param tile1: Tile(x1, y1)

    >>> getRectangleArea(Tile(2,5), Tile(9,7))
    24
    >>> getRectangleArea(Tile(7,1), Tile(11,7))
    35
    >>> getRectangleArea(Tile(7,3), Tile(2,3))
    6
    """

    return (abs(tile1.x - tile0.x) + 1) * (abs(tile1.y - tile0.y) + 1)

    
def main():
    # fill red_tiles with Tiles
    red_tiles = []
    with open("input9.txt") as f:
        for line in f.readlines():
            red_tile = line.strip().split(",")
            x,y = map(int, red_tile)
            red_tiles.append(Tile(x, y))

    polygon = Polygon(red_tiles)
    polygon.area
    print(polygon)

    # # green tiles 
    # green_tiles = []
    # inner_green_tiles = set()
    # for tile0, tile1 in zip(red_tiles, red_tiles[1:] + [red_tiles[0]]):
    #     # x0 == x1
    #     if tile0.x == tile1.x:
    #         y_min = min(tile0.y, tile1.y)
    #         y_max = max(tile0.y, tile1.y)
    #         for y in range(y_min +1, y_max):
    #            green_tiles.append(Tile(tile0.x, y)) 

    #     # y0 == y1
    #     # if y0 == y1: tile2 x==x, y0, y1
    #     elif tile0.y == tile1.y:
    #         x_min = min(tile0.x, tile1.x)
    #         x_max = max(tile0.x, tile1.x)
    #         for x in range(x_min+1, x_max):
    #             green_tiles.append(Tile(x, tile0.y))

    # area size, tile0, tile1
    largest_area = (0,0,0)

    for tile0_index in range(len(red_tiles)):
        for tile1_index in range(tile0_index):
            tile0 = red_tiles[tile0_index]
            tile1 = red_tiles[tile1_index]
            tile2 = Tile(tile0.x, tile1.y)
            tile3 = Tile(tile1.x, tile0.y)
            rectangle = Polygon([tile0, tile2, tile1, tile3])
            print(rectangle)
            if polygon.covers(rectangle):
                area_size = getRectangleArea(red_tiles[tile0_index], red_tiles[tile1_index])
                if area_size > largest_area[0]:
                    largest_area = (area_size, tile0_index, tile1_index)

    print(largest_area)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()