

def add_ingot(purse):
    if "gold_ingots" in purse:
        purse["gold_ingots"] += 1
    else:
        purse["gold_ingots"] = 0
    return purse


def get_ingot(purse):
    if "gold_ingots" in purse:
        return purse


def empty(purse):
    purse.clear()
    return {}


def main():
    purse = {}
    print(add_ingot(get_ingot(add_ingot(empty(purse)))))
    purse["silver_ingots"] = 3
    add_ingot(purse)
    print(get_ingot(purse))


if __name__ == "__main__":
    main()
