#Câu a: Tính tổng các số chia hết cho 7 nhưng không chia hết cho 5 trong khoảng từ 2000 đến 4000:
tong_a = sum(i for i in range(2000, 4001) if i % 7 == 0 and i % 5 != 0)
print(tong_a)

#Câu b: Tính tổng các số chia hết cho 4 nhưng không chia hết cho 6 trong khoảng từ 500 đến 1000:
tong_b = sum(i for i in range(500, 1001) if i % 4 == 0 and i % 6 != 0)
print(tong_b)