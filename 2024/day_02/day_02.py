import polars as pl


# %%
def safe(row: dict) -> bool:
    values = row.values()
    values = [x for x in values if x != None]
    return check_values(values)


def dampener_safe(row: dict) -> bool:
    values = row.values()
    values = [x for x in values if x != None]
    for n in range(len(values)):
        new_values = values[:n] + values[n + 1 :]
        if check_values(new_values):
            return True
    return False


def check_values(values):
    asc_comp = zip(values, values[1:])
    desc_comp = zip(values, values[1:])
    ascending = all((i < j) and (1 <= j - i <= 3) for i, j in asc_comp)
    descending = all((i > j) and (1 <= i - j <= 3) for i, j in desc_comp)
    return ascending or descending


# %%
schema = {
    "col_1": pl.Int32,
    "col_2": pl.Int32,
    "col_3": pl.Int32,
    "col_4": pl.Int32,
    "col_5": pl.Int32,
    "col_6": pl.Int32,
    "col_7": pl.Int32,
    "col_8": pl.Int32,
}

# Read Data
df = pl.read_csv("input.txt", separator=" ", schema=schema, has_header=False)

# Part 1
df_1 = df.with_columns(
    pl.struct(pl.all()).map_elements(safe, return_dtype=pl.Boolean).alias("safe")
)

# Part 2
df_2 = df_1.filter(pl.col("safe").eq(False)).with_columns(
    pl.struct(pl.all().exclude("safe"))
    .map_elements(dampener_safe, return_dtype=pl.Boolean)
    .alias("dampener_safe")
)

# %%
# Part 1
df_1.select(pl.col("safe")).sum()

# %%
# Part 2
# These are additional Dampener Safe
df_2.select(pl.col("dampener_safe")).sum()
