# Web Log Analysis Using MapReduce

Thus project was created as an assignment for “Intro to Hadoop and MapReduce” class (https://www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617).

I had the data set which was an anonymized Web server log file from a public relations company whose clients were DVD distributors. My goal was to write my Mappers and Reducers from scratch using Python and to answer to some questions about this dataset. I did the data processing on my your pseudo-distributed cluster (I used a virtual machine).


Each line of the dataset file represents a hit to the Web server. It includes the IP address which accessed the site, the date and time of the access, and the name of the page which was visited.

The logfile is in Common Log Format:

10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469

%h %l %u %t \"%r\" %>s %b

Where:

%h is the IP address of the client

%l is identity of the client, or "-" if it's unavailable

%u is username of the client, or "-" if it's unavailable

%t is the time that the server finished processing the request. The format is [day/month/year:hour:minute:second zone]

%r is the request line from the client is given (in double quotes). It contains the method, path, query-string, and protocol or the request.

%>s is the status code that the server sends back to the client. You will see see mostly status codes 200 (OK - The request has succeeded), 304 (Not Modified) and 404 (Not Found). See more information on status codes in W3C.org

%b is the size of the object returned to the client, in bytes. It will be "-" in case of status code 304.

Since the dataset was to large for github (481MB), I created a test_access_log file which include the first 50 lines of the original datasets.

##Question 1: 
how many hits were made to the page /assets/js/the-associates.js ?
To answer this question I wrote my_mapper_by_page.py and my_reducer.py. After running them on Hadoop, in part-00000 file I have the the number of hits for each different file on the Web site. For example:
……..
/assets/js/the-associates.js
	2456
……..

##Question 2: 
how many hits were made by the IP address 10.99.99.186 ?
To answer this question I wrote my_mapper_by_ip.py and I used my_reducer.py. After running them on Hadoop, in part-00000 file I have the the number of hits made by each different IP address. For example:
……..
10.99.99.186
	6
……..




##Question 3: 
what is the most popular file on the website (the file whose path occurs most often in access_log)? The number of occurrences? 
Since some passes in the log begin with “http://www.the-associates.co.uk”,  I removed this part using regular expression in m my_mapper_by_page2.py and I wrote my_reducer2.py which output only the most popular path and the number of occurrences of this path. 

I got:
 /assets/css/combined.css
	117352

I got the right answer to all questions! 
