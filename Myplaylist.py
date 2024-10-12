class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        # self.current = None
class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cur= None
    def append(self,data):
        new_node = Node(data)
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
            self.cur = new_node
        else:
            temp = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.tail.prev = temp
    def add_begginig(self,data):
        new_node = Node(data)
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
            self.cur = new_node
            
        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp
        
    def previous(self):
        if self.cur.prev == None:
            print("None")
        else:
            temp = self.cur
            self.cur = temp.prev
            self.cur.next = temp
            print(self.cur.data)
    def forward(self):
        if self.cur.next == None:
            print("None")
        else:
            temp = self.cur
            self.cur = temp.next
            self.cur.prev = temp
    def current(self):
        print(self.cur.data)


    def show(self):
        if self.head == None and self.tail == None:
            print("Empty")
        else:
            crr = self.head
            while crr:
                print(crr.data)
                crr = crr.next
            print("None")

    def remove(self):
        if self.head == None or self.cur.prev == None:
            print("Empty List")
        else:
            temp = self.cur.prev
            temp.next = self.cur.next
            self.cur = temp
    def main(self):
        print("---MyPlayList---")
        rep = True
        while rep:
            print("1. Myplaylist")
            print("2. ADD Song at End of Playlist")
            print("3. Add song at Beggining of Playlist")
            print("4. My Current Song")
            print("5. Remove Current Song")
            print("6. Previous Song")
            print("7. Next Song")
            print("8. Exit From Playlist")
            ch = input("enter your choice:  ")
    
            if ch == '1':
                self.show()
            elif ch == '2':
                data = input("enter the Song Name: ")
                self.append(data)
                print("Song is added succesfully")
            elif ch== '3':
                data = input("enter the Song: ")
                self.add_begginig(data)
                print("Song is added succesfully")
            elif ch == '4':
                print("your current song is : ")
                self.current()
            elif ch == '5':
                self.remove()
                print("Current Song Is Remove From playlist")
            elif ch == '6':
                self.previous()
                print("Your previous Song Is ")
                self.current()
            elif ch == '7':
                self.forward()
                print("Your Next Song Is ")
                self.current()
            elif ch == '8':
                rep = False

            

st = linked_list()
st.main()
