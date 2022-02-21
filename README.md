# cs598-ml4se

## Requirement

- python3
- pydot-1.4.2
    - `pip install -r requirements.txt`
- graphviz
    - `sudo apt install graphviz`

## Usage

```
usage: gen_representation_hqiu.py [-h] [-r REPRESENTATION] [-i INPUT] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -r REPRESENTATION, --representation REPRESENTATION
                        Select code representation from ["AST", "CG", "CFG"]
  -i INPUT, --input INPUT
                        Path to the project source code directory
  -v, --visualization   Visualize the generated code representations in graphs
```

Examples:

```
# owner
python gen_representation_hqiu.py -r AST -i owner/owner/src -v
python gen_representation_hqiu.py -r CG -i owner/owner/src -v
python gen_representation_hqiu.py -r CFG -i owner/owner/src -v

# hutool
python gen_representation_hqiu.py -r AST -i hutool/hutool-json/src -v
python gen_representation_hqiu.py -r CG -i hutool/hutool-json/src -v
python gen_representation_hqiu.py -r CFG -i hutool/hutool-json/src -v

# cfg4j
python gen_representation_hqiu.py -r AST -i cfg4j/cfg4j-git/src -v
python gen_representation_hqiu.py -r CG -i cfg4j/cfg4j-git/src -v
python gen_representation_hqiu.py -r CFG -i cfg4j/cfg4j-git/src -v

# commons-compress
python gen_representation_hqiu.py -r AST -i commons-compress/src/ -v
python gen_representation_hqiu.py -r CG -i commons-compress/src/ -v
python gen_representation_hqiu.py -r CFG -i commons-compress/src/ -v

# incubator-shenyu
python gen_representation_hqiu.py -r AST -i incubator-shenyu/shenyu-common -v
python gen_representation_hqiu.py -r CG -i incubator-shenyu/shenyu-common -v
python gen_representation_hqiu.py -r CFG -i incubator-shenyu/shenyu-common -v

# commons-cli
python gen_representation_hqiu.py -r AST -i commons-cli/src/ -v
python gen_representation_hqiu.py -r CG -i commons-cli/src/ -v
python gen_representation_hqiu.py -r CFG -i commons-cli/src/ -v

# commons-io
python gen_representation_hqiu.py -r AST -i commons-io/src/ -v
python gen_representation_hqiu.py -r CG -i commons-io/src/ -v
python gen_representation_hqiu.py -r CFG -i commons-io/src/ -v

# fastjson
python gen_representation_hqiu.py -r AST -i fastjson/src/ -v
python gen_representation_hqiu.py -r CG -i fastjson/src/ -v
python gen_representation_hqiu.py -r CFG -i fastjson/src/ -v
```

The location of generated code representations (in the format of `.dot` files) and their graphical visualizations (in the format of `.png` files) will be shown at the end.
