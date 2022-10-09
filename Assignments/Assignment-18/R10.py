sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
}
temp = min(sample_dict.values())
for i in sample_dict:
    if sample_dict[i] == temp:
        print(i)
