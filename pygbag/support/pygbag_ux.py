
# screen pixels (real, hardware)
WIDTH = 1280  # {{cookiecutter.width}}
HEIGHT = 720  # {{cookiecutter.height}}

def ux_dim(w,h):
    global WIDTH, HEIGHT
    WIDTH = int(w)
    HEIGHT = int(h)


# reference/idealized screen pixels
REFX = 1980
REFY = 1080

def u(real, ref, v):
    if abs(v) < 0.9999999:
        result = int((float(real) / 100.0) * (v * 1000))
        if v < 0:
            return real - result
        return result
    return int((real / ref) * v)

def ux(*argv):
    global WIDTH, REFX
    acc = 0
    for v in argv:
        acc += u(WIDTH, REFX, v)
    return acc

def uy(*argv):
    global HEIGHT, REFY
    acc = 0
    for v in argv:
        acc += u(HEIGHT, REFY, v)
    return acc

def ur(*argv):
    x = ux(argv[0])
    y = uy(argv[1])
    ret = [x, y]
    if len(argv) > 2:
        w = ux(argv[2])
        h = uy(argv[3])
        ret.append(w)
        ret.append(h)
    return ret