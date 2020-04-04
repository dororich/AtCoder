K = int(input())


cnt = 0
for e in range(10):
    for d in range(10):
        for c in range(10):
            for b in range(10):
                for a in range(10):
                    N = e * 10000 + d * 1000 + c * 100 + b * 10 + a
                    print(N)
                    if e != 0:
                        if abs(e - d) < 2 and abs(d - c) < 2 and abs(c - b) < 2 and abs(b - a):
                            cnt += 1
                        else:
                            pass
                    if d != 0:
                        if abs(d - c) < 2 and abs(c - b) < 2 and abs(b - a):
                            cnt += 1
                        else:
                            pass
                    if c != 0:
                        if abs(c - b) < 2 and abs(b - a):
                            cnt += 1
                        else:
                            pass
                    if b != 0:
                        if abs(b - a):
                            cnt += 1
                        else:
                            pass
                    if a != 0:
                        cnt += 1
                    if cnt == K:
                        # print('break')
                        print(N)
                        break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break
    else:
        continue
    break
