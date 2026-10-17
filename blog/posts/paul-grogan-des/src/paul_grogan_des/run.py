from .simulation import Simulation


def main() -> None:
    S = Simulation()

    for _ in range(2018):
        S.advance_time()


if __name__ == "__main__":
    main()
