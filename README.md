<p align="center">
  <a href="" rel="noopener">
 <img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230807%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230807T103714Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d6b352d1b4b54c96308e7dfdbf014e8d9738170e2cb469fc50efaee4184558a9" alt="Project logo"></a>
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
