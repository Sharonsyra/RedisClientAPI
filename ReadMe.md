[![Build Status](https://travis-ci.org/Sharonsyra/RedisClientAPI.svg?branch=master)](https://travis-ci.org/Sharonsyra/RedisClientAPI)
[![Coverage Status](https://codecov.io/gh/Sharonsyra/RedisClientAPI/branch/master/graph/badge.svg)](https://codecov.io/gh/Sharonsyra/RedisClientAPI)

# RedisClientAPI

This is a  small MySQL database wrapper module that injects a mysql connection instance

## Getting Started
These instructions should help you run the code on your machine.

### Prerequisites
The code is written in Python3
- Python3 installed
- Redis installed

### Installing locally from github

start by cloning the repository from GitHub:

for https use
```
$ git clone https://github.com/Sharonsyra/RedisClientAPI.git
```

for ssh use 
```
git clone git@github.com:Sharonsyra/RedisClientAPI.git
```

Install the application's dependencies from `requirements.txt`
```
$ pip install -r requirements.txt
```

Start your Redis server - This is dependent on how you installed Redis. 

```
redis-server /usr/local/etc/redis.conf 
```

### Running the Redis Methods Client

In you Working folder Test with this commands 

- Import the container 

```
from containers import Configs, Readers, Clients
```

- Override your postgres credentials

```
Configs.config.override({
        "host": "HOST_NAME",
        "port": "PORT_NUMBER",
        "db": DB_VALUE
    })
```

- Make a variable for your redis methods

```
your_variable_name = Readers.redis_methods()
```

- Set Hash equivalent of redis' hset()

```
your_variable_name.set_hash('insert_hash_name', 'insert_key', 'insert_value)
```

- Get Hash equivalent of redis' hget()

```
your_variable_name.get_hash('insert_hash_name', 'insert_key')
```

- Get All Hash equivalent of redis' hgetall()

```
your_variable_name.get_hash_dict('insert_hash_name', 'insert_key')
```

- Hash Check equivalent of redis' hexists()

```
your_variable_name.hash_check('insert_hash_name', 'insert_key')
```

- Delete Hash equivalent of redis' hdel()

```
your_variable_name.delete_hash('insert_hash_name', 'insert_key')
```

### Running your API

Test this on postman or using curl

Run your flask server 

``` 
python main.py
```

**Redis Methods API**

----
<p>This API uses A Redis Methods Client. The methods contained are namely: hget(), hset(), hgetall(), hexists() and hdel()
</p>


**Get Hash**
----
  Returns a hash.

* **URL**
    `/api/v1.0/methods/<hash_name>/<key>`

* **Method:**

    `GET`

*  **URL Params**

    **Required:**

    `hash_name=[string]`
    `key=[string]`

* **Data Params**

    **Required:**

    None

* **Header Params**

    **Required:**

    None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{"Hash": "b'bar'"}`

* **Failure Response:**

  * **Code:** 200 <br />

  * **Content:** `{"Hash": "No matching value!"}`

----

**Set Hash**
----
  Sets a hash to a key.

* **URL**

    `/api/v1.0/methods/<hash_name>/<key>`

* **Method:**

    `POST`

*  **URL Params**

    **Required:**

    `hash_name=[string]`
    `key=[string]`

* **Data Params**

    **Required:**

    None

* **Header Params**

    **Required:**

    None


* **Success Response:**

  * **Code:** 201 <br />
    **Content:** `{"Created": 1}`

* **Failure Response:**

  * **Code:** 200 <br />

  * **Content:** `{"Already Exists!": 0}`

----

**Get All Hash**
----
  Return the key value pair attached to the hash.

* **URL**

    `/api/v1.0/methods/check/<hash_name>/<key>`

* **Method:**

    `GET`

*  **URL Params**

    **Required:**

    `hash_name=[string]`
    `key=[string]`

* **Data Params**

    **Required:**

    None

* **Header Params**

    **Required:**

    None


* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{"Exists?": true}`

* **Failure Response:**

  * **Code:** 200 <br />

  * **Content:** `{"Exists?": false}`

----

**Hash Check**
----
  Check If Hash Exists.

* **URL**

    `/api/v1.0/methods/check/<hash_name>`

* **Method:**

    `GET`

*  **URL Params**

    **Required:**

    `hash_name=[string]`

* **Data Params**

    **Required:**

    None

* **Header Params**

    **Required:**

    None


* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{"Hash Dict: ": { "b'foo'": "b'bar'"}}`

* **Failure Response:**

  * **Code:** 200 <br />

  * **Content:** `{"Hash Dict: ": "No matching hash!"}`

----

**Delete Hash**
----
  Deletes the hash.

* **URL**

    `/api/v1.0/methods/<hash_name>/<key>`

* **Method:**

    `DELETE`

*  **URL Params**

    **Required:**

    `hash_name=[string]`
    `key=[string]`

* **Data Params**

    **Required:**

    None

* **Header Params**

    **Required:**

    None


* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{"Hash Deleted": 1}`

* **Failure Response:**

  * **Code:** 200 <br />

  * **Content:** `{"Hash does not exist": 0}`


### Run your tests:
```
$ pytest -v(optional for verbosity)
```

## Resources Used
- Using Redis in Python - [Python Redis](https://redis-py.readthedocs.io/en/latest/)
- Redis Documentation - [Docs](https://redis.io/documentation)

