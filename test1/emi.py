from math import pow
import pandas as pd

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors


def calculate_emi(p, r, n):
    '''
    p -> principla
    r -> monthly rate
    n -> number of months
    '''
    emi = round(((p * r * (pow((1+r), n))) / (pow((1+r), n)-1)), 2)
    return emi


def write_to_pdf(df):
    pdf = SimpleDocTemplate("Loan Amortization Schedule.pdf", pagesize=letter)
    table_data = []

    for i, row in df.iterrows():
        table_data.append(list(row))

    table = Table(table_data)

    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
    ])

    table.setStyle(table_style)

    pdf_table = []
    pdf_table.append(table)
    pdf.build(pdf_table)

    print("created Loan Amortization Schedule.pdf")


def print_amortization_schedule(p, r, n, emi):
    '''
    p -> principle
    r -> monthly rate
    n -> number of months
    '''
    df = pd.DataFrame([], columns=["Outstanding Loan", "EMI",
                      "Monthly Interest", "Principle paid", "Closing Loan"])
    for i in range(1, n+1):
        monthly_interest_paid = round(p * r, 2)
        principle_paid = round(emi - monthly_interest_paid, 2)
        closing_loan = round((p - principle_paid)
                             if (p - principle_paid > 0) else 0, 2)
        # print(
        #     f"{i}\t{p:.2f}\t{emi:.2f}\t{monthly_interest_paid:.2f}\t{principle_paid:.2f}\t{closing_loan:.2f}")
        df.loc[len(df)] = [p, emi,
                           monthly_interest_paid, principle_paid, closing_loan]
        p = closing_loan
    df.index = range(1, len(df)+1)
    write_to_pdf(df)


principle = float(input("Principle Amount = "))

annual_rate = input("Annual Interest Rate (can include %) = ")
annual_rate_float = float(annual_rate.rstrip("%"))
monthly_annual_rate_float = annual_rate_float / (12 * 100)

number_of_year = float(input("Number of years = "))
number_of_months = number_of_year * 12

emi = (calculate_emi(principle, monthly_annual_rate_float, number_of_months))

print_amortization_schedule(
    principle, monthly_annual_rate_float, int(number_of_months), emi)
