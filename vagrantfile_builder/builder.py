import os
import jinja2

class VagrantManager:
    def __init__(self):
        pass

    @classmethod
    def generate_vagrantfile(
            cls,
            config,
            vagrantfile_path='Vagrantfile'
    ):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        file = open(os.path.join(__location__, vagrantfile_path) , 'w+')

        file.write(cls.__load_template().render(config))
        file.close()

    @classmethod
    def __load_template(cls,template_path='Vagrantfile.template'):
        return (
            jinja2.Environment(
                autoescape=True,
                loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
                    .get_template(template_path)
        )

