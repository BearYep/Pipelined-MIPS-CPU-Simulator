from PipelineCPU import CPU
            
app = CPU()

def main():

    path = './input/test4.txt'
    f = open(path, 'r', encoding='utf-8')
    lines = f.read().splitlines()
    print(lines)
    #app.readInstruction(lines)
    # for line in lines:
        # app.readInstruction(line)
        # app.run()
    app.run(lines)
    print(app.reg)
    print(app.mem)
    f.close()

if __name__ == "__main__":
    main()
