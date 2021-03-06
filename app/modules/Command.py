from enum import Enum
from typing import List

from modules.SplatoonWeapon import Category, SpecialWeapon, SubWeapon, Buki, Custom


class Function(Enum):
    give_me = 'give-me'
    give = 'give'
    help = 'help'


class Option(Enum):
    category = 'category'
    cat = 'cat'
    special = 'special'
    sub = 'sub'
    custom = 'custom'
    not_match = 'not'
    replica = 'with-replica'


class Command:
    def __init__(self, func: Function, categories: List[Category], specials: List[SpecialWeapon], subs: List[SubWeapon],
                 customs: List[Custom], not_match: bool, replica: bool):
        self.func = func
        self.categories = categories
        self.specials = specials
        self.subs = subs
        self.customs = customs
        self.not_match = not_match
        self.replica = replica

    @staticmethod
    def instantiate(message: str):
        command = message.replace('$', '').split(' ')

        func = Function(command[0])
        del command[0]

        categories = []
        specials = []
        subs = []
        customs = []
        not_match = False
        replica = False

        for option in command:
            for enum in Option:
                if option.startswith('--' + enum.value):
                    value = option.replace('--' + enum.value + '=', '')

                    if enum is Option.cat or enum is Option.category:
                        categories.append(Category(value))

                    if enum is Option.special:
                        specials.append(SpecialWeapon(value))

                    if enum is Option.sub:
                        subs.append(SubWeapon(value))

                    if enum is Option.custom:
                        customs.append(Custom(value))

                    if enum is Option.not_match:
                        not_match = True

                    if enum is Option.replica:
                        replica = True

        return Command(func, categories, specials, subs, customs, not_match, replica)

    def execute(self):
        return Buki.get(self.categories, self.subs, self.specials, self.customs, self.not_match, self.replica)
