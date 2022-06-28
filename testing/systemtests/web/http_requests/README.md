# HTTP Requests

HTTP is a set of protocols designed to enable communication between clients and servers. It works as a **request-response protocol** between a **client and server**.
A web browser may be the client, and an application on a computer that hosts a website may be the server.

## Setup

The simplest library to send HTTP requests is called **Requests**.
To download and install Requests library, use following command:
```
$ pip3 install requests
```

## Requests Library

Requests allows us to send HTTP/1.1 requests extremely easily. 
There’s no need to manually add query strings to your URLs, or to form-encode 
our POST data. Keep-alive and HTTP connection pooling are 100% automatic, 
thanks to urllib3.

_Example_: HTTP GET request 
```Python
    def test_get_request(self):
        # Setup
        url = 'http://localhost:8080/'    
        # Exercise
        req = requests.get(url = url)
        # Verify
        response = req.text
        print(f"Response: {response}")
        #Teardown
```

_Example_: HTTP POST request 
```Python
   def test_post_request(self):
        # Setup
        url = 'http://localhost:8080/translator'    
        data = {'word':'cat',
                'language':'Deutsch',
                'action': 'Translate'}
        # Exercise
        req = requests.post(url = url, data = data)
        # Verify
        response = req.text
        print(f"Response: {response}")
        self.assertTrue('Translate: cat into Katze' in response)
        # Teardown
```

## References
* [Requests: HTTP for Humans](https://requests.readthedocs.io/en/latest/)
* [GET and POST requests using Python](https://www.geeksforgeeks.org/get-post-requests-using-python/)

*Egon Teiniker, 2020-2022, GPL v3.0*