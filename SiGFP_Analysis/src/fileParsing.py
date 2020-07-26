from configparser import ConfigParser


class FileParsing:

    @staticmethod
    def parse_file(filename=None, section=None, outputformat='Dict'):
        parser = ConfigParser()

        parser.read(filename)

        if parser.has_section(section):
            params = parser.items(section)
            if outputformat == 'Dict':
                kwargs = {}
                for param in params:
                    kwargs[param[0]] = param[1]
                return kwargs

            elif outputformat == 'List':
                arg_list = []
                for param in params:
                    arg_list.append(param[1])
                return arg_list
            elif outputformat == 'String':
                for param in params:
                    single_arg = param[1]
                return single_arg
        else:
            raise Exception(f"Section {section} not found in the {filename} file")
