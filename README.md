# What is the purpose of GET, POST, and DELETE methods? Why you have used them?
As GET is used to retrieve data from the server I used it to fetch all guestbook names without changing anything on the server and POST is used to send new data to the server so I used it to add a new guest name to the guestbook and assign it a unique ID and DELETE is used to remove data from the server so I used it to delete a guest entry by its ID and I also added error handling to return 404 if the ID does not exist
# What is the purpose of Postman? Why do we use it?
Postman is used to test APIs by sending http requests so I used it to to send GET POST and DELETE requests to my Flask server and check if the API is working correctly or not
# Why did we use in-memory storage here? Is this a good idea?
I used in-memory storage because this task required a simple temporary database and no external database setup
