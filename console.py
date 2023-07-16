#!/usr/bin/python3
"""Console intepreter for AirBNB clone"""
import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import models


class HBNBCommand(cmd.Cmd):
    """
    Create class HBNBCommand
    """
    prompt = "(hbnb)"  # Set your custom prompt here
    classes = [
            'BaseModel', 'Amenity', 'City', 'Place', 'Review', 'State', 'User']

    def do_EOF(self, line):
        """Checks end of file"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing if empty line is passed"""
        pass

    def do_create(self, args):
        """Creates a new instance"""
        if args:
            if args in self.classes:
                # class_obj = getattr(base_model, args)
                dummy_instance = eval(args)()
                dummy_instance.save()
                print(dummy_instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """Prints string representation of an instance"""
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id

        if key in models.storage.all():
            print(models.storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id

        if key in models.storage.all():
            del models.storage.all()[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        list_objs = []
        if line in self.classes:
            objs = models.storage.all()
            for inst_name_id, inst in objs.items():
                cls_name_id = inst_name_id.split(".")
                if line == cls_name_id[0]:
                    list_objs.append(str(inst))
            print(list_objs)
        else:
            print("** class doesn't exist **")

    def custom_split(self, line):
        """
        Helper function for update
        splits classname and id
        """
        args = []
        current_arg = ""
        inside_quotes = False

        for char in line:
            if char == '"':
                inside_quotes = not inside_quotes
            elif char == ' ' and not inside_quotes:
                if current_arg:
                    args.append(current_arg)
                    current_arg = ""
                continue

            current_arg += char

        if current_arg:
            args.append(current_arg)

        return args

    def do_update(self, line):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        args = self.custom_split(line)

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id

        if key not in models.storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]
        instance = models.storage.all()[key]

        try:
            attribute_value = eval(attribute_value)
        except (NameError, SyntaxError):
            pass

        setattr(instance, attribute_name, attribute_value)
        models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
