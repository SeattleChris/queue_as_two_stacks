import os


def queue_operations(queries):
    """ Using two stacks, implement the three queue operations:
        1) `1 x`: Enqueue element `x` into the end of the queue.
        2) 2: Dequeue the element at the front of the queue.
        3) 3: Print the element at the front of the queue.
    """
    stack, result = [], []
    for (op, *vals) in queries:
        match op:
            case 1:  # Enqueue element
                stack.append(vals[-1])
            case 2:  # Dequeue front element
                temp = list(reversed(stack))
                temp.pop()
                stack = list(reversed(temp))
            case 3: # add front element to result list
                result.append(stack[0])
            case _:
                raise ValueError("Not a valid operation.")
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    queries_rows = int(input().strip())
    queries = []
    for _ in range(queries_rows):
        queries.append(list(map(int, input().rstrip().split())))
    result = queue_operations(queries)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
