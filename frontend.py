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

    def get_person_details(self):
        return st.text_area("📌 Enter Your Details", placeholder=example, height=500)


    def combine_all(self):
        self.front_page_title()

        with st.form("cv_form"):
            ps = self.get_person_details()

            submit = st.form_submit_button("✅ Generate CV")

        if submit:
            if ps:
                # Prepare CV content
                final_string = f"All Details: {ps}"

            else:
                st.error("🚨⚠️ Please fill the field to generate CV.")
            return self.chain.invoke({"input": final_string})
    
    def final_output(self):
        final_results = self.combine_all()

        if final_results:
            st.subheader("📄 Final CV Content")
            st.markdown(final_results)

            pdf_buffer = BytesIO()
            doc = SimpleDocTemplate(pdf_buffer)
            styles = getSampleStyleSheet()

            title_style = ParagraphStyle(
                "TitleStyle", parent=styles["Title"], alignment=TA_CENTER, fontSize=20, spaceAfter=20
            )
            heading_style = ParagraphStyle(
                "HeadingStyle", parent=styles["Heading2"], spaceAfter=10, fontSize=14
            )
            normal_style = styles["Normal"]

        # Extract first line (Name) as title
            name_line = final_results.split("", 1)[0].strip()
            story = [Paragraph(name_line, title_style), Spacer(1, 12)]

        # Convert markdown to HTML
            html_content = markdown(final_results)
            soup = BeautifulSoup(html_content, "html.parser")

            for element in soup.children:
                if element.name and element.name.startswith("h"):
                    story.append(Paragraph(element.get_text(), heading_style))
                    story.append(Spacer(1, 6))
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
            st.error("🚨⚠️ No CV content to display. Please fill out the form first.")


bot = CVMakerFrontend()
bot.final_output()
