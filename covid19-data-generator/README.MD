# Data Generator for Covid-19 App


```shell script

 mongoimport --uri "mongodb+srv://admin:admin@info7275-group1.vfvn5.mongodb.net/covid2019" --collection User --drop --type csv --file /Users/gaomc/code/INFO7275/final/covid19-server/covid19-data-generator/generated-data/Users.csv --headerline

 mongoimport --uri "mongodb+srv://admin:admin@info7275-group1.vfvn5.mongodb.net/covid2019" --collection TestCase --drop --type csv --file /Users/gaomc/code/INFO7275/final/covid19-server/covid19-data-generator/generated-data/TestCases.csv --headerline
```