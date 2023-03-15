"""
9. Python Standard Library, 17. Running External Programs

External programs from a script.
Run scripts within a script.
"""
import subprocess

try:
    completed = subprocess.run(["python3", "other.py"],
                               capture_output=True, text=True)
    print("args", completed.args)
    print("returncode", completed.returncode)
    print("stderr", completed.stderr)
    print("stdout", completed.stdout)
except subprocess.CalledProcessError as ex:
    print(ex)

# subprocess.call
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen
