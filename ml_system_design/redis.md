Redis is a versatile in-memory data store that can be used for a wide range of use cases. Here are some examples of how to use Redis in various scenarios:

1. **Basic Key-Value Operations**:

   ```python
   import redis

   # Connect to a Redis server
   r = redis.StrictRedis(host='localhost', port=6379, db=0)

   # Set a key-value pair
   r.set('my_key', 'my_value')

   # Retrieve the value
   value = r.get('my_key')
   print(value.decode('utf-8'))  # Output: 'my_value'
   ```

2. **Using Lists**:

   ```python
   # Adding elements to a list
   r.rpush('my_list', 'item1')
   r.rpush('my_list', 'item2')
   r.rpush('my_list', 'item3')

   # Retrieving list elements
   items = r.lrange('my_list', 0, -1)
   for item in items:
       print(item.decode('utf-8'))

   # Output:
   # 'item1'
   # 'item2'
   # 'item3'
   ```

3. **Using Sets**:

   ```python
   # Adding elements to a set
   r.sadd('my_set', 'item1')
   r.sadd('my_set', 'item2')
   r.sadd('my_set', 'item3')

   # Checking if an element exists in the set
   exists = r.sismember('my_set', 'item2')
   print(exists)  # Output: True
   ```

4. **Using Hashes**:

   ```python
   # Storing user information in a hash
   user_data = {
       'username': 'john_doe',
       'email': 'john@example.com',
       'age': 30
   }
   r.hmset('user:1', user_data)

   # Retrieving specific fields from the hash
   username = r.hget('user:1', 'username')
   print(username.decode('utf-8'))  # Output: 'john_doe'
   ```

5. **Expire Keys**:

   ```python
   # Set a key with an expiration time (in seconds)
   r.setex('temporary_key', 3600, 'This key will expire in 1 hour')

   # Check the time to live (TTL) of a key
   ttl = r.ttl('temporary_key')
   print(ttl)  # Output: 3600 (seconds)
   ```

6. **Pub/Sub Messaging**:

   ```python
   import redis

   r = redis.StrictRedis(host='localhost', port=6379, db=0)

   # Publisher
   r.publish('channel', 'Message from the publisher')

   # Subscriber
   pubsub = r.pubsub()
   pubsub.subscribe('channel')
   for message in pubsub.listen():
       if message['type'] == 'message':
           print(message['data'].decode('utf-8'))
   ```

7. **Incrementing and Decrementing Values**:

   ```python
   # Incrementing a counter
   r.incr('counter')

   # Decrementing a counter
   r.decr('counter')

   # Retrieving the counter value
   counter_value = r.get('counter')
   print(counter_value.decode('utf-8'))
   ```

8. **Using Sorted Sets**:

   Sorted sets are ideal for leaderboard scenarios:

   ```python
   # Adding members to a sorted set with scores
   r.zadd('leaderboard', {'player1': 100, 'player2': 85, 'player3': 120})

   # Retrieving the top players
   top_players = r.zrevrange('leaderboard', 0, 2, withscores=True)
   for player, score in top_players:
       print(f'{player.decode("utf-8")}: {int(score)} points')
   ```

These are just a few examples of how Redis can be used in various scenarios. Redis provides a wide range of data structures and features, making it a powerful choice for caching, real-time analytics, and other data storage needs.
