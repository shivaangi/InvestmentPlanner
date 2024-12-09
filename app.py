import json
import streamlit as st
import google.generativeai as genai
st.title("Investment Planner")
GOOGLE_API_KEY=st.secrets["API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

col1, col2 = st.columns(2)
with col1:
    goal = st.selectbox('What is your primary financial goal?',('Saving for retirement', 'Building an emergency fund', 'Buying a house','Paying for a child\'s education','Taking a dream vacation'))
    income = st.number_input('What is your current income level?')

with col2:
    time = st.selectbox(
        'What is your investment time horizon?',
        ('Short-Term (Less than 5 years)', 'Medium-Term (5-10 years)', 'Long-Term (10+ years)')
    )

    debt = st.selectbox('Do you have any existing debt?',('Yes','No'))

invest = st.number_input('How much investible money do you have available?')
scale = st.slider("How comofrtable are you with risk", min_value=1,max_value=10, step=1)

st.markdown("Made by Shivangi S :Sunflower:")

user_data = f""" - Primary financial goal is  {goal}"
                - Current income level: INR {income}"
                - Investment time horizon: {time}"
                - Debt Status: {debt}"
                - Investable Amount: INR {invest}
                - Risk tolerance{scale}/10 """
# create prompt_conditions = conditions.txt
prompt_conditions = f"""Given the above user data, create an investment plan
Note that your text should be Plain text.
Based on the above user details, provide a tailored investment plan
Add examples along with a description as to why.
Adjust as needed based on the variables given.
Add the amount needed to invest in each option based on the percentage and capital. Add some example stocks to the output format that match the goals. Give thorough explanation. Have the text be 600-700 words.
Include the following:
stocks to invest, timeline, approximate RoI. Along with numbers telling the return approximate
Include disclaimer about using AI for financial advice. """

prompt = user_data + prompt_conditions

if st.button("Generate Investment Plan"):
    with st.spinner('Creating Investment Plan for you'):
        text_area_placeholder = st.empty()

        response = model.generate_content(prompt)

        investment_plan = response.text

        st.title("Investment Plan")
        st.subheader("Personalised Investment Plan for you")
        st.markdown(investment_plan)


