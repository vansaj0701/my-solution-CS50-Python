from fpdf import FPDF


def main():
    name = input("Name: ").strip()
    text_on_image(name)


def text_on_image(name):
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.image("shirtificate.png", x=0, y=0, w=210)
    pdf.set_font("helvetica", "B", 24)
    width = pdf.get_string_width(name)
    x = (210-width) / 2
    y = 297 / 2
    pdf.text(x=x, y=y, text=name)
    pdf.output("shirtificate.pdf")


main()
