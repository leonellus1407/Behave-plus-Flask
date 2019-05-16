from datetime import datetime
import os


class do_behave:
    @staticmethod
    def run_feature():
        i_here = os.environ['HOME'] + "/PythonProjects/pzzby"
        os.chdir(i_here)
        my_file = os.environ['HOME'] + "/PythonProjects/pzzby/features/external.feature"
        os.system("behave --no-color " + my_file)
        f = open(i_here + "/log.txt", 'r')
        return_string = f.read() #.replace("\n", "<br>")
        f.close()
        return return_string

    @staticmethod
    def create_feature(no_handle_string):
        do_behave.write_to_file("", True, True)
        do_behave.write_to_file("", True, False)
        call_stack = do_behave.list_from_string(no_handle_string)
        for var in call_stack:
            do_behave.write_to_file(var + "\n", False, True)

    @staticmethod
    def list_from_string(string_to_handle):
        my_list = string_to_handle.replace('\\"', '\'')
        my_list = my_list.replace('[', '').replace(']', '')
        my_list = my_list.replace('"', '')
        my_list = my_list.replace("'", '"')
        my_list = my_list.split(', ')
        return my_list

    @staticmethod
    def write_to_file(string_to_write, new_file=False, is_feature=False):
        # Work with external.feature
        if is_feature:
            my_file = os.environ['HOME'] + "/PythonProjects/pzzby/features/external.feature"
            if new_file:
                f = open(my_file, 'w')
                string_to_write = "Feature: External Feature\n\n\tScenario:\n"
                f.write(string_to_write)
            else:
                f = open(my_file, 'a')
                f.write("\t\t" + string_to_write)
            f.close()
        # Work with log.txt
        else:
            my_file = "log.txt"
            if new_file:
                f = open(my_file, 'w')
            else:
                f = open(my_file, 'a')
                f.write(string_to_write)
            f.close()
