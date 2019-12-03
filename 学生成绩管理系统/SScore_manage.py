class Node(object):
    def __init__(self, data, pointer):
        self.data = data
        self.next = pointer


# 创建单链表
class SingleLinkedList(object):
    def __init__(self):
        self.head = Node(None, None)
        self.point = self.head

    def append(self, data):
        # 末尾追加节点
        new_node = Node(data, None)
        self.point.next = new_node
        self.point = new_node

    def insert(self, data, find):
        # 插入数据(前向插入数据)
        if not self.head.next:
            print('链表为空')
            return None
        new_node = Node(data, None)
        self.point = self.head
        while self.point.next.data != find:
            self.point = self.point.next
            if self.point.next is None:
                print('没有找到该元素')
                return None

        new_node.next = self.point.next
        self.point.next = new_node

    def delete(self, find):
        # 删除节点
        # 空链表
        if not self.head.next:
            print('链表为空')
            return None
        self.point = self.head
        while self.point.next.data != find:
            self.point = self.point.next
        pointer = self.point.next
        self.point.next = self.point.next.next
        del pointer

    def insert_after_head(self, data):

        node = Node(data, None)
        # bug 产生没写 if 返回
        if not self.head.next:
            self.head.next = node
            return None
        node.next = self.head.next
        self.head.next = node

    def reverse(self):
        local_list = SingleLinkedList()
        self.point = self.head
        count = 0
        while self.point.next:
            count += 1
            self.point = self.point.next
            data = self.point.data
            local_list.insert_after_head(data)
        return local_list

    def get_size(self):
        count = 0
        self.point = self.head
        while self.point.next:
            self.point = self.point.next
            count += 1
        return count

    def delete_by_tail(self, num):
        size = self.get_size()
        assert (num <= size)
        assert (num > 0)
        pos = size - num
        count = 0
        self.point = self.head
        while count < size:
            count += 1
            self.point = self.point.next
            if count == pos:
                pointer = self.point.next
                self.point.next = self.point.next.next
                del pointer

    # 求中间节点 只允许遍历一次
    def quick_middle(self):
        slow_point = self.head
        fast_point = self.head
        while fast_point.next.next:
            slow_point = slow_point.next
            fast_point = fast_point.next.next
            if not fast_point.next:
                break
        if fast_point.next:
            slow_point = slow_point.next
        return slow_point.data

    def check_circle(self):
        pass

    def sort(self):
        # get_size()改变了 self.point 的指向
        length = self.get_size()
        i, j = 0, 0
        flag = 1
        while i < length:
            self.point = self.head.next
            while j < length - i - 1:
                if self.point.data > self.point.next.data:
                    temp = self.point.data
                    self.point.data = self.point.next.data
                    self.point.next.data = temp
                self.point = self.point.next
                j += 1
                flag = 0
            if flag:
                break
            i += 1
            j = 0

    def print(self):
        # 打印结点
        self.point = self.head
        while self.point.next:
            self.point = self.point.next
            print('{} ->'.format(self.point.data), end=' ')
        print('')


class StudentControlSystem(SingleLinkedList):
    # 打印菜单
    def print_menu(self):
        print('*' * 30)
        print('-' * 13 + '菜单' + '-' * 13)
        print('1.增加学生信息')
        print('2.删除学生信息')
        print('3.修改学生信息')
        print('4.查找学生信息')
        print('5.显示所有信息')
        print('6.排序')
        print('0.退出程序')
        print('*' * 30)

    # 用户输入
    def user_input(self, item):
        try:
            item = int(item)
        except:
            pass
        # 增加信息
        if item == 1:
            self.add_info()
        # 删除信息
        elif item == 2:
            find = input('请输入删除的学号：')
            self.del_info(find=find)
        # 修改信息
        elif item == 3:
            self.modify_info()
        # 查找信息
        elif item == 4:
            self.search_info()
        # 显示信息
        elif item == 5:
            self.display_info()
        # 信息排序
        elif item == 6:
            self.rank_info()
        # 退出程序 保存数据
        elif item == 0:
            with open('database.txt', 'w') as f:
                self.point = self.head
                while self.point.next:
                    self.point = self.point.next
                    f.writelines('{}\n'.format(self.point.data))
            exit()
        else:
            print('请输入正确的数字')

    # id 保证互异性
    def unique_id(self, std_id):
        self.point = self.head
        while self.point.next:
            self.point = self.point.next
            if self.point.data['id'] == std_id:
                return False
        return True

    # 增加信息
    def add_info(self):
        # id 不能重复
        # 成绩不能超出范围
        name = input('姓名：')
        std_id = input('学生id：')
        while not self.unique_id(std_id=std_id):
            print('id重复')
            std_id = input('学生id：')
        grade = input('学生成绩：')
        if eval(grade) < 0 or eval(grade) > 100:
            print('超出范围')
            grade = input('学生成绩：')
        print(name, std_id, grade)
        print('请确认无误后保存')
        choice = input('y/n')
        items = ['y', 'yes', 'Y', 'Yes']
        if choice in items:
            print(choice)
            data = {'id': std_id, 'name': name, 'grade': grade}
            self.append(data)

    # 删除信息
    def del_info(self, find):
        print('请确认无误后保存')
        choice = input('y/n')
        items = ['y', 'yes', 'Y', 'Yes']
        if choice in items:
            if not self.head.next:
                print('链表为空')
                return None
            self.point = self.head
            while self.point.next.data['id'] != find:
                self.point = self.point.next
            pointer = self.point.next
            self.point.next = self.point.next.next
            del pointer

    # 序列逆序
    def reverse(self):
        local_list = StudentControlSystem()
        self.point = self.head
        count = 0
        while self.point.next:
            count += 1
            self.point = self.point.next
            data = self.point.data
            local_list.insert_after_head(data)
        return local_list

    # 序列排序
    def sort(self, item):
        length = self.get_size()
        i, j = 0, 0
        flag = 1
        while i < length:
            self.point = self.head.next
            while j < length - i - 1:
                if int(self.point.data[item]) > int(self.point.next.data[item]):
                    # self.point.data, self.point.next.data =
                    # self.point.next.data, self.point.data
                    temp = self.point.data
                    self.point.data = self.point.next.data
                    self.point.next.data = temp
                self.point = self.point.next
                j += 1
                flag = 0
            if flag:
                break
            i += 1
            j = 0

    # 修改信息
    def modify_info(self):
        find = input('输入需要修改的学生的id：')
        if not self.head.next:
            print('链表为空')
            return None
        self.point = self.head
        while str(self.point.next.data['id']) != find:
            self.point = self.point.next
            if self.point.next is None:
                print('没有找到该元素')
                return None
        name = input('姓名：')
        grade = input('学生成绩：')
        self.point.next.data['name'] = name
        self.point.next.data['grade'] = grade

    # 搜索信息
    def search_info(self):
        find = input('输入需要查找的学生的id：')
        if not self.head.next:
            print('链表为空')
            return None
        self.point = self.head
        while str(self.point.next.data['id']) != find:
            self.point = self.point.next
            if self.point.next is None:
                print('没有找到该元素')
                return None
        data = self.point.next.data
        print('ID 姓名 成绩')
        print('{}  {}  {}'.format(data['id'], data['name'], data['grade']))

    # 信息排序
    def rank_info(self):
        choice = input('1.成绩排序 2.学号排序：')
        order = input('1.升序 2.降序：')
        if choice == '1':
            item = 'grade'
        elif choice == '2':
            item = 'id'
        else:
            return None
        self.sort(item=item)
        if order == '2':
            temp = self.reverse()
            temp.display_info()
            return None
        self.display_info()

    # 显示信息
    def display_info(self):
        self.point = self.head
        print('ID 姓名 成绩')
        while self.point.next:
            self.point = self.point.next
            data = self.point.data
            print('{}  {}  {}'.format(data['id'], data['name'], data['grade']))
        print('')


def main():
    SCS = StudentControlSystem()
    try:
        with open('database.txt', 'r') as f:
            for data in f.readlines():
                SCS.append(eval(data))
    except:
        with open('database.txt', 'w') as f:
            pass

    while True:
        SCS.print_menu()
        item = input('请输入你的选择：')
        SCS.user_input(item)


if __name__ == "__main__":
    main()