#!/usr/bin/python3
"""Contains the class for a simple interpreter."""
import cmd

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
        """Handle execution of empty line."""
        pass



if __name__ == '__main__':
    HBNBCommand().cmdloop()
