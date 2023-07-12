#!/usr/bin/python3
# Command Intepreter
import cmd
from models import base_model
import models

class HBNBCommand(cmd.Cmd):
    """
    Create class HBNBCommand
    """
    prompt = "(hbnb)"  # Set your custom prompt here

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
            if hasattr(base_model, args):
                # class_obj = getattr(base_model, args)
                dummy_instance = base_model.BaseModel()
                dummy_instance.save()
                print(dummy_instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
    
    def do_show(self, line):
        """Prints str repr of instance"""
        args = line.split()

        class_name = args[0]
        inst_id = args[1]

        try:
            if class_name:
                if hasattr(base_model, class_name):
                    # print(f"{class_name} class exists")
                    if len(args) == 1:
                        print("** instance id missing **")
                    else:
                        objs = models.storage.all()
                        for inst_name_id, inst  in objs.items():
                            cls_name_id = inst_name_id.split(".")
                            if inst_id == cls_name_id[1] and class_name == cls_name_id[0]:
                                print(inst)
                                return
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
        
        except IndexError:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
