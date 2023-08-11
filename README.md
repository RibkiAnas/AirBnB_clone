<p align="center">
  <a href="" rel="noopener">
 <img src="https://camo.githubusercontent.com/59589bd21e8ec09ef94f2d9bb80d36d144bc487fe4737f8b213d005f3273921b/68747470733a2f2f696d6775722e636f6d2f4f696c457358562e706e67" alt="Project logo"></a>
</p>
<h3 align="center">0x00. AirBnB clone - The console</h3>

---

<p align="center"> The goal of this project is to create a website similar to AirBnB. The first step is to develop a backend interface, or console, that can handle data operations. The console allows the user to perform actions like creating, updating, and deleting objects, as well as managing file storage. The data is stored in JSON format and can be retrieved in future sessions.
    <br> 
</p>

### General Use

1. First clone the repository.

2. Once the repository is cloned locate the "console.py" file and run it as follows:

```
/AirBnB_clone$ ./console.py
```

3. When this command is run the following prompt should appear:

```
(hbnb)
```

4. This prompt designates you are in the "HBnB" console.
   You can use different commands in the console to do things like create, update, and delete objects, and manage how they are stored in files.

```
* create - Creates an instance based on given class

* destroy - Destroys an object based on class and UUID

* show - Shows an object based on class and UUID

* all - Shows all objects the program has access to, or all objects of a given class

* update - Updates existing attributes an object based on class name and UUID

* quit - Exits the program (EOF will as well)
```

### Examples

#### Basic Command Structure

###### 1. Create an object

```
(hbnb) create BaseModel
77ds6d-ajdj-902df-bb34b-93009dj
(hbnb)
```

###### 2. Show an object

```
(hbnb) show BaseModel 77ds6d-ajdj-902df-bb34b-93009dj
[BaseModel] (77ds6d-ajdj-902df-bb34b-93009dj) {'id': '77ds6d-ajdj-902df-bb34b-93009dj', 'created_at': datetime.datetime(2023, 8, 7, 14, 21, 12, 96959),
'updated_at': datetime.datetime(2023, 8, 7, 14, 21, 12, 96971)}
(hbnb)
```

###### 3. Destroy an object

```
(hbnb) destroy BaseModel 77ds6d-ajdj-902df-bb34b-93009dj
(hbnb) show BaseModel 77ds6d-ajdj-902df-bb34b-93009dj
** no instance found **
(hbnb)
```

###### 4. Update an object

```
(hbnb) update BaseModel 77ds6d-ajdj-902df-bb34b-93009dj first_name "anas"
(hbnb) show BaseModel 77ds6d-ajdj-902df-bb34b-93009dj
[BaseModel] (77ds6d-ajdj-902df-bb34b-93009dj) {'id': '77ds6d-ajdj-902df-bb34b-93009dj', 'created_at': datetime.datetime(2023, 8, 7, 14, 33, 45, 729889),
'updated_at': datetime.datetime(2023, 8, 7, 14, 33, 45, 729907), 'first_name': 'anas'}
(hbnb)
```

#### Variant Syntax

###### 1. Show all User Objects

```
(hbnb) User.all()
["[User] (8c66555f-28d7-4ae7-9156-f9299a9eb7e4) {'id': '8c66555f-28d7-4ae7-9156-f9299a9eb7e4', 'created_at': datetime.datetime(2023, 8, 10, 15, 57, 55, 703677), 'updated_at': datetime.datetime(2023, 8, 10, 15, 57, 55, 703687), 'first_name': 'Anas', 'last_name': 'Bar', 'email': 'airbnb6@mail.com', 'password': 'root'}", "[User] (1a816bcf-614a-4b3c-8310-92a24407a241) {'id': '1a816bcf-614a-4b3c-8310-92a24407a241', 'created_at': datetime.datetime(2023, 8, 10, 15, 57, 55, 704372), 'updated_at': datetime.datetime(2023, 8, 10, 15, 57, 55, 704393), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}"]
```

###### 2. Destroy a User

```
(hbnb) User.destroy(8c66555f-28d7-4ae7-9156-f9299a9eb7e4)
(hbnb) User.all()
["[User] (1a816bcf-614a-4b3c-8310-92a24407a241) {'id': '1a816bcf-614a-4b3c-8310-92a24407a241', 'created_at': datetime.datetime(2023, 8, 10, 15, 57, 55, 704372), 'updated_at': datetime.datetime(2023, 8, 10, 15, 57, 55, 704393), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}"]
```

###### 3. Update a User by attributes

```
(hbnb) User.update("1a816bcf-614a-4b3c-8310-92a24407a241", "first_name", "Anas")
(hbnb) User.all()
["[User] (1a816bcf-614a-4b3c-8310-92a24407a241) {'id': '1a816bcf-614a-4b3c-8310-92a24407a241', 'created_at': datetime.datetime(2023, 8, 10, 15, 57, 55, 704372), 'updated_at': datetime.datetime(2023, 8, 10, 15, 57, 55, 704393), 'first_name': 'Anas', 'email': 'airbnb2@mail.com', 'password': 'root'}"]
```

###### 3. Update a User by dictionary

```
(hbnb) User.update("1a816bcf-614a-4b3c-8310-92a24407a241", {'email': 'example@mail.com'})
(hbnb) User.all()
["[User] (1a816bcf-614a-4b3c-8310-92a24407a241) {'id': '1a816bcf-614a-4b3c-8310-92a24407a241', 'created_at': datetime.datetime(2023, 8, 10, 15, 57, 55, 704372), 'updated_at': datetime.datetime(2023, 8, 10, 15, 57, 55, 704393), 'first_name': 'Anas', 'email': 'example@mail.com', 'password': 'root'}"]
```
