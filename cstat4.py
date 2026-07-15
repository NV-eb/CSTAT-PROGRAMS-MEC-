def calc(data):
    avg_dict={}
    for key, values in data.items():
        avg = sum(values)/len(values)
        avg_dict[key]=avg;
    return avg_dict
    
    
data = {"Math":[90,78,98],"English":[90,88,85],"Science":[98,99,91]}
result=calc(data)

print(result)
