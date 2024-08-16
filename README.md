# AirBnB clone - The console
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration, and so on.
# Command Interpreter
The command interpreter is exactly like the UNIX Shell, only that it is limited to a specific use-case. In our case, we want to be able to manage the objects of our project:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object
# Command Interpreter Usage
|  Command                      |  Example
|-------------------------------|------------------------------------------------------ 
|  Start command interpreter    |  ./console.py
|  Quit command Interpreter     |  (hbnb) quit 
|  Display help info of command |  (hbnb) help `<command>`
|  Create object                |  (hbnb) create `<class>` 
|  Show object                  |  (hbnb) show `<class> <id>` or (hbnb) `<class>.show(<id>)`
|  Show all objects or all class instances      |  (hbnb) all or (hbnb) all `<class>`   
|  Destroy object               |  (hbnb) destroy `<class> <id>` or (hbnb) destroy `<class>.destroy(<id>)`
|  Update an object attribute   |  (hbnb) update `<class> <id> <attribute name> "<attribute value>"` or (hbnb) `<class>.update(<id>, <attribute name>, "<attribute value>")`
# Examples
  # Intercative mode
  ![Screenshot 2024-08-15 210441](https://github.com/user-attachments/assets/efd8bdc8-118d-4835-89f3-dd802a14966f)
  # Non-interactive mode
  ![Screenshot 2024-08-16 111941](https://github.com/user-attachments/assets/d17eca41-c991-4f44-a9df-ade3889e071f)
# AirBnB_clone
