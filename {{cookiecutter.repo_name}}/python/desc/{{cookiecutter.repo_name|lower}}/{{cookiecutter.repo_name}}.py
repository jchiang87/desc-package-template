class {{cookiecutter.repo_name}}(object):
    '''
    Example class for {{cookiecutter.repo_name}} package.
    '''
    def __init__(self, message):
        self.message = message

    def run(self, raise_error=False):
        if raise_error:
            raise RuntimeError()
        return self.message

if __name__ == '__main__':
    foo = {{cookiecutter.repo_name}}()
    print foo.run()
