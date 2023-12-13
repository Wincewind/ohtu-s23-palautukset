from kps_funktiot import luo_peli


def main():
    while True:
        peli = luo_peli()
        if peli is None:
            break
        peli.pelaa()


if __name__ == "__main__":
    main()
