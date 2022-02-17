import argparse
import os
import subprocess

PATH_ANALYZER = 'analyzer-hqiu/out/artifacts/PropertyGraph_jar/'
NAME_ANALYZER = 'main.jar'
NAME_CG_ANALYZER = 'javacg-static.jar'

app_paths = {
    "owner": "owner/out/artifacts/owner_jar/owner.jar",
    "hutool": "hutool/target/hutool-json-5.7.21.jar",
    "cfg4j": "cfg4j/out/artifacts/git-bind-1.0.0-SNAPSHOT.jar"
}

# get the AST representation of the code at the specified location
def get_ast(path):
    original_cwd = os.getcwd()
    print('Current working directory:', original_cwd)

    os.chdir(original_cwd + '/' + PATH_ANALYZER)
    cwd = os.getcwd()
    print('Current working directory:', cwd)

    if os.path.isfile(path) or os.path.isdir(path):
        # extract the AST representation of the code in the file or all files of the directory
        print('Target path:', path)
        result = subprocess.run(['java', '-jar', NAME_ANALYZER, '-a', '-d', path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.stdout:
            print(result.stdout.decode('utf-8'))
        if result.stderr:
            print(result.stderr.decode('utf-8'))
    elif os.path.isfile(original_cwd + '/' + path) or os.path.isdir(original_cwd + '/' + path):
        # extract the AST representation of the code in the file or all files of the directory
        print('Target path:', original_cwd + '/' + path)
        result = subprocess.run(['java', '-jar', NAME_ANALYZER, '-a', '-d', original_cwd + '/' + path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.stdout:
            print(result.stdout.decode('utf-8'))
        if result.stderr:
            print(result.stderr.decode('utf-8'))

        if path[-1] == '/':
            path = path[:-1]
        print('AST representation files are stored to:', original_cwd + '/' + path + '/../AST')
    else:
        print('Input file/directory not found:', path)

# get the CG representation of the code at the specified location
def get_cg(path):
    original_cwd = os.getcwd()
    print('Current working directory:', original_cwd)

    os.chdir(original_cwd + '/' + PATH_ANALYZER)
    cwd = os.getcwd()
    print('Current working directory:', cwd)

    if os.path.isfile(path) or os.path.isdir(path) or os.path.isfile(original_cwd + '/' + path) or os.path.isdir(original_cwd + '/' + path):
        # extract the CG representation from the jar generated in the project
        if 'owner' in path:
            path = original_cwd + '/' + app_paths['owner']
        elif 'hutool' in path:
            path = original_cwd + '/' + app_paths['hutool']
        elif 'cfg4j' in path:
            path = original_cwd + '/' + app_paths['cfg4j']
        print('Target path:', path)
        result = subprocess.run(['java', '-jar', NAME_CG_ANALYZER, path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.stdout:
            print(result.stdout.decode('utf-8'))
        if result.stderr:
            print(result.stderr.decode('utf-8'))
    else:
        print('Input file/directory not found:', path)

# get the CFG representation of the code at the specified location
def get_cfg(path):
    original_cwd = os.getcwd()
    print('Current working directory:', original_cwd)

    os.chdir(original_cwd + '/' + PATH_ANALYZER)
    cwd = os.getcwd()
    print('Current working directory:', cwd)

    if os.path.isfile(path) or os.path.isdir(path):
        # extract the CFG representation of the code in the file or all files of the directory
        print('Target path:', path)
        result = subprocess.run(['java', '-jar', NAME_ANALYZER, '-c', '-d', path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.stdout:
            print(result.stdout.decode('utf-8'))
        if result.stderr:
            print(result.stderr.decode('utf-8'))
    elif os.path.isfile(original_cwd + '/' + path) or os.path.isdir(original_cwd + '/' + path):
        # extract the CFG representation of the code in the file or all files of the directory
        print('Target path:', original_cwd + '/' + path)
        result = subprocess.run(['java', '-jar', NAME_ANALYZER, '-c', '-d', original_cwd + '/' + path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.stdout:
            print(result.stdout.decode('utf-8'))
        if result.stderr:
            print(result.stderr.decode('utf-8'))
    
        if path[-1] == '/':
            path = path[:-1]
            print('CFG representation files are stored to:', original_cwd + '/' + path + '/../CFG')
    else:
        print('Input file/directory not found:', path)

parser = argparse.ArgumentParser()

parser.add_argument("-r", "--representation", help="Select code representation from [\"AST\", \"CG\", \"CFG\"]")
parser.add_argument("-i", "--input", help="Path to the project source code directory")

args = parser.parse_args()
if args.representation and args.input:
    if args.representation not in ['AST', 'CG', 'CFG']:
        print("Unknown code representation format! Select code representation from [\"AST\", \"CG\", \"CFG\"] to proceed.")
        exit()
    print("Getting", args.representation, "of", args.input + "...")
    if args.representation == 'AST':
        get_ast(args.input)
    elif args.representation == 'CG':
        get_cg(args.input)
    elif args.representation == 'CFG':
        get_cfg(args.input)
else:
    parser.print_help()
