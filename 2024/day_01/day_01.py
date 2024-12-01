# %%
import polars as pl

# %%
# Read in the data
df = pl.read_csv("input.txt", has_header=False)

# Clean the data and generate the part 01 calculations
df = (
    df.with_columns(
        pl.col("column_1")
        .str.split_exact("   ", 1)
        .struct.rename_fields(["first_part", "second_part"])
        .alias("fields")
    )
    .unnest("fields")
    .with_columns(
        pl.col("first_part")
        .cast(pl.Int64, strict=False)
        .alias("first_part_int")
        .sort(),
        pl.col("second_part")
        .cast(pl.Int64, strict=False)
        .alias("second_part_int")
        .sort(),
    )
    .with_columns(
        (pl.col("first_part_int") - pl.col("second_part_int")).abs().alias("part_01")
    )
)

# %%
# Answer to Pat 01
print(f"Part 01: {df.select("part_01").sum()}")

# %%
# How many time does each number appear in the second column
df_count = df["second_part_int"].value_counts()

# Join the data and calculate result to part 02
df = (
    df.join(
        df_count,
        left_on="first_part_int",
        right_on="second_part_int",
        how="left",
    )
    .fill_null(0)
    .with_columns((pl.col("first_part_int") * pl.col("count")).alias("part_02"))
)

# %%
# Answer to Pat 02
print(f"Part 02: {df.select("part_02").sum()}")

# %%
