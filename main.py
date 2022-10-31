def main() -> None:
    tyngdeakselerasjon = 9.81
    høyde = 2.5
    luftmotstand_koeffisient = 0.07
    masse = 60 / 1000
    volume = 1.2E-4

    startfart = 0

    delta_tid = 0.1

    def a(v: float) -> float:
        # sum_f = m*a
        # a = sum_f/m
        # sum_f = G - L
        G = tyngdeakselerasjon * masse
        L = luftmotstand_koeffisient * v**2

        return (G - L) / masse


if __name__ == "__main__":
    main()
