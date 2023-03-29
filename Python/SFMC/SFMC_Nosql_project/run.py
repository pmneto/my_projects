def run():
    t = ""
    with open('main.py') as f:
        t = f.read()
    return t


exec(run())