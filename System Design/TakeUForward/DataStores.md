# Bloom Filters

Bloom Filters is a probabilistic data structure. It is used to check for string searches. This gives a surity if a string has been not searched, but not if a string has been searched.  

**1 Hit Wonder** - It is a search result that is searched only once. We might need to add this to cache but we need to be sure that occupying cache space is worth for this, ie - we will need to get this again, so we dont immediately push it to cache for the risk of losing something important.  

Bloom Filter is a bit array of length M. For a given string, lets hash it with K has functions to a each index (0->M-1). For each string search, make all the indices 1 for that string. Now, whenever we look for a string, if all its indices are 1s, then that string has been previously searched (probably). If there is atleast one 0, then it has not been searched (definitely). We can also have mutliple bloom filters, in a sort of multi level way, each time the ith bloom filter has all 1s, we go to i+1th bloom filter and make it all 1s. This way we will get the frequency of number of searches of a string. After getting confidences, we will cache that string.   

Since this is probablistic, some hash fucntions may map two character to a single index, there, even we if did not search, we might get a result that we have already searched.  Increasing the number of hash fucntions reduces it.
```
K = M(Log2)/N
```

# Data Replication
We need to always replicate data to avoid a single point of failure. We can replicate in two ways - synchronously & asynchronously. Synchronously - master sends a signal to slave db everytime there is a command, and the slave also executes this command. In async, only once the data is pulled.  
If we have writes in slave, this need to be propagated to master, at this point the network becomes master-master or peer to peer network. Any node that gets write operations is the master node. 

## Split Brain Problem
Let us say we have two servers A,B. Instead of the node failing, what happens if the network between them fails? Each will assume they are the master, and transactions consistency will fail. This can be solved by using another node.  
Lets say we have three nodes - A,B,C and the network between A and B has failed. Now, initially, all the nodes are in state S0. A gets a write and moves to state S1. It informs B, but fails since network has failed. It informs C and C moves its state from S0->S1, in sync with A. Now B gets a transaction and goes from S0 to S2. It signals C, but C asks what was its previous state, since the previous state needs to S1. Here B will rollback, update the state from S0->S1. The transaction for state S2 fails.  

## Distributed Consensus
The way in which multiple nodes come to a single conclusion. This is done by many procotols - 
1. 2 Phase Commit
2. 3 Phase Commit
3. Multi version concurrency control (used by postgres)
4. SAGA - Used for really long transactions


# Scaling DB Writes
1. To scale up, we need to avoid unnecessary headers, reduce IO calls.
2. We can use logs (which is a ds on top of LL). Here, the insertions are pretty fast - O(1), but the reads are very slow since we need to go sequentially.
3. After the data is commited, we can go ahead and convert it into a sorted list in the DB. We can merge mutliple sorted lists, to improve reads, but we only merge when it is advantageous , ie merging is better than reading (too many sorted lists to search through). This is called a STT (sorted string table)
4. We can use bloom filters on top of it to optimise query performance. 

# Location Based Databases

1. Databases that are used for location based operations is called location based databases.
2. We have some requirements for those - measurable distance, ie we need to be able to get the distance between two points (this also needs to be uniform and granular). We also need proximity, ie we need to be able to find out which points are nearby.
3. We can store locations with coordinates. 
4. We can use quad trees to group locations, word -> india, china, europe -> mumbai, delhi, cc, chennai -> ... This way we will iterate through the tree to find location.
5. 	

