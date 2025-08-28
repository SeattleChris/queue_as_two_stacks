# queue_as_two_stacks

In this challenge, you must first implement a queue using two stacks. Then process `q` queries, where each query is one of the following  types:

1) 1 x: Enqueue element  into the end of the queue.
2) 2: Dequeue the element at the front of the queue.
3) 3: Print the element at the front of the queue.

## Input Format

The first line contains a single integer, `q` , denoting the number of queries.
Each line `i` of the `q` subsequent lines contains a single query in the form described in the problem statement above. All three queries start with an integer denoting the query `operation`, but only query `1` is followed by an additional space-separated value, `x`, denoting the value to be enqueued.

## Constraints

* 1 <= `q` <= 10^5
* 1 <= `operation` <= 3
* 1 <= `|x|` <= 10^9
* It is guaranteed that a valid answer always exists for each query with operation `3`.

## Output Format

For each query operation `3`, print the value of the element at the front of the queue on a new line.

## Note

No starter code, including `__main__` was provided for this problem.
