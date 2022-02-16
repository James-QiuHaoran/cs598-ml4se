# PropertyGraph

A library to generate Abstract Syntax Tree and Control Flow Graph for Java programs based on an open-source repository: https://github.com/Zanbrachrissik/PropertyGraph

## Usage

```
$ cd out/artifacts/PropertyGraph_jar
$ java -jar main.jar [-d <projectPath>] [-a] [-c]

-d: project path  
-c: choose to generate CFG
-a: choose to generate AST
```

Example:

```
java -jar main.jar -d test/src -a -c
```
