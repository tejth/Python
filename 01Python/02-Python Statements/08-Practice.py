# st ="print only the words that starts with  s in this sentence"
# list1= st.split();
# for item in list1:
#     if item[0] == 's':
#         print(item + " " , end="")

# for i in range(0,11):
#     if(i%2==0):
#         print(i)


# lst = [x for x in range (1,51) if x%3==0]
# print(lst)

# st ="print only the words that starts with  s in this sentence"
# list1= st.split();
# for item in list1:
#     if len(item)%2==0:
#         print("even" + " ", item)


# for i in range(1,101):
#     if i%3==0:
#         print("Fizz " , i)
#     elif i %5==0:
#         print("Buzz ", i)
#     elif (i%3==0) and (i%5==0):
#         print("FizzBuzz ", i)
#     else:
#         pass

st = 'Create a list of the first letters of every word in this string'
lsitstr = st.split()
lststr = [ x[0] for x in lsitstr ]
print(lststr)
        