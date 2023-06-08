from Simulator import Simulator


def main():
    simulator = Simulator(40, 1024, 512, 256)
    simulator.enable_logger()
    simulator.start()


if __name__ == "__main__":
    main()