class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None

class Stack:
    def __init__(self):
        self.head = Node(None)
        self.len = 0

    def push(self, value):
        node = Node(value)

        self.len += 1
        if not self.head:
            self.head = node
            return
        else:
            node.prev = self.head
            self.head = node

    def pop(self):
        self.len = self.len-1 if self.len-1 > 0 else 0
        head = self.head if self.head else None
        if self.len == 0:
            self.head = Node(None)
        else:
            self.head = head.prev
        return head.value
    
    def peek(self):
        return self.head.value or None

    def size(self):
        return self.len

run_cases = [
    ("push", "Fire arrow", "Fire arrow", None),
    ("push", "Lightning arrow", "Lightning arrow", None),
    ("peek", None, "Lightning arrow", "Lightning arrow"),
    ("size", None, "Lightning arrow", 2),
    ("pop", None, "Fire arrow", "Lightning arrow"),
]

submit_cases = run_cases + [
    ("push", "Ice arrow", "Ice arrow", None),
    ("peek", None, "Ice arrow", "Ice arrow"),
    ("size", None, "Ice arrow", 2),
    ("pop", None, "Fire arrow", "Ice arrow"),
    ("pop", None, None, "Fire arrow"),
    ("pop", None, None, None),
    ("peek", None, None, None),
    ("size", None, None, 0),
]


def test(stack, method, input, expected_state, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * Stack: {stack.head.value}")
    print(f" * Method: {method}")
    print(f" * Item (only for push): {input}")
    print(f"Expected Return: {expected_output}")
    print(f"Expected Stack: {expected_state}")
    stack_method = getattr(stack, method)
    if input:
        result = stack_method(input)
    else:
        result = stack_method()
    print(f"Actual Return: {result}")
    print(f"Actual Stack: {stack.head.value}")
    if result == expected_output and stack.head.value == expected_state:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    stack = Stack()
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(stack, *test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
