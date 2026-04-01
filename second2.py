try:
    arr=[1,2,3,4]
    print(arr[6])
except IndexError:
    print("index not found")
else:
    print("number printed successfully")