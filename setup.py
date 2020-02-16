from setuptools import setup, find_packages

args = {}
args['name'] = 'template_lib'
args['version'] = '0.0.1'
args['description'] = 'python setup template'
args['url'] = 'repo url'
args['install_requires'] = []
args['packages'] = find_packages()
# 'myapp = myapp.main:main'
# <exe name> = <package>.<file>:<function>
console_scripts = ['hello = hello.hello:main']
args['entry_points'] = {
    'console_scripts': console_scripts
}

if __name__ == "__main__":
    setup(**args)
