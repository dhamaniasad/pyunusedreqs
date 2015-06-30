def read_requirements():
    with open('requirements.txt', 'r') as req_file:
        reqs = req_file.readlines()
    requirements = reqs
    count = 0
    for req in reqs:
        requirements[count] = req.strip()
        count += 1


def command_line_runner():
    read_requirements()
