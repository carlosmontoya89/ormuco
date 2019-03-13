def versionCompare(v1, v2):    
    arr1 = v1.split(".") 
    arr2 = v2.split(".") 
    arr0= [0]*max(len(arr1),len(arr2)) 
    arr1=arr1+arr0
    arr2=arr2+arr0
     
    i = 0      
    
    while(i < len(arr1)):

        #Version2 > Version1
        if int(arr2[i]) > int(arr1[i]): 
            return -1   

        #Version1 > Version2
        if int(arr1[i]) > int(arr2[i]): 
            return 1
          
        i += 1
    #Version2 = Version1        
    return 0