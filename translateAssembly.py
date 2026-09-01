with open("assemblyInstruction.txt", "r") as input: 
    with open("instructionMemory.txt", "w") as iOutput, open("dataMemory.txt", "w") as dOutput:
        iOutput.write("v3.0 hex words addressed\n00: 00 " )
        dOutput.write("v3.0 hex words addressed\n00: " )
        text = True
        for line in input:
            output = ""
            line = line.strip()
            line = line.lower()
            line = line.replace(" ", "")
            if line == "":
                continue
            if line == ".text":
                text = True
                continue
            elif line == ".data":
                text = False
                continue
            if text: 
                if line[0:3] == "add":
                    output += "00"
                elif line[0:3] == "sub":
                    output += "01"
                elif line[0:3] == "ldr":
                    output += "10"
                elif line[0:3] == "str":
                    output += "11"
                if line[3:5] == "x0":
                    output += "00"
                elif line[3:5] == "x1":
                    output += "01"
                elif line[3:5] == "x2":
                    output += "10"
                elif line[3:5] == "x3":
                    output += "11"
                if line[6:8] == "x0":
                    output += "00"
                elif line[6:8] == "x1":
                    output += "01"
                elif line[6:8] == "x2":
                    output += "10"
                elif line[6:8] == "x3":
                    output += "11"
                if line[9:11] == "x0":
                    output += "00"
                elif line[9:11] == "x1":
                    output += "01"
                elif line[9:11] == "x2":
                    output += "10"
                elif line[9:11] == "x3":
                    output += "11"

                num = int(output, 2)
                hexOutput = format(num, "x")
                iOutput.write(hexOutput+ " ")
            else:
                num = int(line)
                hexOutput = format(num,"x")
                dOutput.write(hexOutput+ " ")

            