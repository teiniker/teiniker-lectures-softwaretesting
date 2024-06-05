# Apache JMeter

Apache JMeter may be used to test performance both on static and dynamic resources,
Web dynamic applications.
It can be used to simulate a heavy load on a server, group of servers, network or
object to test its strength or to analyze overall performance under different load types.

**JMeter is not a browser, it works at protocol level****.
As far as web-services and remote services are concerned, JMeter looks like a browser
(or multiple browsers).
JMeter does not perform all the actions supported by browsers. In particular,
JMeter does not execute the Javascript found in HTML pages. Nor does it render the HTML
pages as a browser does.


## Setup and Start JMeter

[Download}(https://jmeter.apache.org/download_jmeter.cgi): apache-jmeter-5.6.3.zip

```
$ unzip apache-jmeter-5.6.3.zip
$ mv apache-jmeter-5.6.3 ~/local/

$ cd apache-jmeter-5.6.3/
$ bin/jmeter.sh
```

## Performance Testing Using JMeter

The process of performance testing using JMeter includes:

1. **Test Plan Creation**: The first step is to create a test plan that
    outlines the testing scenarios. This includes adding thread groups
    (representing users), samplers (requests), and other elements like
    listeners, timers, and assertions.

2. **Thread Groups**: Define the number of virtual users (threads), the
    ramp-up period, and the loop count. This simulates the load on the
    application.

3. **Samplers**: Add samplers to the test plan to simulate different types
    of requests, such as HTTP requests, database queries, or SOAP/REST API calls.

    * **Configuration Elements**: Configure elements like HTTP request defaults,
        CSV data set config (for parameterizing inputs), and user-defined variables
        to manage test data and settings.

4. **Timers and Controllers**: Use timers to simulate real user think times
    and controllers to manage the logic of the test execution, such as
    looping, branching, or conditional execution.

5. **Assertions**: Add assertions to validate the responses from the server,
    ensuring that the application behaves correctly under load.

6. **Listeners**: Add listeners to collect and visualize the test results.
    Common listeners include the **View Results Tree**, Summary Report,
    Aggregate Report, and **Graph Results**.

7. **Execution**: Execute the test plan, either from the GUI or in non-GUI
    mode for higher performance and scalability.

8. **Monitoring and Analysis**: Monitor the test execution in real-time and
    analyze the collected data to identify performance bottlenecks, errors,
    and other issues.

9. **Reporting**: Generate detailed reports that provide insights into
    the performance of the application, highlighting areas that need
    optimization.


_Example:_ Load Testing the Books REST service
```
TestPlan
	Name: Book Service Test Plan
	Add / Threads (Users) / Thread Group
		Name: Thread Group
		Number of threads (users): 10
		Add / Sampler / Http Request
			Protocol: http
			Server Name: localhost
			Port Number: 8080
			Http Request: GET
			Path: /books
		Add / Listener / View Results Tree
		Add / Listener / View Results Table
```


## References
* [Download Apache JMeter](https://jmeter.apache.org/download_jmeter.cgi)

* [YouTube (JMeter Tutorial For Beginners): Load Testing Using JMmeter](https://youtu.be/NTyY8wKSvik)

* Antonio Gomes Rodrigues, Bruno Demion, Philippe Mouawad. **Master Apache JMeter - From Load Testing to DevOps: Master performance testing with JMeter**. Packt Publishing, 2019.

*Egon Teiniker, 2020-2024, GPL v3.0*
