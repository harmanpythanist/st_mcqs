import streamlit as st

def styled_text(text, underline=False, color="black", size=14, bold=False, font_family="Roboto"):
    styles = f'color: {color}; text-decoration: {"underline" if underline else "none"};'
    styles += f' font-size: {size}px; font-weight: {"bold" if bold else "normal"};'
    styles += f' font-family: {font_family};'
    st.markdown(f'<span style="{styles}">{text}</span>', unsafe_allow_html=True)

def check():
    with st.sidebar:
        styled_text('Enter your credentials on sidebar to access your account!', bold=True, size = 19)
        a = st.text_input('Username')
        b = st.text_input('Password')
        

        if a == 'manal' and b == 'manal002':
            st.success('correct')
            return 'manal'
        elif a == 'user' and b == 'user12':
            st.success('correct')
            return 'saad'
        elif a == 'harman' and b == 'harman21':
            st.success('correct')
            return 'harman'

        elif a == 'ml' and b == 'ml123':
            st.success('correct')
            return 'ml_arfa_class'
        elif a == 'f24phil' and b == 'f24phil':
            st.success('correct')
            return 'f24_test_mcq'

def mcqs_refining(data):
    a = data.split('---')
    questions = []
    answers = []
    for i in a:
        m = i.strip().split('\n')   
        if len(m) >= 5:
            questions.append(m[0]) 
            ans = m[1], m[2], m[3], m[4] 
            answers.append(ans)
        else:
            pass
    correct_options = []
    refined_answers = []

    for i in answers:
        tup = ()
        for j in i:
            if '*' in j:
                correct_options.append(j[:-1])  
                tup = tup + (j[:-1],)
            else:
                tup = tup + (j,)
        refined_answers.append(tup)

    return (correct_options, refined_answers, questions, answers)

def mcq_display(correct_options, refined_answers, questions, answers):
    if 'user_selections' not in st.session_state:
        st.session_state.user_selections = [None] * len(questions)
    for num in range(len(questions)):
        try:
            # Check if the user's previous selection exists in the refined answers list
            previous_selection = st.session_state.user_selections[num]
            index = refined_answers[num].index(previous_selection) if previous_selection in refined_answers[num] else 0
            
            st.session_state.user_selections[num] = st.selectbox(
                questions[num],
                refined_answers[num],
                key=f"question_{num}_{round}",
                index=index
            )
        except IndexError:
            st.error(f"Error displaying question {num + 1}: Check the answer options format.")

def check_mcq(correct_options, refined_answers, questions, answers):
    score = 0
    total = len(questions)
    for num in range(total):
        if st.session_state.user_selections[num] == correct_options[num]:
            score += 1
    styled_text(f'You scored {score}/{total}.', bold=True, size = 19)
    for num in range(total):
        if st.session_state.user_selections[num] == correct_options[num]:
            st.write(f"Question {num + 1}: Correct!")
        else:
            st.write(f"Question {num + 1}: Incorrect. The correct answer was {correct_options[num]}.")

styled_text('Welcome here to master your knowledge', size = 23)
st.write('---')



a = check()

if a == 'harman':
    st.subheader('Good luck for your quizzes!')
    a, b, c = st.tabs(['home', 'chap1', 'chap2'])

    with a:
        styled_text('Welcome. You can access your quizzes on next pages!', size = 17, bold = True)
        st.write('---')
        
    
    with b:    
        st.write('---')
        with open('harman_tests/quiz1.txt', 'r') as f:
            data = f.read()
            
        correct_options, refined_answers, questions, answers = mcqs_refining(data)
        mcq_display(correct_options, refined_answers, questions, answers)
        if st.button('Submit'):
            check_mcq(correct_options, refined_answers, questions, answers)


    
if a == 'ml_arfa_class':
    st.subheader('Good luck for your quizzes!')
    b,c,d,a = st.tabs(['home', 'week1', 'week2', 'week3'])

    with b:
        styled_text('Welcome. You can access your quizzes on next pages!', size = 17, bold = True)
        st.write('---')
        st.write('Contact me [here](https://www.instagram.com/fly_fazaia/)')
        
    
    with c:   
        round = 1
        st.write('---')
        with open('week_1_genai_arfa/week1.txt', 'r') as f:
            data = f.read()
            
        correct_options, refined_answers, questions, answers = mcqs_refining(data)
        mcq_display(correct_options, refined_answers, questions, answers)
        if st.button('Submit'):
            check_mcq(correct_options, refined_answers, questions, answers)
    
    with d:  
        round=2
        st.write('---')
        with open('week_1_genai_arfa/week2.txt', 'r') as f1:
            data1 = f1.read()
            
        correct_options1, refined_answers1, questions1, answers1 = mcqs_refining(data1)
        mcq_display(correct_options1, refined_answers1, questions1, answers1)
        if st.button('Submit_Week2'):
            check_mcq(correct_options1, refined_answers1, questions1, answers1)

    with a:
        round=3
        st.write('---')
        with open('week_1_genai_arfa/week3.txt', 'r') as f1:
            data1 = f1.read()
            
        correct_options1, refined_answers1, questions1, answers1 = mcqs_refining(data1)
        mcq_display(correct_options1, refined_answers1, questions1, answers1)
        if st.button('Submit_Week3'):
            check_mcq(correct_options1, refined_answers1, questions1, answers1)

        

if a == 'f24_test_mcq':
    st.subheader('Good luck for your quiz!')
    a, b = st.tabs(['home', 'Philosophy Final'])

    with a:
        styled_text('Welcome. You can access your quiz on next page!', size = 17, bold = True)
        st.write('---')
        
    
    with b:    
        round = 1
        st.write('---')
        with open('midss/phil.txt', 'r') as f:
            data = f.read()
            
        correct_options, refined_answers, questions, answers = mcqs_refining(data)
        mcq_display(correct_options, refined_answers, questions, answers)
        if st.button('Submit'):
            check_mcq(correct_options, refined_answers, questions, answers)
    









if a == 'saad':
    st.write('good hogya')
