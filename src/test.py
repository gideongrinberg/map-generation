from cell import *
from tile import Tile, Direction

def test_get_cell():
    tile1 = Tile.from_2d_array([[Cell.Indoor, Cell.Outdoor], [Cell.Indoor, Cell.Outdoor]])

    assert tile1.get_cell(Direction.TOP_LEFT) == tile1.tiles[0][0]
    assert tile1.get_cell(Direction.TOP_RIGHT) == tile1.tiles[0][1]
    
    assert tile1.get_cell(Direction.BOTTOM_LEFT) == tile1.tiles[1][0]
    assert tile1.get_cell(Direction.BOTTOM_RIGHT) == tile1.tiles[1][1]

def test_creates():
    tile1 = Tile.from_2d_array([[Cell.Indoor, Cell.Outdoor], [Cell.Indoor, Cell.Outdoor]])

    assert tile1.get_cell(Direction.TOP_LEFT) == Cell.Indoor
    assert tile1.get_cell(Direction.TOP_RIGHT) == Cell.Outdoor
    
    assert tile1.get_cell(Direction.BOTTOM_LEFT) == Cell.Indoor
    assert tile1.get_cell(Direction.BOTTOM_RIGHT) == Cell.Outdoor


def test_find_match():
    tile1 = Tile.from_2d_array([[Cell.Indoor, Cell.Outdoor], [Cell.Indoor, Cell.Outdoor]])
    tile2 = tile1.find_match()

    assert tile1.is_match(tile2)

    assert tile1.get_cell(Direction.TOP_LEFT) == tile2.get_cell(Direction.TOP_RIGHT)
    assert tile1.get_cell(Direction.TOP_RIGHT) == tile2.get_cell(Direction.TOP_LEFT)


if __name__ == "__main__":
    test_funcs = [test_creates, test_find_match, test_get_cell]

    total = len(test_funcs)
    failed = 0
    passed = 0

    for test in test_funcs:
        try:
            test()
        except AssertionError:
            failed += 1
            print(f"Test {test.__str__()} failed assertion.")
        except: 
            print(f"Test errored.")
        else:
            passed += 1
    
    print(f"Failed: {failed}. Passed: {passed}. Total: {total}")
