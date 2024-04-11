import re

class WebMachine:
    def __init__(self, filename) -> None:
        self.undo_cache = []
        self.filename = filename
    
    def execute_command(self, command):
        if (len(command.split(' ')) == 3 and command.split(' ')[1] == '->'):
            return self.execute_shape_rule(command.split(' ')[0], command.split(' ')[2])
        elif (command == 'undo'):
            return self.undo()
        elif (len(command.split(' ')) == 2 and command.split(' ')[0] == 'newfile'):
            return self.change_active_file(command.split(' ')[1])
        elif (command == 'exit'):
            print("Exiting...")
            exit()
        else:
            return 'Invalid command!'

    def execute_shape_rule(self, shape_one, shape_two):
        content = []
        with open(self.filename, "r") as f:
            content = f.read()
        self.undo_cache.append(content)

        shape_indicies = [m.end(0) for m in re.finditer("style", content)]
        ignore_idx = max(shape_indicies) # ignore CSS, assuming it is at the start
        
        updated_content = content[(ignore_idx + 1):]
        updated_content = updated_content.replace(shape_one, shape_two)

        new_content = content[:(ignore_idx + 1)] + updated_content
        with open(self.filename, "w") as f:
            f.write(new_content)

        return "Shape Rule Successfully Executed"
    
    def change_active_file(self, filename):
        self.filename = filename
        return "Filename Successfully Changed"

    def undo(self):
        if (len(self.undo_cache) == 0): return "Cannot undo anymore"

        previous_data = self.undo_cache.pop(-1)
        with open(self.filename, "w") as f:
            f.write(previous_data)

        return "Undo Successful"