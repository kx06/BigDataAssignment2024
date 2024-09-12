

## Task 1: Store Profit and Loss

### Story Background:

You are given data from a retail chain in India that sells a wide range of products, including groceries, home appliances, beauty items, apparel and many more goods in multiple cities across the country. However, not all stores in the chain sell every product category. Each store has its own top-selling categories based on consumer demand. Only these top-selling categories will determine the profit gained or the loss incurred by a store.

*Given the input, your task is to determine:*

1. The number of stores that are profitable for each city.
2. The number of stores operating at a loss for each city.

*Points to be Considered:*
1. Sales data (Revenue and COGS) for a product category (top-selling or not) may or may not be recorded.
2. Net results (Profit or Loss) for each store is only calculated if there exists Sales data (Revenue and COGS) for atleast some top-selling category.
3. If Net results > 0, it is a profitable store, otherwise it's incurring a loss.



#### Mapper and reducer
*Mapper*
Input : Array of JSON Objects
*Reducer*
Output : 
```
{"city": "Bangalore", "profit_stores": 2, "loss_stores": 0}
{"city": "Chennai", "profit_stores": 1, "loss_stores": 1}
{"city": "Mumbai", "profit_stores": 2, "loss_stores": 0}
```

### Instructions

1. Write a python mapper
        Name : mapper.py
        Read the specification for input and output as mentioned above
        Only packages that can be imported are : json and sys
		
2. Write a python reducer to perform the aggregation
        Name : reducer.py
        Read the specification for input and output as mentioned above
        Only packages that can be imported are : json and sys
		
3. Test it out with the sample dataset given and check the expected output


Testing instructions
Local testing

`cat <path_to_dataset>.json | ./mapper.py | sort -k 1,1 | ./reducer.py

Hadoop testing

```
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-<hadoop_version>.jar \
-mapper "$PWD/mapper.py" \
-reducer "$PWD/reducer.py" \
-input  <path_to_input_in_hdfs> \
-output <path_to_output_folder_in_hdfs>
```





## TASK 2: Load Balancer
### Story Background:

A Company's team was assigned to predict the status codes that clients would receieve while hitting the company's endpoints, while taking into consideration the traffic received on a certain endpoint at a given time, as well as the reliability of the servers handling the requests. You are given a dataset with the information regarding all the requests made by clients during the day. The predicted status codes by the team are also provided. You are to validate the dataset given and evaluate each client's success metric.
Metadata for the Dataset:

*Request ID (rX):*
A unique identifier for each request. This is used to differentiate between different requests in the dataset.

*Client ID (cX):*
Identifies the client making the request. Each client is associated with a unique ID, which can be used to track the activity or behavior of individual clients.


*Endpoint (endpoint):*
Represents the specific service or function the request is accessing.

user/profile:
Access or update user profile information. 
user/settings: 
Modify user settings, such as privacy or notification preferences. 
order/history: Retrieve the history of past orders. 
order/checkout: Complete the checkout process for an order. 
product/details: View detailed information about a specific product. 
product/search: Search for products based on certain criteria. 
cart/add: Add an item to the shopping cart. 
cart/remove: Remove an item from the shopping cart. 
payment/submit: Submit payment information to complete a purchase. 
support/ticket: Create or view support tickets for customer service.

Each endpoint is associated with a price, which is used to calculate the total_price for each client. The price for all the endpoints is given below.

```     'user/profile': 100
        'user/settings': 200
        'order/history': 300
        'order/checkout': 400
        'product/details': 500
        'product/search': 600
        'cart/add': 700
        'cart/remove': 800
        'payment/submit': 900
        'support/ticket': 1000
```


*Timestamp (HH:MM:SS):*
Indicates the time at which the request was made in hours, minutes, and seconds. This can be used for analyzing patterns in request timing or for sequencing events.

*Downtime (No.of servers):*
Reflects the no.of servers down. A value of 0.0 indicates no servers are down at that second.

*Predicted Status Code:*
Represents the status codes predicted by the Company's team for each client request. These predictions may or may not be correct.
500 - Internal Server Error 200 - Successful Request


### Objective
Direct each incoming request to an available server assigned to the respective endpoint, given that each endpoint has 3 servers which may or may not be down at different timestamps. The goal is to determine the number of successfully predicted requests by the team for each client and calculate each client's total_price, based on the fixed price associated with each endpoint.

#### Points to be considered :
1. The requests in the same timestamp must be processed in the lexicographical order.
2.  A Single client is only allowed to hit one endpoint at a given timestamp. Other requests are not processed and are not taken into consideration for evaluation.
3.  The time taken to handle a client request by any server is 1 second.

#### Workflow Constraints :
1. You are obligated to use exactly three stages to account to this solution. (i.e. three pairs of Mappers and Reducers)
2. Do not import any external modules. Use modules only available in the default python package.
3. The output should be in space separated format.


#### Testing your code
Here is a sample script on testing your multi-stage map reduce.


```
#!/usr/bin/env bash

# Clean up the intermediate HDFS directories which could have been created as a part of a previous run 
hdfs dfs -ls /intermediate-1
if [[ $? == 0 ]]
then
	echo "Deleteing Intermediate-1 HDFS directory before starting job.." 
	hdfs dfs -rm -r /intermediate-1
fi

hdfs dfs -ls /intermediate-2
if [[ $? == 0 ]]
then 
	echo "Deleting Intermediate-2 HDFS directory before starting job.." 
	hdfs dfs -rm -r /intermediate-2
fi

# Clean up the previously used output directory. 
hdfs dfs -ls /task2/output
if [[ $? == 0 ]]
then
    echo "Deleting previous output directory"
    hdfs dfs -rm -r /task2/output
fi


echo "Initiating stage-1"
echo "==========================================================="

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-mapper "$PWD/mapper_1.py" \
-reducer "$PWD/reducer_1.py" \
-input /task2/dataset.txt \
-output /intermediate-1

echo "==========================================================="
echo "Stage-1 done" 
echo "Initiating stage-2"
echo "==========================================================="
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-mapper "$PWD/mapper_2.py" \
-reducer "$PWD/reducer_2.py" \
-input /intermediate-1/part-00000 \
-output /intermediate-2
echo "==========================================================="
echo "Stage-2 done" 
echo "Initializing stage-3"
echo "==========================================================="

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-mapper "$PWD/mapper_3.py" \
-reducer "$PWD/reducer_3.py" \
-input /intermediate-2/part-00000 \
-output /task2/output

echo "==========================================================="
echo "Stage-3 done"
```