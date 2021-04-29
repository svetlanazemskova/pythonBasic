# Node Implementation
class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_prev_node(self):
        return self.prev_node

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

# Test Node
my_node = Node(99)
my_node_str = Node("Hallo Welt!")
print("My Node Values are: " + str(my_node.get_value()) +" " + str(my_node_str.get_value()) +"\n")


# Linked List Implementation
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    # get the head node
    def get_head_node(self):
        return self.head_node

    # insert a new head node
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

# Test Linked List
print("Let's test Linked List: ")
ll = LinkedList(89)
ll.insert_beginning(67)
ll.insert_beginning(45)
ll.insert_beginning(123)
print(ll.stringify_list())

# Doubly Linked List Implementation
class DoublyLinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None

  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node

    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)

    self.head_node = new_head

    if self.tail_node == None:
      self.tail_node = new_head

  def add_to_tail(self, new_value):
      new_tail = Node(new_value)
      current_tail = self.tail_node

      if current_tail != None:
          current_tail.set_next_node(new_tail)
          new_tail.set_prev_node(current_tail)

      self.tail_node = new_tail

      if self.head_node == None:
          self.head_node = new_tail

  def remove_head(self):
      removed_head = self.head_node

      if removed_head == None:
          return None

      self.head_node = removed_head.get_next_node()

      if self.head_node != None:
          self.head_node.set_prev_node(None)

      if removed_head == self.tail_node:
          self.remove_tail()

      return removed_head.get_value()

  def remove_tail(self):
      removed_tail = self.tail_node

      if removed_tail == None:
          return None

      self.tail_node = removed_tail.get_prev_node()

      if self.tail_node != None:
          self.tail_node.set_next_node(None)

      if removed_tail == self.head_node:
          self.remove_head()

      return removed_tail.get_value()

  def remove_by_value(self, value_to_remove):
      node_to_remove = None
      current_node = self.head_node

      while current_node != None:
          if current_node.get_value() == value_to_remove:
              node_to_remove = current_node
              break

          current_node = current_node.get_next_node()

      if node_to_remove == None:
          return None
      if node_to_remove == self.head_node:
          self.remove_head()
      elif node_to_remove == self.tail_node:
          self.remove_tail()
      else:
          next_node = node_to_remove.get_next_node()
          prev_node = node_to_remove.get_prev_node()
          next_node.set_prev_node(prev_node)
          prev_node.set_next_node(next_node)

      return node_to_remove

  def stringify_list(self):
      string_list = ""
      current_node = self.head_node
      while current_node:
          if current_node.get_value() != None:
              string_list += str(current_node.get_value()) + "\n"
          current_node = current_node.get_next_node()
      return string_list

# Test Doubly Linked List: Create your S1 here:
print("Test Doubly Linked List: S1 Sbahn Berlin: ")
subway = DoublyLinkedList()
subway.add_to_head("Zehlendorf")
subway.add_to_head("Mexikoplatz")
subway.add_to_head("Schlachtensee")
subway.add_to_tail("Sundgauer Strasse")
subway.add_to_tail("Lichterfelde West")
subway.add_to_tail("Botanische Garten")
subway.add_to_tail("Steglitz")
print(subway.stringify_list())
subway.remove_head()
subway.remove_tail()
print(subway.stringify_list())
subway.remove_by_value("Lichterfelde West")
print(subway.stringify_list())

print("Test Doubly Linked List: We are waiting for 100")
test_list = DoublyLinkedList()
test_list.add_to_head(9)
test_list.remove_tail()
test_list.add_to_tail(8)
test_list.add_to_tail(2)
test_list.remove_head()
test_list.add_to_tail(100)
test_list.remove_by_value(9)
test_list.remove_head()
print(test_list.head_node.get_value())
print("\n")

# Linear Search Implementation
def linear_search(search_list, target_value):
    for idx in range(len(search_list)):
        print(search_list[idx])
        if search_list[idx] == target_value:
            return idx
    raise ValueError("{0} not in list".format(target_value))


# Test Linear Search
print("Test linear search: We are waiting for finding 22, which index is 1")
values = [54, 22, 46, 99]
print(linear_search(values, 22))
#print(linear_search(values, 30))
print("\n")

# Finding duplicates
tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"

def linear_search_dup(search_list, target_value):
  matches = []
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      matches.append(idx)
  if matches:
    return matches
  else:
    raise ValueError("{0} not in list".format(target_value))

#Test finding duplicates
print("Test finding duplicates: We are waiting for indexes 0 and 5")
tour_stops = linear_search_dup(tour_locations, target_city)
print(tour_stops)
print("\n")

# Finding the Maximum Value
test_scores = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]

#Linear Search Algorithm for finding Max
def linear_search_max(search_list):
  maximum_score_index = None
  for idx in range(len(search_list)):
    if not maximum_score_index or search_list[idx] > search_list[maximum_score_index]:
      maximum_score_index = idx
  return maximum_score_index

# Test finding MAX
print("Test finding MAX: return index, we are waiting for 3")
highest_score = linear_search_max(test_scores)
print(highest_score)
print("\n")

# Binary Search Implementation
def binary_search(sorted_list, target):
  if not sorted_list:
    return 'value not found'
  mid_idx = len(sorted_list)//2
  mid_val = sorted_list[mid_idx]
  if mid_val == target:
    return mid_idx
  if mid_val > target:
    left_half = sorted_list[:mid_idx]
    return binary_search(left_half, target)
  if mid_val < target:
    right_half = sorted_list[mid_idx+1:]
    result = binary_search(right_half, target)
    if result == "value not found":
      return result
    else:
      return result + mid_idx + 1

# For testing:
print("Test Binary search: return index, we are waiting for 3")
sorted_values = [13, 14, 15, 16, 17]
print(binary_search(sorted_values, 16))
print("\n")

# Queue Implementation
class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            print("Adding " + str(item_to_add.get_value()) + " to the queue!")
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("Sorry, no more room!")

    def dequeue(self):
        if self.get_size() > 0:
            item_to_remove = self.head
            print(str(item_to_remove.get_value()) + " is served!")
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("The queue is totally empty!")

    def peek(self):
        if self.size > 0:
            return self.head.get_value()
        else:
            print("No orders waiting!")

    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.get_size()

    def is_empty(self):
        return self.size == 0


print("Creating a deli line with up to 10 orders...\n------------")

deli_line = Queue(10)
print("Adding orders to our deli line...\n------------")
deli_line.enqueue("egg and cheese on a roll")
deli_line.enqueue("bacon, egg, and cheese on a roll")
deli_line.enqueue("toasted sesame bagel with butter and jelly")
deli_line.enqueue("toasted roll with butter")
deli_line.enqueue("bacon, egg, and cheese on a plain bagel")
deli_line.enqueue("two fried eggs with home fries and ketchup")
deli_line.enqueue("egg and cheese on a roll with jalapeos")
deli_line.enqueue("plain bagel with plain cream cheese")
deli_line.enqueue("blueberry muffin toasted with butter")
deli_line.enqueue("bacon, egg, and cheese on a roll")
# ------------------------ #

deli_line.enqueue("western omelet with home fries")
# ------------------------ #
print("------------\nOur first order will be " + deli_line.peek())
print("------------\nNow serving...\n------------")
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
# ------------------------ #

deli_line.dequeue()
# ------------------------ #
print("\n")

# Stack Implementation
class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
            print("Adding {} to the pizza stack!".format(value))
        else:
            print("No room for {}!".format(value))

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            print("Delivering " + item_to_remove.get_value())
            return item_to_remove.get_value()
        print("All out of pizza.")

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        print("Nothing to see here!")

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0

    def print_items(self):
        pointer = self.top_item
        print_list = []
        while (pointer):
            print_list.append(pointer.get_value())
            pointer = pointer.get_next_node()
        print_list.reverse()
        print("{0} Stack: {1}".format(self.get_name(), print_list))


# Defining an empty pizza stack
pizza_stack = Stack(6)
# Adding pizzas as they are ready until we have
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")

pizza_stack.push("pizza #7")

# Delivering pizzas from the top of the stack down
print("The first pizza to deliver is " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

pizza_stack.pop()
print("\n")

# Hash Map
class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key, count_collisions=0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]

    if current_array_value is None:
      self.array[array_index] = [key, value]
      return

    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return

    # Collision!

    number_collisions = 1

    while(current_array_value[0] != key):
      new_hash_code = self.hash(key, number_collisions)
      new_array_index = self.compressor(new_hash_code)
      current_array_value = self.array[new_array_index]

      if current_array_value is None:
        self.array[new_array_index] = [key, value]
        return

      if current_array_value[0] == key:
        self.array[new_array_index] = [key, value]
        return

      number_collisions += 1

    return

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]

    if possible_return_value is None:
      return None

    if possible_return_value[0] == key:
      return possible_return_value[1]

    retrieval_collisions = 1

    while (possible_return_value != key):
      new_hash_code = self.hash(key, retrieval_collisions)
      retrieving_array_index = self.compressor(new_hash_code)
      possible_return_value = self.array[retrieving_array_index]

      if possible_return_value is None:
        return None

      if possible_return_value[0] == key:
        return possible_return_value[1]

      number_collisions += 1

    return
print("Test: assign and retrieve in our Hash Map")
hash_map = HashMap(15)
hash_map.assign('gabbro', 'igneous')
hash_map.assign('sandstone', 'sedimentary')
hash_map.assign('gneiss', 'metamorphic')
print(hash_map.retrieve('gabbro'))
print(hash_map.retrieve('sandstone'))
print(hash_map.retrieve('gneiss'))

# Tree Implementation
class TreeNode:
    def __init__(self, value):
        self.value = value  # data
        self.children = []  # references to other nodes

    def add_child(self, child_node):
        # creates parent-child relationship
        print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        # removes parent-child relationship
        print("Removing " + child_node.value + " from " + self.value)
        self.children = [child for child in self.children
                         if child is not child_node]

    def traverse(self):
        # moves through each node referenced from self downwards
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children