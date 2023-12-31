from PipelineCPU import CPU
            
app = CPU()

def main():

    path = './input/memory.txt'
    f = open(path, 'r', encoding='utf-8')
    lines = f.read().splitlines()
    print(lines)
    app.run(lines)
    print(app.reg)
    print(app.mem)
    f.close()

if __name__ == "__main__":
    main()
