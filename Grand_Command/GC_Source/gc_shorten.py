try:
    def shorten(Num):
        count = 0
        let = ""

        while Num >= 1000:
            Num /= 1000
            count += 1

        Num = str(Num)

        Num2 = ""

        if count >= 1:
            for i in range(Num.index(".")+2):
                Num2 += Num[i]

            Num = Num2

        if count == 1:
            Num += "K"
        if count == 2:
            Num += "M"
        if count == 3:
            Num += "B"
        if count == 4:
            Num += "T"
        if count == 5:
            Num += "q"
        if count == 6:
            Num += "Q"
        if count == 7:
            Num += "s"
        if count == 8:
            Num += "S"

        return Num
except ImportError:
    print("Cant import gc_shorten @ this time" )