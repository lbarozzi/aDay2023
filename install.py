import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

if __name__ == '__main__':
    with open("requirements.txt") as f:
        packages= f.readlines()
        for pkg in packages:
            install(pkg)

print("Done")
