# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        # the left had side are the key names we have avaiable for our html file
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email =data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

# -------------------The R out of CRUD (read all)-----------------------------
# Now we use class methods to query our database.
#  We use class method to get all the instances from the database 
    @classmethod
    def get_all(cls):
        # we need to use a string of the SQL query we want to run 
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        # We are asking the function to connect to our database and run the query that we stated above
        results = connectToMySQL("users_assignment").query_db(query)
        # Best practice to print results to see if it pulled the correct infomration from the database.  If 
        # there was any issues, it would print False 
        print(results)
        # Create an empty list to append our instances of users
        all_users = []
        # Iterate over the db results and create instances of users with cls.
        for one_user in results:
            all_users.append(cls(one_user))
        return all_users


# class method to save our friend to the database (we can create a friend)
    @classmethod
    def save(cls, data ):
        # Remember that because this query includes variables, we should use a prepared statement. 
        query = "INSERT INTO users ( first_name , last_name , email ) VALUES ( %(fname)s , %(lname)s , %(uemail)s );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL("users_assignment").query_db( query, data )