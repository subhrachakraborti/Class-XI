def main():
    print("Enter Your Word!")
    st = input()
    p = len(st)
    st = ' ' + st
    st1 = ""
    for i in range(p):
        ch = st[i]
        if ch.isspace():
            ch1 = st[i+1]
            st1 += ' ' + ch1.upper()
            i += 1
        else:
            st1 += ch
    print(st1)

if __name__ == "__main__":
    main()
