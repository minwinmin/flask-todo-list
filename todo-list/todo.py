# #下記はtodoリスト
# class ToDoitem:
#     item_id=0

#     #メソッドの中でも、インスタンスが生成されるときに自動的に呼び出されるメソッドのことをコンストラクタ
#     #コンストラクタを定義するには「init」という名前のメソッドを作成
#     def __init__(self, title):
#         self.title = title
#         self.done = False
#         self.item_id = ToDoitem.item_id
#         ToDoitem.item_id += 1

# class ToDoList:
#     def __init__(self):
#         self.todolist = []

#     def add(self, title):
#         item = ToDoitem(title)
#         self.todolist.append(item)
    
#     # def delete(self, item_id):
#     #     item = [x for x in self.todolist if x.item_id == item_id]
#     #     del item[0]
#     #     #pass文は「何もしない文」
#     #     pass

#     def delete(self, item_id):
#         item = [x for x in self.todolist if x.item_id != item_id]
    
#     def update(self, item_id):
#         #リスト内包表記
#         item = [x for x in self.todolist if x.item_id == item_id]
#         item[0].done = not item[0].done
    
#     def get_all(self):
#         return self.todolist
    
#     def delete_doneitem(self):
#         self.todolist = [x for x in self.todolist if not x.done]

class ToDoItem:
  item_id = 0

  def __init__(self, title):
    self.title = title
    self.done = False
    self.item_id = ToDoItem.item_id
    ToDoItem.item_id += 1

class ToDoList:
  def __init__(self):
    self.todolist = []

  def add(self, title):
    item = ToDoItem(title)
    self.todolist.append(item)

  def delete(self, item_id):
    #item = [x for x in self.todolist if x.item_id == item_id]
    self.todolist = [x for x in self.todolist if x.item_id != item_id]
    # delとpassの行は削除する
    

  def update(self, item_id):
    item = [x for x in self.todolist if x.item_id == item_id]
    item[0].done = not item[0].done

  def get_all(self):
    return self.todolist

  def delete_doneitem(self):
    self.todolist = [x for x in self.todolist if not x.done]