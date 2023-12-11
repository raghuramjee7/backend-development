# Load Balancing

The concept of taking N servers and balacing the load evenly on all of them is called load balancing.  

Lets say we get a random request ID from the user. Let is be 0 -> M-1. Take this request ID and hash it, take the remainder with N (servers), and whatever remainder we got, send it to that server.
```
r1 = request_id    
h1 = hash(r1)  
server = h1%N  
```
If there are X requests, each server has X/N load and the load factor is X/N.   

But whenever we add a new server, the whole route of requests need to change, since servers usually store some user data, all that needs to be re-routed. This is very expensive. Also, in real life, the request IDs are rarely random. 

# Consistent Hashing

Consistent hashing deals with the issue of adding and removing servers.  
Earlier, we mapped a bunch of requests to a server, because we used linear search space (request hashes), and simple modulo.  
Here, we can have a circular search space from 0 -> M-1. Now, we also hash the servers, and take the modulo with M. Lets say a server s1 is mapped and hashed to point 1, another server to point 10 another to 20. Everytime we get a request to somewhere between 0 to M-1, we map it to the rightmost server point. We could also have multiple hash functions so that server 1 points to places 1, 15, 20, so that when one server goes, the circularity is not much effected.  


# Sharding
**Horizontal Partitioning** - We use one key to partition a bunch of data among different servers.  
**Vertical Partitioning** - We parition the data based on the columns.  
Sharding is a part of horizontal paritioning. Here we split the data based on a shard key. This is critical in choosing how to shard data.  
Problems of sharding is joins and fixed number of shards
In DBMS, consistency triumphs over availability. 
