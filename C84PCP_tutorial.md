Hash the password 
===================


In this activity, you will learn to encrypt the password by fetching data from the signup form and storing it using hashing. 


<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10640570/lll.gif" width = "521" height = "235">


Follow the given steps to complete this activity.


* Open the file app.py.


*  Generate a hash for the password using the generateHash()function.  
```sh
    password = generateHash(password)
```
    
* Replace the decrypt code and generate a hash of the password variable received from the signin form and save it in the variable “hash”. 

```sh
    hash = generateHash(password)
```
    	    
* Replace the second condition in the if block to compare the hashed password with the current hash.

```sh
    if blockData['username'] == username and blockData['password'] == hash:
```


* Save and run the code to check the output. Try using the != operator in the if condition and check the output to observe the change.


