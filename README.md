# Pipelined-MIPS-CPU-Simulator

Pipelined MIPS CPU Simulator for computer organization final project

The following instructions are supported, including:
- `add $dest $src1 $src2` - add `src1` and `src2` then store into `dest`  
- `sub $dest $src1 $src2` - sub `src2` from `src1` and store into `dest`  
- `beq $src1 $src2 index` - Compare `src1` and `src2` to see if they are equal, if true, then jump to the `index` instruction
- `lw $dest offset($src)` - Load the data in `src` with `offset` to `dest`
- `sw $src offset($dest)` - Save the data in `src` to `dest` with `offset`

## System Requirements

- Python: 3.11.5

## How to run

- Place your test data in `./input` and name it `memory.txt` prior to running.

- Run the program by 
    ```bash
    python main.py
    ``` 

    You will get a `result.txt` file containing the results as required for the project. 
    See **Input & Output Files** for details.

## Input & Output

### Input: `memory.txt`

Input instructions must be placed in this file, and the format of instructions should in the form of **MIPS**.

### Output: `result.txt`

Simulated results will be stored in this file, containing:
- States of each instruction at each cycle
- Numbers of cycles it takes to run the input instructions
- Final register and memory values