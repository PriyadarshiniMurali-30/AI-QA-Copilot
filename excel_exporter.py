from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment


def export_to_excel(results, file_path):

    workbook = Workbook()

    sheet = workbook.active
    sheet.title = "QA Artifacts"

    headers = [
        "Requirement",
        "BA Questions",
        "Test Scenarios",
        "Positive Test Cases",
        "Negative Test Cases",
        "Boundary Test Cases",
        "Risks"
    ]

    # Header Style
    header_fill = PatternFill(start_color="4F81BD",
                              end_color="4F81BD",
                              fill_type="solid")

    header_font = Font(bold=True, color="FFFFFF")

    # Write Headers
    for col_num, header in enumerate(headers, start=1):

        cell = sheet.cell(row=1, column=col_num)

        cell.value = header
        cell.fill = header_fill
        cell.font = header_font

    # Write Data
    row_num = 2

    for result in results:

        sheet.cell(row=row_num, column=1).value = result["requirement"]

        sheet.cell(row=row_num, column=2).value = "\n".join(result["ba_questions"])

        sheet.cell(row=row_num, column=3).value = "\n".join(result["test_scenarios"])

        sheet.cell(row=row_num, column=4).value = "\n".join(
            tc["description"] for tc in result["positive_test_cases"]
        )

        sheet.cell(row=row_num, column=5).value = "\n".join(
            tc["description"] for tc in result["negative_test_cases"]
        )

        sheet.cell(row=row_num, column=6).value = "\n".join(
            tc["description"] for tc in result["boundary_test_cases"]
        )

        sheet.cell(row=row_num, column=7).value = "\n".join(result["risks"])

        # Wrap text for all cells
        for col in range(1, 8):

            sheet.cell(row=row_num,
                       column=col).alignment = Alignment(wrap_text=True,
                                                         vertical="top")

        row_num += 1

    workbook.save(file_path)