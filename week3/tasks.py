from invoke import task

PYTHON = "python3"  # ← ここ変えるだけでOK

@task
def run(c):
    c.run(f"{PYTHON} May5.py")

@task
def check(c):
    c.run(f"{PYTHON} -m py_compile May5.py")

@task
def lint(c):
    c.run("flake8 .")

@task
def test(c):
    c.run("pytest")

@task
def all(c):
    c.run("flake8 .")
    c.run("pytest")
    c.run(f"{PYTHON} May5.py")
