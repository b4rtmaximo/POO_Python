import resposta_0024


def main():
    b1 = resposta_0024.Cafe()
    b2 = resposta_0024.Cha()
    b3 = resposta_0024.Leite()

    b1.preparar()
    print("\n")
    b2.preparar()
    print("\n")
    b3.preparar()

if __name__ == "__main__":
    main()