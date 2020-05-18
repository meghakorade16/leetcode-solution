temp = [25, 2, 3, 57, 38, 41]

st = ""
max = 0;
for i in temp:
    st += str(i)
temp = []
for i in st:
    if st.count(i) >= max:
        max = st.count(i)
        if i not in temp:
            temp.append(i)
print(temp)





