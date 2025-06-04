from queue import Queue

if __name__ == "__main__":
    q = Queue()
    for _ in range(int(input())):
        inst = input().split()
        match inst[0]:
            case '1':
                q.put(int(inst[1]))
            case '2':
                q.get()
            case '3':
                print(q.queue[0])

