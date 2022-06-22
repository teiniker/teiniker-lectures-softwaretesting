Given the following web application:

$ java -jar translator.jar

URL: http://localhost:8080/index.html

Test Cases:
>  word = 'cat', language = 'Deutsch' => 'Translate: cat into Katze'
>  word = 'horse', language = 'Francais' => 'Translate: horse into Cheval' 
>  word = 'dog', language = 'Deutsch' => 'Translate: dog into unknown'
>  word = 'dog', language = 'Francais' => 'Translate: dog into unknown'

## Using cURL 
$ curl -i -X POST -d 'word=cat&language=Deutsch&action=Translate' http://localhost:8080/translator
HTTP/1.1 200 
Content-Type: text/html;charset=UTF-8
Content-Language: en-US
Transfer-Encoding: chunked
Date: Tue, 21 Jun 2022 19:14:25 GMT

<!DOCTYPE HTML>
<html>
<head>
    <title>Translation Application</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>
    <h2>
        <p >Translate: cat into Katze</p>
    </h2>
    <p/>
    <a href="index.html"> back</a>
</body>
</html>
