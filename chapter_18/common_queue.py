from collections import deque

stack = deque(('Kotlin', 'Python'))

# 元素入栈

stack.append("java")

print(stack)

stack.append("c++")

print(stack)

# 出栈

stack.pop()

print(stack)

stack.pop()

print(stack)

print(len(stack))
stack.pop()
print(len(stack))

# 作为堆来是使用 先进先出  一端插入，另外一端删除


stack = deque(('Kotlin', 'Python'))

stack.append("java")

stack.append("c++")
stack.append("c")

print(stack)

stack.popleft()

print(stack)

stack.popleft()

print(stack)

