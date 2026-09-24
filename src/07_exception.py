# def get_grade_text(grade_value: int) -> str:
#     grades = {
#         1: "Elégtelen",
#         2: "ELégséges",
#         3: "Közepes",
#         4: "Jó",
#         5: "Jeles",
#     }

#     if grades.get(grade_value) is None:
#         raise ValueError("This is not a valid grade value")

#     return grades.get(grade_value)


def get_grade_text(grade_value: int) -> str:
    grades = {
        1: "Elégtelen",
        2: "ELégséges",
        3: "Közepes",
        4: "Jó",
        5: "Jeles",
    }
    try:
        return grades[grade_value]
    except KeyError:
        raise ValueError(f"This is not a grade: {grade_value}")
    except RuntimeError:
        raise RuntimeError("Unexpected error...")


print(get_grade_text(20))
