from fpdf import FPDF
from fpdf.drawing import DeviceRGB


class PDFCreator:
    def __init__(self, data: dict) -> None:
        self.data = data

    def create_cv(self) -> None:
        file = FPDF('P', format='A4')
        file.set_page_background(DeviceRGB(0.3, 0.3, 0.3))
        file.add_page()
        file.set_left_margin(20)
        self.__set_header(file)
        self.__set_about(file)
        self.__set_work_exp(file)
        self.__set_skills(file)
        self.__set_languages(file)
        self.__save(file)

    def __set_header(self, file: FPDF) -> None:
        file.set_font('Times', style='BI', size=25)
        file.set_text_color(255, 255, 255)
        file.cell(0, 5, f'{self.data["full_name"]}', align='C')

        file.ln(15)

        file.set_font('Times', style='I', size=12)
        file.write_html(f"""<b>Speciality</b>: {self.data['speciality']}
                        <br><br><b>Salary fork (per month, usd)</b>: {self.data['salary_from']}-{self.data['salary_to']}$
                        <br><br><b>Age</b>: {self.data['age']} y.o
                        <br><br><b>Location</b>: {self.data['location']}
                        <br><br><b>Email</b>: {self.data['email']}
                        <br><br><b>Telegram</b>: {self.data['telegram']}<br><br><br><br>""")

    def __set_about(self, file: FPDF) -> None:
        file.set_font('Times', style='BI', size=15)
        file.cell(0, 20, 'About Me:', border='T')
        file.ln(20)
        file.set_font('Times', style='I', size=12)
        file.write(h=0, txt=f'{self.data["about_me"]}')

    def __set_work_exp(self, file: FPDF) -> None:
        file.ln(20)
        file.set_font('Times', style='BI', size=15)
        file.cell(0, 20, 'Work Experience:', border='T')
        file.set_font('Times', style='I', size=12)
        count = 1
        for work in self.data['work_exp']:
            file.ln(20)
            file.write_html(f"""<font size="20">{count}:</font>
                            <br><br><b>Company</b>: {work['company']}
                            <br><br><b>Speciality</b>: {work['speciality']}
                            <br><br><b>Stack</b>: {work['stack']}
                            <br><br><b>Working Time</b>: {work['work_from']} to {work['work_to']}
                            <br><br><b>Responsibilities at work</b>: {work['responsibilities']}""")
            count += 1

    def __set_skills(self, file: FPDF) -> None:
        file.ln(20)
        file.set_font('Times', style='BI', size=15)
        file.cell(0, 20, 'Skills:', border='T')

        file.set_font('Times', style='I', size=12)
        file.ln(15)
        file.set_fill_color(66, 66, 66)
        file.multi_cell(0, 10, ', '.join([v['skill'] for v in self.data['skills']]), fill=True)

    def __set_languages(self, file: FPDF) -> None:
        file.ln(20)
        file.set_font('Times', style='BI', size=15)
        file.cell(0, 20, 'Languages:', border='T')

        file.set_font('Times', style='I', size=12)
        file.ln(12)
        for lang in self.data['lang']:
            file.write_html(f"""<br><br><b>{lang['lang']}</b>: {lang['level']}""")

    def __save(self, file: FPDF):
        file.output(f'{self.data["full_name"].replace(" ", "")}.pdf')
