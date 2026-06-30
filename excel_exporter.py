from openpyxl import Workbook


def create_sheet(workbook, sheet_name, header, items):

    sheet = workbook.create_sheet(title=sheet_name)

    sheet["A1"] = "ID"
    sheet["B1"] = header

    row = 2

    for item in items:

        sheet.cell(row=row, column=1, value=row - 1)
        sheet.cell(row=row, column=2, value=item)

        row += 1


def export_test_artifacts(data):

    workbook = Workbook()

    workbook.remove(workbook.active)

    create_sheet(
        workbook,
        "BA Questions",
        "Question",
        data["ba_questions"]
    )

    create_sheet(
        workbook,
        "Test Scenarios",
        "Scenario",
        data["test_scenarios"]
    )

    create_sheet(
        workbook,
        "Positive Tests",
        "Test Case",
        data["positive_test_cases"]
    )

    create_sheet(
        workbook,
        "Negative Tests",
        "Test Case",
        data["negative_test_cases"]
    )

    create_sheet(
        workbook,
        "Boundary Tests",
        "Test Case",
        data["boundary_test_cases"]
    )

    create_sheet(
        workbook,
        "Risks",
        "Risk",
        data["risks"]
    )

    workbook.save("QA_Test_Artifacts.xlsx")

    print("Excel workbook created successfully!")