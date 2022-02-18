import argparse
import os
import subprocess
import pydot

PATH_ANALYZER = 'analyzer-hqiu/out/artifacts/PropertyGraph_jar/'
NAME_ANALYZER = 'main.jar'
NAME_CG_ANALYZER = 'javacg-static.jar'

app_paths = {
    "owner": "owner/out/artifacts/owner_jar/owner.jar",
    "hutool": "hutool/target/hutool-json-5.7.21.jar",
    "cfg4j": "cfg4j/out/artifacts/git-bind-1.0.0-SNAPSHOT.jar"
}

# get the AST representation of the code at the specified location
def get_ast(path, visualization=False):
    original_cwd = os.getcwd()
    print('Current working directory:', original_cwd)

    os.chdir(original_cwd + '/' + PATH_ANALYZER)
    cwd = os.getcwd()
    # print('Current working directory:', cwd)

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

        # visualization
        if visualization:
            print('Transforming .dot files to .png files...')
            dir_path = original_cwd + '/' + path + '/../AST'
            for file_name in os.listdir(dir_path):
                file_path = os.path.join(dir_path, file_name)
                print(file_path)
                graphs = pydot.graph_from_dot_file(file_path)
                graphs[0].write_png(dir_path + '/' + file_name[:-3] + 'png')
    else:
        print('Input file/directory not found:', path)

# get the CG representation of the code at the specified location
def get_cg(path, visualization=False):
    original_cwd = os.getcwd()
    print('Current working directory:', original_cwd)

    os.chdir(original_cwd + '/' + PATH_ANALYZER)
    cwd = os.getcwd()
    # print('Current working directory:', cwd)

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
def get_cfg(path, visualization=False):
    original_cwd = os.getcwd()
    print('Current working directory:', original_cwd)

    os.chdir(original_cwd + '/' + PATH_ANALYZER)
    cwd = os.getcwd()
    # print('Current working directory:', cwd)

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

        # visualization
        if visualization:
            print('Transforming .dot files to .png files...')
            dir_path = original_cwd + '/' + path + '/../CFG'
            for file_name in os.listdir(dir_path):
                if file_name == 'Util_cfg.dot':
                    continue
                file_path = os.path.join(dir_path, file_name)
                if os.path.getsize(file_path) < 100:
                    # skip files less than 100 bytes
                    continue
                print(file_path)
                try:
                    graphs = pydot.graph_from_dot_file(file_path)
                    graphs[0].write_png(dir_path + '/' + file_name[:-3] + 'png')
                except:
                    continue
    else:
        print('Input file/directory not found:', path)

parser = argparse.ArgumentParser()

parser.add_argument("-r", "--representation", help="Select code representation from [\"AST\", \"CG\", \"CFG\"]")
parser.add_argument("-i", "--input", help="Path to the project source code directory")
parser.add_argument("-v", "--visualization", action='store_true', help="Visualize the generated code representations in graphs")

args = parser.parse_args()
if args.representation and args.input:
    if args.representation not in ['AST', 'CG', 'CFG']:
        print("Unknown code representation format! Select code representation from [\"AST\", \"CG\", \"CFG\"] to proceed.")
        exit()
    print("Getting", args.representation, "of", args.input + "...")
    print("Visualization:", args.visualization)
    if args.representation == 'AST':
        get_ast(args.input, args.visualization)
    elif args.representation == 'CG':
        get_cg(args.input, args.visualization)
    elif args.representation == 'CFG':
        get_cfg(args.input, args.visualization)
else:
    parser.print_help()
