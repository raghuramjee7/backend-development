# Splitwise Simplify

1. The main goal is to reduce the number of transactions between people.
2. We construct a graph of incoming and outgoing edges and each edge weight is the amount of money to be transferred.
3. For each node, we calculate the net amount of money to be transferred (incoming - outgoing).
4. Now the edges will be neuralised and each node has a net amount to be transferred (+ for recieving or - for sending).
5. Omit nodes with net 0.
6. Sum of sending and recieving should be 0 total.
7. Now we do a DFS to calculate the minimum number of transactions and who should pay whom.
8. We start from the node with the maximum net amount to be transferred.
