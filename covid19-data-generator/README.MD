# Data Generator for Covid-19 App

## Generate data based on the dataset from Massachusetts Department of Public Health COVID-19 Dashboard.



```shell script

mongoimport --uri "mongodb+srv://admin:<password>@info7275-group1.vfvn5.mongodb.net/covid2019" --collection User --drop --type csv --file ./Users.csv --headerline

mongoimport --uri "mongodb+srv://admin:<password>@info7275-group1.vfvn5.mongodb.net/covid2019" --collection TestCase --drop --type csv --file ./TestCases.csv --headerline
 
mongoimport --uri "mongodb+srv://admin:<password>@info7275-group1.vfvn5.mongodb.net/covid2019" --collection TestCase --drop --type csv --file ./MedicalStatus.csv --headerline

 
```
