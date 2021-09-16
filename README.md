# Fastmake ⚡

Fastmake is a CLI build tool for when you don't want to write a makefile from scratch. Fastmake will bundle and compile all your files in the source directory and generate an executable.

### Installation 🔬

1. Clone this repository. 📝
2. Add an alias to the `main.py` file. 🐍
3. Ready to go. 🏌️‍♂️

### Usage 🥼

To generate an executable, just use the `-t` flag and point it to your source folder

```sh
$ fastmake -t src -e my_app.exe
```

### Flags 🚩

| Flag            | Usage                                                                     |
| --------------- | ------------------------------------------------------------------------- |
| [TARGET] -t     | Root folder of your project (where all you're files are stored)           |
| [COMPILER] -c   | Chosen compiler to compile your program (optional, defaults to gcc)       |
| [FLAGS] -f      | Add additional flags to the build command (optional, defaults to ENABLED) |
| [EXECUTABLE] -e | Add a name to your generated executable (optional, defaults to 'main')    |
| [FILE TYPE] -ft | Add a filetype as a default to generate the executable (defaults to .c)   |
| [HELP] -h       | Terminal helper with examples                                             |

### Want to try it out? 🧪

1. Clone this repository

```sh
$ git clone https://github.com/Nxrth-x/fastmake.git
```

2. Add an alias

```sh
$ alias fastmake="python main.py"
```

3. Generate an executable

```sh
$ fastmake -t example -e my_app.exe
```
