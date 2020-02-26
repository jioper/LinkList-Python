class Student:
    def __init__(self,SchNum,name,score):
        self.SchNum = SchNum
        self.name = name
        self.score = score
        self.next = None

class Link:

    def __init__(self):
        self.head = Student(None,None,None)
        self.tail = self.head
        self.size = 1

    def add(self,SchNum,name,score):
        stu = Student(SchNum,name,score)
        self.tail.next = stu
        self.tail = stu
        self.size = self.size + 1



    def insert(self,SchNum,name,score,index):
        if(index > self.size):
            print('长度超限')
        else:
            stu = self.head
            insert_stu = Student(SchNum,name,score)
            for i in range(index - 1):
                stu = stu.next
            insert_stu.next = stu.next
            stu.next = insert_stu
            self.size = self.size + 1



    def delete(self,index):
        if (index > self.size):
            print('长度超限')
        else:
            stu = self.head
            for i in range(index - 1):
                stu = stu.next
            temp = stu.next
            stu.next = temp.next
            self.size = self.size - 1



    def change(self,SchNum,name,score,index):
        if (index > self.size):
            print('长度超限')
        else:
            stu = self.head
            for i in range(index):
                stu = stu.next
            stu.SchNum =SchNum
            stu.name = name
            stu.score =score



    def getData(self,index):
        if(index > self.size):
            print('长度超限')
        else:
            stu = self.head
            for i in range(index):
                stu = stu.next
            return [stu.SchNum,stu.name,stu.score]


    def getSize(self):
        return self.size

    def jiudi_invert(self,head):
        dummy = Student(None,None,None)
        dummy.next = head
        prev = dummy.next
        pcur = prev.next

        while(pcur != None):
            prev.next = pcur.next
            pcur.next = dummy.next
            dummy.next = pcur
            pcur = prev.next

        self.head = dummy.next


    def new_invert(self,head):
        dummy = self.head
        pcur = head.next
        count = 0
        while(count < self.size - 1):
            prev = pcur.next
            pcur.next = dummy
            dummy = pcur
            pcur = prev
            count = count + 1

        self.head = dummy






def main():
    link = Link()

    newlink = Link()
    for i in range(5):
        newlink.add(i,'新链表！！！',i)

    print('添加节点 => 1 , 插入节点 => 2 , 删除节点 => 3 , 改变节点数据 => 4 , 遍历链表 => 5 , 获取链表长度 => 6')
    print('反转链表(就地反转） => 7 ,   反转链表 => 9 , 退出 => 0')
    select = -1

    while select != 0:
        select = int(input('请选择：'))

        if(select == 1):
            print('请输入相应数据')
            SchNum = int(input('学号：'))
            name = input('姓名：')
            score = input('成绩：')
            link.add(SchNum,name,score)
        elif(select == 2):
            print('请输入相应数据')
            SchNum = int(input('学号：'))
            name = input('姓名：')
            score = input('成绩：')
            index = int(input('要插入的位置（整数）：'))
            link.insert(SchNum,name,score,index)
        elif(select == 3):
            index = int(input('要删除节点的索引：'))
            link.delete(index)
        elif(select == 4):
            print('请输入相应数据')
            SchNum = int(input('学号：'))
            name = input('姓名：')
            score = input('成绩：')
            index = int(input('要改变的位置（整数）：'))
            link.change(SchNum,name,score,index)
        elif(select == 5):
            print('学号------姓名--------成绩')
            for i in range(link.size):
                data = link.getData(i)
                print(str(data[0]) + '   ' + str(data[1]) + '   ' + str(data[2]))
        elif(select == 6):
            print('链表的长度为：'+str(link.getSize()))
        elif(select == 7):
            link.jiudi_invert(link.head)
        elif(select == 8):
            link.connectLink(newlink)
        elif(select == 9):
            link.new_invert(link.head)


if __name__ == '__main__':
    main()
