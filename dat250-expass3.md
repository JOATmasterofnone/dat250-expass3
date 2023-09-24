# Technical problems encountered during installation and use of MongoDB and how you resolved

There were no technical issues with the installation of MongoDB in Ubuntu. Installation went
smoothly if you followed the directions on the website.

# Screenshots for:

## The correct validation of the installation package

![Public Key MongoDB](publickeyMongodb.png)

## Relevant results obtained during Experiment 1

### C

![MongoDB Insert](mongod_insert.png)

### R

![MongoDB Query](mongod_query.png)

### U

![MongoDB Update](mongod_update.png)

### D

![MongoDB Remove](mongod_remove.png)

## Experiment 2 example working

![MongoDB Write](mongod_write.png)

## Map-reduce operation (and its result)

![MongoDB MapReduce](mongod_mapreduce.png)

### Reason for why your implemented Map-reduce operation

Since Map-reduce is deprecated from version 5.0 and we are using 7.0.1, I've implemented
an aggregation instead. The aggregation just checks to see how many chocolates were
purchased.

## Any pending issues with this assignment which you did not manage to solve

I intended to translate what was written in Python to Java and add it to a project in IntelliJ. But I was unable to do so with the time I had available.

