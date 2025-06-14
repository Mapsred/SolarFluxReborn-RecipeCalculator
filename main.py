from typing import Optional, List, Counter

from src import cli, solar_panels
from src.classes.item import Item
from src.utils.counter import recursive_list_count, count_all_items


def main() -> None:
    action: Optional[str] = None

    while action != 'quit':
        tier: str = cli.choose_from('tier', *map(str, range(6, 9)))

        if tier is None:
            continue

        amount: str = ''
        while not amount.isdigit():
            amount = cli.ask('Choose an amount [1]') or '1'

        int_amount: int = int(amount)
        solar_panel = solar_panels[int(tier) - 1]
        to_craft: List[Item] = (solar_panel.get_raw_recipe() * int_amount)

        count: Counter = recursive_list_count(to_craft).round_up()

        # Compte tous les items (y compris intermédiaires)
        all_items_count = count_all_items(solar_panel, int_amount)

        cli.pretty_list(
            "Items to craft",
            (f"{k} x{v:,}" for k, v in sorted(all_items_count.items(), key=lambda x: str(x[0])) if not k.is_base)
        )

        cli.pretty_list(
            "Total ressources needed",
            (f"{k} x{v:,}" for k, v in sorted(count.items()))
        )

        action: str = cli.choose_from('action', 'get materials', 'quit')


if __name__ == '__main__':
    main()
