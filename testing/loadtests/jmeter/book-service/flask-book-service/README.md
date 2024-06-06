# Example: Book Service

In this example, we can see how simple a RESTful service can be implemented with
**Flask**.

## Start the Service

We start the web service from the command line:
```
$ python3 book_service.py

```
## Multi-Threading

When we run a Flask application using the `app.run()` method, we can pass
various configuration options to control the behavior of the development
server. One of these options is **threaded**.

Setting `threaded=True` instructs Flask's built-in development server
(powered by Werkzeug) to handle each incoming HTTP request in a separate
thread. This allows the server to process multiple requests concurrently,
rather than sequentially.

In recent versions of Flask, **threading is enabled by default**. This
means that even if you do not explicitly set `threaded=True`, the server
will still run in multi-threaded mode.

When using threading, it is important to ensure that our application
**code is thread-safe**. This means that shared resources (such as global
variables or database connections) must be properly managed to avoid race
conditions and other concurrency issues.


## Access the REST Service

### Find all Books
```
$ curl -i http://localhost:8080/books

HTTP/1.1 200 OK
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 15 May 2024 15:38:27 GMT
Content-Type: application/json
Content-Length: 401
Connection: close

{
  "data": [
    {
      "author": "Eric Matthes",
      "id": 1,
      "isbn": "978-1718502703",
      "title": "Python Crash Course"
    },
    {
      "author": "Brett Slatkin",
      "id": 2,
      "isbn": "978-0134853987",
      "title": "Effective Python"
    },
    {
      "author": "Luciano Ramalho",
      "id": 3,
      "isbn": "978-1492056355",
      "title": "Fluent Python"
    }
  ]
}
```

### Find a particular Book
```
$ curl -i http://localhost:8080/books/1

HTTP/1.1 200 OK
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 15 May 2024 15:40:51 GMT
Content-Type: application/json
Content-Length: 104
Connection: close

{
  "author": "Eric Matthes",
  "id": 1,
  "isbn": "978-1718502703",
  "title": "Python Crash Course"
}
```

### Insert a Book
```
$ curl -i -X POST http://localhost:8080/books -H "Content-Type: application/json" -d '{"id":7, "author":"Wes McKinney ", "title":"Python for Data Analysis", "isbn":"978-1098104030"}'

HTTP/1.1 201 CREATED
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 15 May 2024 15:41:44 GMT
Content-Type: application/json
Content-Length: 110
Connection: close

{
  "author": "Wes McKinney ",
  "id": 7,
  "isbn": "978-1098104030",
  "title": "Python for Data Analysis"
}
```

### Update a Book
```
$ curl -i -X PUT http://localhost:8080/books/2 -H "Content-Type: application/json" -d '{"author":"Brett Slatkin","title":"Effective Python", "isbn":"0134853989"}'

HTTP/1.1 200 OK
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 15 May 2024 15:42:31 GMT
Content-Type: application/json
Content-Length: 98
Connection: close

{
  "author": "Brett Slatkin",
  "id": 2,
  "isbn": "0134853989",
  "title": "Effective Python"
}
```

### Delete a Book

```
$ curl -i -X DELETE http://localhost:8080/books/1

HTTP/1.1 204 NO CONTENT
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 15 May 2024 15:43:12 GMT
Content-Type: text/html; charset=utf-8
Connection: close
```

*Egon Teiniker, 2020-2024, GPL v3.0*
