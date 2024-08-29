#!/usr/bin/python3
"""Contains the class for a simple interpreter."""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Simple command interpreter"""
    prompt = '(hbnb) '

    def do_prompt(self, line):
        "Change the interactive prompt"
        self.prompt

    def do_EOF(self, line):
        """Handles end-of-file."""
        return True

    def do_quit(self, line):
        """Handles the quit command."""
        return True

    def emptyline(self):
        """Handles execution of empty line."""
        pass

    def do_create(self, line):
        """Creates a new instance of a valid class, saves it
        to a JSON file and prints the id.
        """
        if not line:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            a = storage.classes()[line]()
            a.save()
            print(a.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id.
        """
        if not line:
            print("** class name missing **")
            return
        args = line.split(' ')

        if len(args) == 1:
            print("** instance id missing **")
            return
        else:
            class_name = args[0]
            instance_id = args[1]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return
            else:
                key = f"{class_name}.{instance_id}"
                instance = storage.all().get(key)
                if instance is None:
                    print("** no instance found **")
                    return
                print(instance)

    def do_destroy(self, line):
        """Deletes an instance based on the class name
        and id and saves the change into the JSON file.
        """
        if not line:
            print("** class name missing **")
            return
        else:
            args = line.split(' ')

            if len(args) < 2:
                print("** instance id missing **")
            else:
                class_name = args[0]
                instance_id = args[1]

                if class_name not in storage.classes():
                    print("** class doesn't exist **")
                    return

                key = f"{class_name}.{instance_id}"
                instance = storage.all().get(key)

                if not instance:
                    print("** no instance found **")
                    return
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all
        instances based or not on the class name.
        """
        if not line:
            instances = [str(value) for key, value in storage.all().items()]
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            instances = [str(value) for key, value in storage.all().items() if key.startswith(f"{line}.")]
        print(instances)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating an attribute and saves the change into the JSON file.
        """
        if not line:
            print("** class name missing **")

        else:
            args = line.split(" ")
            class_name = args[0]

            if class_name not in storage.classes():
                print("** class doesn't exist **")

            elif len(args) < 2:
                print("** instance id missing **")

            elif len(args) < 3:
                print("** attribute name missing **")

            elif len(args) < 4:
                print("** value missing **")

            else:
                instance_id = args[1]
                attr_name = args[2]
                attr_value = args[3]

                if type(attr_name) == int:
                    attr_value = int(args[3].strip('"'))
                elif type(attr_name) == float:
                    attr_value = float(args[3].strip('"'))
                elif type(attr_name) == str:
                    attr_value = str(args[3].strip('"'))

                key = f"{class_name}.{instance_id}"
                instance = storage.all().get(key)

                if not instance:
                    print("** no instance found **")

                else:
                    setattr(instance, attr_name, attr_value)
                    storage.save()

    def default(self, line):
        """Handles commands for which there's no 'do_xx method'."""
        command = line.split(".")
        if len(command) != 2:
            return
        else:
            class_name = command[0]
            method = command[1]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            else:
                instances = [str(value) for key, value in storage.all().items() if key.startswith(f"{class_name}.")]
                if method == "all()":
                    print(instances)
                elif method == "count()":
                    print(len(instances))
                elif method.startswith("show"):
                    show_arg = method.split("w")
                    instance_id = show_arg[1].strip("()")
                    key = f"{class_name}.{instance_id}"
                    instance = storage.all().get(key)

                    if instance is None:
                        print("** no instance found **")
                    print(instance)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
