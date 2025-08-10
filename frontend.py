import streamlit as st
from essesntials import * 
from backend import CVMakerBackend
from bs4 import BeautifulSoup
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from io import BytesIO
from markdown import markdown

class CVMakerFrontend(CVMakerBackend):
    def __init__(self):
        CVMakerBackend.__init__(self)

    def front_page_title(self):
        st.markdown(
            """
            <style>
            .title {
                font-size: 50px;
                font-weight: 900;
                text-align: center;
                color: #2E86C1;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            .subtitle {
                font-size: 20px;
                font-weight: 400;
                text-align: center;
                color: #566573;
                margin-top: -15px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            </style>
            <div class="title">📄 NextStep CV</div>
            <div class="subtitle">✨ Helping you take the next big step in your career</div>
            <br><br>
            """,
            unsafe_allow_html=True
        )

    def get_contact_details(self):
        return st.text_area("📌 Personal Details", placeholder=personal_details, height=200)

    def get_education(self):
        return st.text_area("🎓 Education Background", placeholder=education.title(), height=200)

    def get_experience(self):
        return st.text_area("💼 Work Experience", placeholder=experience.title(), height=200)

    def get_projects(self):
        return st.text_area("🛠 Major Projects", placeholder=projects.title(), height=200)

    def get_skills(self):
        return st.text_area("⚡ Skills", placeholder=skills.title(), height=200)

    def get_programming_languages(self):
        return st.text_area("💻 Programming Languages", placeholder=programing_languages, height=150)

    def get_reference(self):
        return st.text_input("📜 Reference", placeholder=reference)

    def combine_all(self):
        self.front_page_title()

        with st.form("cv_form"):
            pd = self.get_contact_details()
            edu = self.get_education()
            exp = self.get_experience()
            pro = self.get_projects()
            sk = self.get_skills()
            pl = self.get_programming_languages()
            ref = self.get_reference()

            submit = st.form_submit_button("✅ Generate CV")

        if submit:
            if pd and edu and exp and pro and sk and pl and ref:
                # Prepare CV content
                final_string = f"""
                Personal Details:
                {pd}

                Education:
                {edu}

                Experience:
                {exp}

                Projects:
                {pro}

                Skills:
                {sk}

                Programming Languages:
                {pl}

                Reference:
                {ref}
                """

            else:
                st.error("⚠ Please fill all fields. Type 'No' if not applicable.")
            return self.chain.invoke({"input": final_string})
    
    def final_output(self):
        final_results = self.combine_all()

        if final_results:
            st.subheader("📄 Final CV Content")
            st.text_area("Generated CV", value=final_results, height=400)

            pdf_buffer = BytesIO()
            doc = SimpleDocTemplate(pdf_buffer)
            styles = getSampleStyleSheet()

            title_style = ParagraphStyle("TitleStyle", parent=styles["Title"], alignment=TA_CENTER, fontSize=20, spaceAfter=20)
            heading_style = ParagraphStyle("HeadingStyle", parent=styles["Heading2"], spaceAfter=10)
            normal_style = styles["Normal"]

            story = [Paragraph("", title_style), Spacer(1, 12)]

        # Convert markdown to HTML and parse it
            html_content = markdown(final_results)
            soup = BeautifulSoup(html_content, "html.parser")

            for element in soup.children:
                if element.name and element.name.startswith("h"):
                    story.append(Paragraph(element.get_text(), heading_style))
                elif element.name == "p":
                    story.append(Paragraph(element.get_text(), normal_style))
                    story.append(Spacer(1, 6))
                elif element.name in ["ul", "ol"]:
                    items = [ListItem(Paragraph(li.get_text(), normal_style)) for li in element.find_all("li")]
                    story.append(ListFlowable(items, bulletType="bullet"))
                    story.append(Spacer(1, 6))

            doc.build(story)
            pdf_buffer.seek(0)

            st.download_button(
                label="⬇ Download CV as PDF",
                data=pdf_buffer,
                file_name="NextStep_CV.pdf",
                mime="application/pdf"
            )
        else:
            st.error("⚠ No CV content to display. Please fill out the form first.")



bot = CVMakerFrontend()
bot.final_output()
