import pandas as pd


def calculate_demographic_data(print_data=True):

    # Read data from file
    df = pd.read_csv(
        "adult.data.csv",
        names=[
            "age",
            "workclass",
            "fnlwgt",
            "education",
            "education-num",
            "marital-status",
            "occupation",
            "relationship",
            "race",
            "sex",
            "capital-gain",
            "capital-loss",
            "hours-per-week",
            "native-country",
            "salary"
        ],
        header=0,
        skipinitialspace=True
    )

    # Convert numeric columns to numbers
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["fnlwgt"] = pd.to_numeric(df["fnlwgt"], errors="coerce")
    df["education-num"] = pd.to_numeric(
        df["education-num"], errors="coerce"
    )
    df["capital-gain"] = pd.to_numeric(
        df["capital-gain"], errors="coerce"
    )
    df["capital-loss"] = pd.to_numeric(
        df["capital-loss"], errors="coerce"
    )
    df["hours-per-week"] = pd.to_numeric(
        df["hours-per-week"], errors="coerce"
    )

    # How many of each race are represented?
    race_count = df["race"].value_counts()

    # Average age of men
    average_age_men = round(
        df.loc[df["sex"] == "Male", "age"].mean(),
        1
    )

    # Percentage of people with a Bachelor's degree
    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100,
        1
    )

    # People with advanced education
    higher_education = df["education"].isin(
        ["Bachelors", "Masters", "Doctorate"]
    )

    # People without advanced education
    lower_education = ~higher_education

    # Percentage of people with advanced education earning >50K
    higher_education_rich = round(
        (
            df.loc[higher_education, "salary"] == ">50K"
        ).mean() * 100,
        1
    )

    # Percentage of people without advanced education earning >50K
    lower_education_rich = round(
        (
            df.loc[lower_education, "salary"] == ">50K"
        ).mean() * 100,
        1
    )

    # Minimum number of hours worked per week
    min_work_hours = df["hours-per-week"].min()

    # People who work the minimum number of hours
    num_min_workers = df["hours-per-week"] == min_work_hours

    # Percentage of those people earning >50K
    rich_percentage = round(
        (
            df.loc[num_min_workers, "salary"] == ">50K"
        ).mean() * 100,
        1
    )

    # Percentage earning >50K by country
    country_earning_percentage = (
        df.groupby("native-country")["salary"]
        .apply(lambda x: (x == ">50K").mean() * 100)
    )

    # Country with highest percentage earning >50K
    highest_earning_country = country_earning_percentage.idxmax()

    highest_earning_country_percentage = round(
        country_earning_percentage.max(),
        1
    )

    # Most popular occupation in India among people earning >50K
    india_rich = df[
        (df["native-country"] == "India") &
        (df["salary"] == ">50K")
    ]

    top_IN_occupation = india_rich["occupation"].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(
            f"Percentage with Bachelors degrees: "
            f"{percentage_bachelors}%"
        )
        print(
            f"Percentage with higher education that earn >50K: "
            f"{higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: "
            f"{lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: "
            f"{rich_percentage}%"
        )
        print(
            "Country with highest percentage of rich:",
            highest_earning_country
        )
        print(
            f"Highest percentage of rich people in country: "
            f"{highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage":
            highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }