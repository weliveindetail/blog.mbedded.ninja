---
authors: [ "Geoffrey Hunter" ]
date: 2013-03-18
draft: false
title: Linux Bash Commands For C
type: page
---

{{< figure src="/images/programming-misc/essential-bash-commands-for-c-screenshot.png" caption="Screenshot of essential bash commands for C being used in a terminal on Ubuntu."  width="450px" >}}

Below are a list of the most essential bash commands when working with the c programming language in linux.

Examples tested on Ubuntu v12.04.

```sh
# Install GNU C compiler and other essential C programs onto Linux platform
sudo apt-get install build-essential

## Creates c file called main.c in current directory and opens gedit to begin editing it
# (and frees terminal)
gedit main.c &

## Compiles C program main.c with standard flags and creates executable called main
gcc -Wall -W -Werror main.c -o main

## Run a compiled executable called main in the current directory
# Note that './' is mandatory, otherwise bash will think you have typed a command
./main

## Change file permissions on executable called main so that it will run (if experiencing 'Permission denied' errors)
chmod +x main

## Compiles C program main.c and creates executable called main with debugging symbols
gcc -Wall -W -Werror main.c -o main -g

## Starts debugging session on compile program called main.
# Make sure -g flag was used when compiling
gdb main

# GDB commands (omit the (gdb) prefix, this will be present in the terminal already)
(gdb) break 16   # Set breakpoint at line 16 (when running gdb)
(gdb) run        # Run program (when in gdb)
(gdb) n          # Move to next line
(gdb) c          # Continue to next breakpoint
(gdb) s          # Step to next line (unlike n, will jump into functions)
(gdb) print x    # Print the variable x
```