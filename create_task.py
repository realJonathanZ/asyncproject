# For this file, simulated (arbitrary) numbers of api calls to deal with.
# The api call response time varies from 10 to 15 seconds.
# The calls are to made concurrently.
# Predefined array containing 0s and 1s that quantity is not fixed.
# Search the first one in array -> make an api call -> replace 1 with 0 -> loop
# until all entries are 0.

# And more importantly, The (n+1)th call must start after nth call has started.
# Therefore, cannot use asyncio.gather() this way






##
# A -> 4s, B -> 4s, total -> 4.0118 s
# A -> 10s, B -> 14s, total -> 14.0162 s
# B -> 12s, A -> 21s, total -> 21.0092 s

# executing a lot of sleep-tasks together -> 21.0124 s