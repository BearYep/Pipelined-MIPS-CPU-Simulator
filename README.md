# Pipelined-MIPS-CPU-Simulator
Pipelined MIPS CPU Simulator for computer organization final project

Support five instructions, including `add`, `sub`, `beq`, `lw` and `sw`.

## Running

### You need to run this code in `Python 3.11.5`
Before each execution, you need to enter your test data in `./input/memory.txt`, which should be the combined language code of MIPS.

Once you have done that, you can run the program directly and you will get a `result.txt` file containing the required results, see **Input & Output Files** for detailed results.

## Input & Output Files

### Input: `memory.txt`
You need to enter your input into this file.

The format of the `memory.txt` should be the combined language code of MIPS.

### Output: `result.txt`
The simulation results will be output in this file.

It contains the state of each instruction at each cycle, the number of cycles it takes for the input code to run, and the final register and memory values.