import sys

print(f"Name of the script      : {sys.argv[0]}")
print(f"Arguments of the script : {sys.argv[1:]}")

cl_opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
cl_args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

print(f"options:{cl_opts}\narguments:{cl_args}")