# For this file, simulated (arbitrary) numbers of api calls to deal with.
# The api call response time varies from 10 to 15 seconds.
# The calls are to made concurrently.
# Predefined array containing 0s and 1s that quantity is not fixed.
# Search the first one in array -> make an api call -> replace 1 with 0 -> loop
# until all entries are 0.

# And more importantly, The (n+1)th call must start after nth call has started.
