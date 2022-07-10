#  pip install requests streamlit streamlit_lottie bokeh==2.4.1
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from bokeh.models.widgets import Div
from PIL import Image

st.set_page_config(
    page_title="👨‍💻 Satya Sasi Vatsal",
    page_icon=":boy:",
    layout="wide",
)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Specially codded Style.css remove streamlit branding
local_css("css/styles.css")

#  Anchor
st.title("#")  # This anchor is needed for the page to start at the top when it is called.



image = Image.open('profile.png')
_, img_column, _ = st.columns((2,1,2))
img_column.image(image, use_column_width  = True)

st.write('''
# B.Satya Sasi Vatsal
#### Python/Django Developer
''')

with st.container():
    col1, col2 = st.columns((2, 1))
    with col1:  
        st.write("""""")
        st.write("""""")
        st.write("""""")
        st.write("""""")
        st.write("""""")
        st.write("""""")

        st.subheader(
            """
            I am a Self- motivated, Inquisitive, energetic computer science engineering student skilled in leadership, with a strong foundation in math, logic,cross-platform coding and I love to teach !!, I am looking for an opportunity to work with a team that runs on clear communication. I want to align myself with a company I believe in and where I can create positive change.I possess a sharp eye for detail, which I use to find even the smallest errors in code. I work well under pressure and can produce high-quality work in short periods of time. I have strong interpersonal skills and work with a wide variety of people. I am always looking to learn more and am open to taking on challenging projects
            """
        )
    with col2:
        st_lottie(
            load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_bniew9j6.json"),
            height=500,
        )


with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st_lottie(
            load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_Yiahbq.json"),
            height=500,
        )
    with col2:
        st.header("About")
        st.write(
            """
            I have been programming since 2020, starting with developing a Python package and contributing to open source
            
            Short facts & milestones:
            - Certified Django Developer ([verify](https://drive.google.com/file/d/1OWLOo2pgd7NxWCNB8Nva9i0FcbfALti6/view?usp=sharing))
            - Certified Data-Science Engineer ([verify](https://drive.google.com/file/d/1eQj_lp68nttPUAhr2UAG6gijdAJ9LVPl/view?usp=sharing))
            - Lead Igniter in D2c igniters student Club in VIIT
            - Conducted "Basics of Coding" Workshop for 150+ students
            - Secured 2nd position in inter college held Web-Hackathon
            - Secured 15th,18th rank among 400+ participants in intra college competitive coding
            - Enthusiasm for data engineering, automating, data visulaization, teaching and fast food 🍕🍟🥓
            - 🐼 You can arrest me for animal trafficking, coz i deal with pandas a lot.
            - ✉️ You can contact me at sasivatsal7122@gmail.com 
            - Checkout my resume - [Click_Here](https://drive.google.com/file/d/1gPLBjuDx2Uf4O8Bw-MFusUVU_3XSyZu_/view)
            If you are interested in building something together, have questions/suggestions about my code or just wanna connect, feel free to get in touch with me! 
            """
        )
        download_resume = st.download_button(
                            label="Download My Resume",
                            data="resume/SasiVatsal's_Resume.pdf",
                            file_name="SasiVatsal's_Resume.pdf",
                            mime='text/pdf',
                            )
        

def txt(a):
    _, col, _ = st.columns((1,3,1))
    with col:
        st.markdown(a)

def txt1(a, b):
  _, col1, col2, _ = st.columns([1,2,1,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)



# --- Education ---
with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.header("Education")
        st.markdown("""<h3 style="color:red">B-tech Computer Science and Engineering</h3>""",unsafe_allow_html=True)
        st.markdown("""<h5> - Vignan's Institute of Information Technology 2020 - 2024</h5>""",unsafe_allow_html=True)
        st.markdown("""<h5> - CGPA: 8.86 (upto 2-1)</h5>""",unsafe_allow_html=True)
        st.write("""""")
        st.markdown("""<h3 style="color:red">Senior Secondary (XII), Science</h3>""",unsafe_allow_html=True)
        st.markdown("""<h5> - Ascent Junior College (SSC BOARD) </h5>""",unsafe_allow_html=True)
        st.markdown("""<h5> - Year of completion: 2020</h5>""",unsafe_allow_html=True)
        st.markdown("""<h5> - CGPA: 9.60/10</h5>""",unsafe_allow_html=True)
        st.write("""""")
        st.markdown("""<h3 style="color:red">Secondary (X)</h3>""",unsafe_allow_html=True)
        st.markdown("""<h5>Dr.KKR's Gowtham International School. (SSC board)</h5>""",unsafe_allow_html=True)
        st.markdown("""<h5> - Year of completion: 2018</h5>""",unsafe_allow_html=True)
        st.markdown("""<h5> - CGPA: 9.80/10</h5>""",unsafe_allow_html=True)
    with col2:
        st_lottie(
            load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_4rq0nvpt.json"),
            height=500,
        )




# --- TECH STACK / SKILLS ---
with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col2:
        st.header("Tech Stack / Skills")
        st.write(
            """
            Languages
            - `Python`, `C++/C`, `SQL`,`HTML`, `CSS`, `JavaScript`
            Frameworks
            - `FastAPI`, `Dash`, `Django`, `Flask`, `Bootstrap`
            Python Library
            - `numpy`, `opencv`, `pandas`, `glob`, `requests`, `PIL`
            Data Visualization
            - `Plotly`, `Seaborn`, `Matplotlib`
            Machine/Deep Learning
            - `scikit learn`,`TensorFlow`, `Keras`
            Databases
            - `MySQL`, `MongoDB`
            Hosting & Cloud
            - `AWS`, `Azure`, `Heroku`, `Vercel`, `Streamlit Cloud` 😉
            Miscellaneous
            - `Git`, `Github`, `CI/CD`, `Docker`
             """
        )

    with col1:
        st_lottie(
            load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_ba013t74.json"),
            height=500,
        )


# --- PORTFOLIO ---
with st.container():
    st.write("---")
    st.header("Portfolio")
    st.write("##")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("images/cinematrix.png")
        st.subheader("CineMatrixxx")
        st.markdown("<TT>CineMatrix is one of its kind versatile, diversified movie recommending system</TT>",unsafe_allow_html=True)
        with st.expander("Full Description"):
            st.write("""CineMatrix is one of its kind versatile, diversified movie recommending system which is based on not one or two but a combination five different recommending algorithms.CineMatrix is built on a solid foundation of advanced algorithms and methods like K-Nearest-Neighbours,term-frequency-inverse-document-frequency(tfidf),cosine similarity,SVD and many more other advanced techniques which gives at most most accurate recommendations almost instantly. With an interactive and user friendly UI/UX CineMatrix stands out from the rest of the other recommenders on the internet.""")
        if st.button('Enter App', key="ews_enter"):
            js = "window.open('https://cinematrix.subzeroo.tech/')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
        if st.button('Github', key="ews_github"):
            js = "window.open('https://github.com/sasivatsal7122/Go_Screen-CineMatrix-ML-MODEL')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    
    with col2:
        st.image("images/marc.png")
        st.subheader("My Academic Record")
        st.markdown("<TT>My Academic Record is a Multi-Page Full Stack Responsive Web application made entirely from Python</TT>",unsafe_allow_html=True)
        with st.expander("Full Description"):
            st.write("""My Academic Record is a Multi-Page Full Stack Responsive Web application made entirely from Python🐍. My Academic Record is powerful web based app which serves an important purpose that is storing and tracking your academic performance and history like a digital diary or a log of you academic status. Not just recording it also provides data analytics of your performnace in an Aesthetic and visually pleasing graphs. The entire application is Responsive hence can be accessed in any device ranging from a smartphone to a desktop.
The moto of making this app is i personally feel unanswerable to myself where i'm lacking or whether is there any improvement or consistency in my perfromance compared to the last semester, why care you ask coz these little things matter in the end and we are just too lazy to enter those marks in a physical diary or keep record of them and carry, now..whats the better way of doing it?.. the solution is a web app which can be accessed anywhere on any device any time and there is no question of loosing the log cause eveything is digital as it should be in 21st century.""")
        if st.button('Enter App', key="gee_enter"):
            js = "window.open('https://marcviit.herokuapp.com/')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
        if st.button('Github', key="gee_github"):
            js = "window.open('https://github.com/sasivatsal7122/MyAcadRec--webapp')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    
    with col3:
        st.image("images/handgesture.png")
        st.subheader("HandGesture Recognition and Live Translator")
        st.markdown("<TT>sign detector, which detects alphabets from A to Z that can very easily be extended to cover a vast multitude of other signs and hand gestures.</TT>",unsafe_allow_html=True)
        with st.expander("Full Description"):
            st.write("""There have been several advancements in technology and a lot of research has been done to help the people who are deaf and dumb. Aiding the cause, Deep learning, and computer vision can be used too to make an impact on this cause.
This can be very helpful for the deaf and dumb people in communicating with others as knowing sign language is not something that is common to all, moreover, this can be extended to creating automatic editors, where the person can easily write by just their hand gestures.""")
        if st.button('Enter App', key="ccw_enter"):
            js = "window.open('https://hst.herokuapp.com')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
        if st.button('Github', key="ccw_github"):
            js = "window.open('https://github.com/sasivatsal7122/HandGesture-Recognition-and-Live-Translator')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)


with st.container():
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image("images/digitaldiary.png")
        st.subheader("Digital Diary")
        st.markdown("<TT>Digital Diary is a tool to write your diaries every day without needing to write your stuff in text files. Also it comes with great features which help you to organize your time, minimize your effort and remember your best memories audibly and visually</TT>",unsafe_allow_html=True)
        with st.expander("Full Description"):
            st.write("""we all know diary is a safe way to talk about issues that have irritated or frustrated you, but it is still helpful to keep track of the good things in life. There is a good chance that you might forget a lot of it, hence, a positive diary will be a gateway to positive emotions at any point in time instead of dragging the reader down every time they decide to look back. This can inspire one to write in a more casual manner. There are some advantages of keeping a diary. These benefits include improved emotional health and the ability to resolve traumatic experiences as a result of having a safe environment to convey your emotions.
But with time, many of us lost interest or dont have time to write diary or atleast maintain a diary at home. As the technology progress and many things have been digitalzied.. so why not diary? Digital Diary is a tool to write your diaries every day without needing to write your stuff in text files. Also it comes with great features which help you to organize your time, minimize your effort and remember your best memories audibly and visually. And even that's not the best part yet...

- There are no Ad's, wierd pop up's

- There is no scope for personal info leak

- Safe and Secure

- Seemless,fast and responsive

- Absolutely Free

- Can be used in phone,tablet,laptop,pc""")
            
        if st.button('Enter App', key="qrc_enter"):
            js = "window.open('https://digitaldiary.herokuapp.com')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
        if st.button('Github', key="qrc_github"):
            js = "window.open('https://github.com/sasivatsal7122/Digital_diary--Webapp')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    
    with col5:
        st.image("images/cinematrixbot.png")
        st.subheader("CineMatrix Telegram Bot")
        st.markdown("<TT>A Simple telegram bot made using python which can be used to download movies seemlessly</TT>",unsafe_allow_html=True)
        if st.button('Enter App', key="spw_enter"):
            js = "window.open('https://t.me/CineMatrixxx_bot')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
        if st.button('Github', key="spw_github"):
            st.write('Github opens in new browser tab')
            js = "window.open('https://github.com/ratherUsefulCode/streamlit-portfolio-page')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    
    with col6:
        st.image("images/yoursugardaddy.png")
        st.subheader("Your Sugar Daddy - ML APP")
        st.markdown("<TT>A powerful Multi Page web application which can diagnose and predict diabetic symptoms and calculates pre risk diabetic features warning the user with an Interactive user friendly UI</TT>",unsafe_allow_html=True)
        if st.button('Enter App'):
            js = "window.open('https://yoursugardaddy.herokuapp.com/')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
            st.write('Web Application opens in new browser tab')
        if st.button('Github', key="bpw_github"):
            js = "window.open('https://github.com/sasivatsal7122/Your-Sugar-Daddy---ML_APP')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)


# --- CONTACT ---
with st.container():
    st.write("---")
    # st.subheader("Contact Me")
    # st.markdown("<h2 style='text-align: center;'>Contact</h2>", unsafe_allow_html=True)
    st.write("##")

    col1, col2= st.columns(2)
    with col1:
        st_lottie(
            load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_u25cckyh.json"),
            height=500,
        )
        
    with col2:
        st.write("""""")
        st.write("""""")
        st.write("""""") 
        st.subheader("Contact Me")
        contact_form = """
        <form action="https://formsubmit.co/sasivatsal7122@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="true">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)



