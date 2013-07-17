import subprocess


def shell(args):
    if not isinstance(args, (list, tuple)):
        args = args.split(' ')

    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()

    return (stdout.strip(), stderr.strip())
