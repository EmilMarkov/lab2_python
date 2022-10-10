import os

class log:
    def __init__(self, name):
        self.path = os.getcwd()
        self.name = name

    def add(self, log_value):
        try:
            log_file = open(self.path + rf"\{self.name}", "a")
            try:
                log_file.write(str(log_value) + "\n")
            except Exception as e:
                print(e)
            finally:
                log_file.close()
        except Exception as ex:
            print(ex)

    def print(self):
        try:
            log_file = open(self.path + rf"\{self.name}", "r")
            try:
                for line in log_file:
                    print(line, end="")

            except Exception as e:
                print(e)
            finally:
                log_file.close()
        except Exception as ex:
            print(ex)