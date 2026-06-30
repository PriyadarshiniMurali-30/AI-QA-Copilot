from openpyxl import load_workbook


def read_requirements(file_path):

    workbook = load_workbook(file_path)

    sheet = workbook["Requirements"]

    requirements = []

    for row in sheet.iter_rows(min_row=2, values_only=True):

        requirement = row[0]

        if requirement is not None and str(requirement).strip() != "":
            requirements.append(requirement)

    return requirements