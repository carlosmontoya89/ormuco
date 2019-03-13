from  overlap.overlaps import isOverlapping

def test_overlaps():
    assert isOverlapping((1,5), (2,6))==True, "it should overlaps"
    assert isOverlapping((2, 4), (6,8))==False, "it should not overlaps"
    assert isOverlapping((2, 4), (4,10))==True, "it should not overlaps"
    assert isOverlapping((10,20), (15,25))==True, "it should not overlaps"
    assert isOverlapping((30,35), (36,38))==False, "it should not overlaps"
    assert isOverlapping((11,25), (16,28))==True, "it should not overlaps"
    assert isOverlapping((1,15), (6,18))==True, "it should not overlaps"
    assert isOverlapping((25,55), (66,78))==False, "it should not overlaps"
    

if __name__ == "__main__":
    test_overlaps()
    print("Everything passed")