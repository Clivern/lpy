# 056. Lists as stacks
#
# append and pop() make a stack: last in, first out. For a queue, collections.deque is
# O(1) at both ends; pop(0) on a list is O(n).
#
# Run: python 056_list_as_stack/main.py

stack = []
stack.append("a")
stack.append("b")
print(stack.pop(), stack.pop(), stack)
