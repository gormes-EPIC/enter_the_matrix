def main():
    result = input("Enter input: ")
    result = level_0(result)
    if result == "morpheus":
        print("Level 0 Complete")
        
        # Level 1
        result = input("Enter input: ")
        result = level_1(result)
        if result == "Ne0IsThe1":
            print("Level 1 Complete")
            
            # Level 2
            result = input("Enter input: ")
            result = level_2(result)
            if result == "reality":
                print("Level 2 Complete")
                
                # Level 3
                result = input("Enter input: ")
                result = level_3(result)
                if result == "b1u3p1ll":
                    print("Return to the matrix...")
                    return
                elif result == "R3dp1ll":
                    print("Level 3 Complete")
                    print("Follow the white rabbit...")
                    return
                
    print(f"{result} is incorrect. Try again")


def level_0(user_input):
    if user_input.startswith("enter"):
        start, end = user_input.split("_")
        end = end.replace("o", "u")
        end = end.replace("0", "o")
        end = end.replace("f", "ph")
        return end

def level_1(user_input):
    user_input = float(user_input)
    user_input = 2 - user_input
    user_input = f"{user_input:.2}"
    user_input = user_input.replace(".","IsThe")
    return f"Ne{user_input}"

def level_2(user_input):
    output = ""

    if user_input.startswith("A"):
        output += "trinity"
    elif user_input.startswith("B"):
        output += "neoishere"

    if len(user_input) == 5:
        if "ent" in user_input:
            user_input = user_input.replace("g", "000")
    elif len(user_input) == 6:
        if "srt" in user_input:
            user_input = user_input.replace("g", "12345")

    if len(user_input) == 7 and user_input.endswith("t"):
        first, last = output.split("n")
        output = "real" + last
    else:
        first, last = user_input.split("s")
        output = last + "ity"

    return output

def level_3(user_input):
    x = user_input[-2:] 
    passwd = ["t","a","k","e", "t", "h", "e", "b", "l", "u", "e", "p", "i", "l", "l"]
    output = "" 
    i = 0
    for ch in user_input:
        if ch == "a":
            output += str(int(x[0]) % 8)
        elif ch == "e":
            output += str(int(x[1]) // 3)
        elif ch == "i":
            output += i
        elif ch == "o":
            output += "p"
        elif ch == "u":
            output += user_input[5]
        elif ch >= "a" and ch < "f":
            output += user_input[2] * 2
            break
        elif ch >= "f" and ch < "n":
            output += user_input[i + 3]
        elif ch >= "n" and ch <= "q":
            output += ch + 1
        elif ch == "r":
            output += ch
        elif ch == "x":
            i += 1
            pass
        else:
            output += passwd[i]
        i += 1
    
    if len(output) != 0:
        output = output.capitalize()

    return f"{output}"

if __name__ == "__main__":
    main()
