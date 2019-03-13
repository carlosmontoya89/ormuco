def isOverlapping(line1, line2):
    set1={i for i in range(line1[0],line1[1]+1)}
    set2={i for i in range(line2[0],line2[1]+1)}
    if set1 & set2:
        result=True
    else:
        result=False
    return result

	
if __name__ == '__main__':
    overlaps=isOverlapping((1,5), (2,6))
    print(overlaps)
