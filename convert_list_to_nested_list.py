data_list = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

new_list = [data_list[i:i+1] for i in range(0, len(data_list), 1)]

print(new_list)