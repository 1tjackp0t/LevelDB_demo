# coding=UTF-8
import plyvel


class DbClient:

    # 初始化&打开数据库
    def __init__(self, location):
        self._db = plyvel.DB(location, create_if_missing=True)
        print("open db's location:" + location)

    # 插入数据&修改
    # leveldb 存取的是二进制数据,所以参数得先确保转换成字符串类型,然后再转换成二进制数据
    # 若插入先相同key值则变为修改!
    def put(self, key, value):
        self._db.put(str(key).encode(), str(value).encode())
        print("input success!")

    # 根据key查value
    def get(self, key):
        # 此处返回的是bytes型数据
        return self._db.get(str(key).encode())

    # 查询
    def query_all(self):
        data_list = {}
        for key, value in self._db:
            data_list[key.decode()] = value.decode()
        return data_list

    def delete(self, key):
        self._db.delete(str(key).encode())

    # 关闭db
    def close(self):
        self._db.close()
        print("db closed!")

    # 析构,关闭数据库连接
    def __del__(self):
        self.close()


# # 初始化
# db = DbClient('/db')
# # 增加
# db.put('john', 'good boy')
# db.put('lisa', 'beautiful girl')
# # 查询
# print(db.get('john'))
# # 批量查询
# print(db.query_all())
# # 修改
# db.put('john', 'bad boy')
# print(db.query_all())
# # 删除
# db.delete('lisa')
# print(db.query_all())
