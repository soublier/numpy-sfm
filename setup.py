import pathlib
import setuptools

NAME = 'numpy-SfM'
VERSION = '0.0.1'


def set_init_dir():

    dir_list = [
        'src',
        'tests',        
        'data',
        'notebooks',
    ]

    file_dict = {
        'src/__init__.py': '',
        'tests/.gitkeep': '',        
        'data/.gitkeep': '',
        'notebooks/.gitkeep': '',
    }

    for dir_name in dir_list:
        p = pathlib.Path(dir_name)
        if p.exists():
            continue
        p.mkdir(parents=True, exist_ok=True)
        print('make dir {}'.format(dir_name))

    for file_name, file_content in file_dict.items():
        p = pathlib.Path(file_name)
        if p.exists():
            continue
        print('make file {} << {}'.format(file_name, file_content))
        p.write_text(file_content)


set_init_dir()

setuptools.setup(
    name=NAME,
    version=VERSION,
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'}
)