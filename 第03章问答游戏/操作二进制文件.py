import struct

# 数据编码二进制
file_name = "./resource/text_data.txt"
format_string="i"#int 4

file = open(file_name, 'wb+')
for n in range(1, 1000):
    number = struct.pack(format_string, n)
    file.write(number)
file.close()

print("+" * 40)

# 读取二进制数据
file = open(file_name, 'rb')
b = file.read()
print(b)
file.close()

print("+" * 40)

# 读取出不同数据类型数据
file = open(file_name, 'rb')
size = struct.calcsize(format_string)  # a-----4

bytes_read = file.read(size)

while bytes_read:
    value = struct.unpack(format_string, bytes_read)  # tuple
    value = value[0]
    # print(str(value) + ' ')
    print(value, end=" ")

    bytes_read = file.read(size)

a = file.read()
file.close()
print(a)

print(
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    "END"
    "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


