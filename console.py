#!/usr/bin/python3
# Command Intepreter
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
