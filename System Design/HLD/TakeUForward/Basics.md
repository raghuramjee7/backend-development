# Basics

## Scalability
The ability to handle more requests as they arrive is called scalability.  
**Horizontal Scaling** - Adding mutliple machines  
*Pros & Cons*
1. No single point of failure (resilient)
2. Network calls / Remote Procedure Calls (slow)
3. It requires load balancing
4. Data consistency is not available
5. Scales well  
**Vertical Scaling** - Converting to more powerful machine  
*Pros & Cons*
1. No load balancing
2. Inter process communication (fast)
3. It is a single point of failure
4. There is data consistency
5. Does not scale well (hardware limitation)

We take the best qualities of both and develop systems. The hybrid solution is vertical scaling and then horizontal scaling is considered.  

## Capacity Estimation & Numbers Everyone Should Know
Latency Comparison Numbers (~2012)
----------------------------------
L1 cache reference                           0.5 ns
Branch mispredict                            5   ns
L2 cache reference                           7   ns                      14x L1 cache
Mutex lock/unlock                           25   ns
Main memory reference                      100   ns                      20x L2 cache, 200x L1 cache
Compress 1K bytes with Zippy             3,000   ns        3 us
Send 1K bytes over 1 Gbps network       10,000   ns       10 us
Read 4K randomly from SSD*             150,000   ns      150 us          ~1GB/sec SSD
Read 1 MB sequentially from memory     250,000   ns      250 us
Round trip within same datacenter      500,000   ns      500 us
Read 1 MB sequentially from SSD*     1,000,000   ns    1,000 us    1 ms  ~1GB/sec SSD, 4X memory
Disk seek                           10,000,000   ns   10,000 us   10 ms  20x datacenter roundtrip
Read 1 MB sequentially from disk    20,000,000   ns   20,000 us   20 ms  80x memory, 20X SSD
Send packet CA->Netherlands->CA    150,000,000   ns  150,000 us  150 ms

Notes
-----
1 ns = 10^-9 seconds
1 us = 10^-6 seconds = 1,000 ns
1 ms = 10^-3 seconds = 1,000 us = 1,000,000 ns

Credit
------
By Jeff Dean:               http://research.google.com/people/jeff/  
Originally by Peter Norvig: http://norvig.com/21-days.html#answers  

## CDN
CDN stands for content delivery network. It is a distributed caching network that provides hosting and serving static files.  

