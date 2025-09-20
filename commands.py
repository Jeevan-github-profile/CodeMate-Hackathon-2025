import os
import shutil

def ls(args):
    path = args[0] if args else "."
    try:
        return "\n".join(os.listdir(path))
    except FileNotFoundError:
        return f"ls: cannot access '{path}': No such file or directory"

def pwd(args):
    return os.getcwd()

def cd(args):
    if not args:
        return "cd: missing operand"
    try:
        os.chdir(args[0])
        return ""
    except FileNotFoundError:
        return f"cd: {args[0]}: No such directory"

def mkdir(args):
    if not args:
        return "mkdir: missing operand"
    try:
        os.mkdir(args[0])
        return ""
    except FileExistsError:
        return f"mkdir: cannot create directory '{args[0]}': File exists"

def rm(args):
    if not args:
        return "rm: missing operand"
    target = args[0]
    if os.path.isdir(target):
        shutil.rmtree(target)
    elif os.path.isfile(target):
        os.remove(target)
    else:
        return f"rm: cannot remove '{target}': No such file or directory"
    return ""
