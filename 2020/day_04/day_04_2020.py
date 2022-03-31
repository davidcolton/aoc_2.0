from aoc.data import read_blocks_of_data as rd
from pydantic import BaseModel, conint, ValidationError, validator

import string


class Passport(BaseModel):
    byr: conint(ge=1920, le=2002)
    iyr: conint(ge=2010, le=2020)
    eyr: conint(ge=2020, le=2030)
    hgt: str
    hcl: str
    ecl: str
    pid: str

    @validator("hgt")
    def check_height(cls, v):
        if "cm" in v or "in" in v:
            units = v[-2:]
            height = int(v[:-2])
            if (units == "cm" and 150 <= height <= 193) or (
                units == "in" and 59 <= height <= 76
            ):
                return v
        raise ValueError("Not a valid height")

    @validator("hcl")
    def check_hair_colour(cls, v):
        if v[0] == "#" and all(ch in string.hexdigits for ch in v[1:].lower()):
            return v
        else:
            raise ValueError("Not a valid hair colour")

    @validator("ecl")
    def check_eye_colour(cls, v):
        if v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return v
        else:
            raise ValueError("Not a valid eye colour")

    @validator("pid")
    def check_passport_id(cls, v):
        if len(v) == 9 and all(ch in string.digits for ch in v):
            return v
        else:
            raise ValueError("Not a valid passport")


def passport_list_to_dict(input: list) -> dict:
    # Takes a list of raw passports and returns a list of dictionaries
    passport_list = [l.replace("\n", " ").strip().split() for l in input]

    passports = [
        dict(key_value.split(":") for key_value in passport)
        for passport in passport_list
    ]

    year_types = ["byr", "iyr", "eyr"]

    # Fix year value type to be ints
    for passport in passports:
        for key_name in year_types:
            if key_name in passport.keys():
                passport[key_name] = int(passport[key_name])

    return passports


def simple_validation(passports: list) -> int:
    total_passports = len(passports)
    invalid_passports = sum(
        [1 for p in passports if len(p) < 7 or (len(p) == 7 and "cid" in p.keys())]
    )

    return total_passports - invalid_passports


def advanced_validation(passports: list) -> int:

    valid_passports = 0

    for passport in passports:
        try:
            p = Passport(**passport)
            valid_passports += 1
        except ValidationError:
            # Not a valid passport, nothing to do
            pass

    return valid_passports


if __name__ == "__main__":
    # Simple import
    # Single line of data imported as a string
    input = "day_04.txt"
    raw_data = rd(input)

    data = passport_list_to_dict(raw_data)

    print(f"PART 01: Simple Test Valid Passports: {simple_validation(data)}.")
    print(f"PART 02: Advanced Test Valid Passports: {advanced_validation(data)}.")
