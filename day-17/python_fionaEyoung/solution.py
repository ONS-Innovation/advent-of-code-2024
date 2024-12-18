class ThreeBitComputer:

    def __init__(self, fname, maxit=1000):
        with open(fname, 'r') as f:
            self.REG_A = int(f.readline().strip().split()[-1])
            self.REG_B = int(f.readline().strip().split()[-1])
            self.REG_C = int(f.readline().strip().split()[-1])
            f.readline()
            self.PROG = [int(i) for i in f.readline().strip().split()[-1].split(',')]
        self.IPNTR = 0
        self.output = []

        self.ops = {0:self.adv, 1:self.bxl, 2:self.bst, 3:self.jnz, 4:self.bxc, 5:self.out, 6:self.bdv, 7:self.cdv}

        self.maxit = maxit

    def combo(self, x):
        if x>=0 and x<=3: return x
        match x:
            case 4:
                return self.REG_A
            case 5:
                return self.REG_B
            case 6:
                return self.REG_C
            case 7:
                raise NotImplementedError("7 is a reserved self.combo operand")
            case default:
                raise NotImplementedError(f"Unknown self.combo operand {x}")

    def adv(self, x):
        # Opcode 0: division A, self.combo
        self.REG_A = int(self.REG_A/(2**self.combo(x)))

    def bxl(self, x):
        # Opcode 1: bXOR, literal
        self.REG_B ^= x

    def bst(self, x):
        # Opcode 2: mod, self.combo
        self.REG_B = self.combo(x) % 8

    def jnz(self, x):
        # Opcode 3: jump, literal
        if self.REG_A:
            self.IPNTR = x
        else:
            self.IPNTR += 2

    def bxc(self, x):
        # Opcode 4, bXOR B C
        self.REG_B ^= self.REG_C

    def out(self, x):
        # Opcode 5, self.combo
        self.output.append(str(self.combo(x)%8))

    def bdv(self, x):
        # Opcode 6, division B, self.combo
        self.REG_B = int(self.REG_A/(2**self.combo(x)))

    def cdv(self, x):
        # Opcode 7, division C, self.combo
        self.REG_C = int(self.REG_A/(2**self.combo(x)))

    def instruction(self, op, x):
        self.ops[op](x)
        # NOJUMP = (3,)
        if op != 3:
            self.IPNTR += 2

    def run(self):
        i = 0
        HALT = False
        while not HALT:
            self.instruction(self.PROG[self.IPNTR], self.PROG[self.IPNTR+1])
            i += 1
            if self.IPNTR >= len(self.PROG): break
            if i > self.maxit: return False
        return True



# def instruction(opcode, operand):

fname = 'input.txt'
comp = ThreeBitComputer(fname)
# result = comp.run()

# bool(result)

print("Part 1: ", ','.join(comp.output))
