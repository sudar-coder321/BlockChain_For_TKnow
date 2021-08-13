import hashlib


def hash(obj):
    return hashlib.sha256(str(obj).encode('utf-8')).hexdigest()


if __name__ == '__main__':
    data1 = ['hello', 'world']
    data2 = 3
    data3 = 12892803140938.12329831
    data4 = """This is a sample data """
    data5 = {"key1": "value1",
             "key2": "value2",
             "key3": "value3",
             "key4": "value4",
             "key5": "value5"}
    data6 = set([1, 8, 2, 4, 5, 6])

    print(hash(data1)+":"+str(data1)+"\n")
    print(hash(data2)+":"+str(data2)+"\n")
    print(hash(data3)+":"+str(data3)+"\n")
    print(hash(data4)+":"+str(data4)+"\n")
    print(hash(data5)+":"+str(data5)+"\n")
    print(hash(data6)+":"+str(data6)+"\n")
