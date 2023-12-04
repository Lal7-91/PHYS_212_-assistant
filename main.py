import streamlit as st

from dotenv import load_dotenv
from streamlit_option_menu import option_menu

load_dotenv()

from function import *




def main():


    def topics_menu():
            
            with st.sidebar:
                selected = option_menu(
                    menu_title="Topics:",  
                    options=["Home",
                              "Vectors", "Coulomb`s Law", 
                              "Electric Fields", "Electric Potential", 
                              "Capacitance", "Current & Resisrtant",
                              "Circutis", "Magnetic Fields",
                              "Magnetic Fields due Currents", 
                              "Induction & Induutance", "Electromagnatic Oscillations", 
                                "Contacts"
                              ],  
                    
                    icons=["house", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book", "envelope"], 
                    menu_icon="collection", 
                    default_index=0, 
                )
            return selected

    selected = topics_menu()

    col1, col2, col3 = st.columns([1.5,2,1])
    col21,col22,col23 = st.columns([1,10,1])
    col31,col32,col33 = st.columns([1,2,1])
    col41,col42,col43 = st.columns([1,2,1])


    

    if selected == "Home":    #Home

        
        
        col22.image("https://images.shiksha.com/mediadata/images/articles/1519899600phpTP3PsS.jpeg", 
                width= 650)
        
        col32.write("#### Welcom to PHYS-212 Assistant")
        col42.markdown("Made by Lal7")
    

    elif selected == "Vectors":

        topic = "Ch3.pdf"

        col1.write("## option menu:")

        st.divider()
        
        
        def chois_menu():
            
            chois = option_menu(
                menu_title=None,  
                options=["Summary", "Ask ✨", "Mini quiz"],  
                icons=["list", " ", "list-check"],    
                default_index= 1,  
                orientation="horizontal",
            )
            
            return chois
        
        chois = chois_menu()
        
        text = load_and_extract_one_pdf(topic)
        if chois == "Summary":
            
            with st.spinner("Wait ..."):
                st.write(Summary(text))
            
        elif chois == "Mini quiz":
             
            quiz = make_quiz()
            

            with st.spinner("Wait ..."):
                questions = quiz.get_questions(text)["questions"]
            
                quiz.display_questions(questions)



        elif chois == "Ask ✨":
            
            question = st.text_input(
            "Ask qustion about this topic",
            placeholder= ("Ask "))

            if question:
                

                with st.spinner("Just a sec .."):
                    
                    response = ask(topic, question)
                    
                    st.write("## Answer")
                    st.write(response)
        

    elif selected == "Coulomb`s Law":
        topic = "Ch21.pdf"
        
        col1.write("## option menu:")
        st.divider()

        def chois_menu():

            chois = option_menu(
                menu_title=None,  
                options=["Summary", "Ask ✨", "Mini quiz"],  
                icons=["list", " ", "list-check"],    
                default_index= 1,  
                orientation="horizontal",
            )

            return chois

        chois = chois_menu()
        text = load_and_extract_one_pdf(topic)
        

        if chois == "Summary":
            
            with st.spinner("Wait ..."):
                st.write(Summary(text))


        elif chois == "Mini quiz":
            
            quiz = make_quiz()

            with st.spinner("Wait ..."):
            
                questions = quiz.get_questions(text)["questions"]

                quiz.display_questions(questions)



        elif chois == "Ask ✨":
            
            question = st.text_input(
            "Ask qustion about this topic",
            placeholder= ("Ask "))

            if question:
                
                with st.spinner("Just a sec .."):
                    
                    response = ask(topic, question)
                    
                    st.write("## Answer")
                    st.write(response)


    elif selected == "Electric Fields":
        topic = "Ch22.pdf"
        
        col1.write("## option menu:")
        st.divider()

        def chois_menu():

            chois = option_menu(
                menu_title=None,  
                options=["Summary", "Ask ✨", "Mini quiz"],  
                icons=["list", " ", "list-check"],  
                default_index= 1,  
                orientation="horizontal",
            )

            return chois

        chois = chois_menu()
        text = load_and_extract_one_pdf(topic)
        

        if chois == "Summary":
            with st.spinner("Wait ..."):
                st.write(Summary(text))


        elif chois == "Mini quiz":
            
            quiz = make_quiz()

            with st.spinner("Wait ..."):
                questions = quiz.get_questions(text)["questions"]

                quiz.display_questions(questions)



        elif chois == "Ask ✨":
            
            question = st.text_input(
            "Ask qustion about this topic",
            placeholder= ("Ask "))

            if question:
                
                with st.spinner("Just a sec .."):
                    
                    response = ask(topic, question)
                    
                    st.write("## Answer")
                    st.write(response)


    elif selected == "Electric Potential":
        topic = "Ch24.pdf"
        
        col1.write("## option menu:")
        st.divider()

        def chois_menu():

            chois = option_menu(
                menu_title=None,  
                options=["Summary", "Ask ✨", "Mini quiz"],  
                icons=["list", " ", "list-check"],  
                default_index= 1,  
                orientation="horizontal",
            )

            return chois

        chois = chois_menu()
        text = load_and_extract_one_pdf(topic)
        

        if chois == "Summary":
            
            with st.spinner("Wait ..."):
                st.write(Summary(text))


        elif chois == "Mini quiz":
            
            quiz = make_quiz()

            with st.spinner("Wait ..."):
                questions = quiz.get_questions(text)["questions"]

                quiz.display_questions(questions)



        elif chois == "Ask ✨":
            
            question = st.text_input(
            "Ask qustion about this topic",
            placeholder= ("Ask "))

            if question:
                
                with st.spinner("Just a sec .."):
                    
                    response = ask(topic, question)
                    
                    st.write("## Answer")
                    st.write(response)


    elif selected == "Capacitance":
        topic = "CH25.pdf"
        
        col1.write("## option menu:")
        st.divider()

        def chois_menu():

            chois = option_menu(
                menu_title=None,  
                options=["Summary", "Ask ✨", "Mini quiz"],  
                icons=["list", " ", "list-check"],  
                default_index= 1,  
                orientation="horizontal",
            )

            return chois

        chois = chois_menu()
        text = load_and_extract_one_pdf(topic)
        

        if chois == "Summary":
            with st.spinner("Wait ..."):
                st.write(Summary(text))


        elif chois == "Mini quiz":
            
            quiz = make_quiz()

            with st.spinner("Wait ..."):
                questions = quiz.get_questions(text)["questions"]

                quiz.display_questions(questions)



        elif chois == "Ask ✨":
            
            question = st.text_input(
            "Ask qustion about this topic",
            placeholder= ("Ask "))

            if question:
                
                with st.spinner("Just a sec .."):
                    
                    response = ask(topic, question)
                    
                    st.write("## Answer")
                    st.write(response)
        
                
    elif selected == "Current & Resisrtant":
        topic = "Ch26.pdf"
        
        col1.write("## option menu:")
        st.divider()

        def chois_menu():

            chois = option_menu(
                menu_title=None,  
                options=["Summary", "Ask ✨", "Mini quiz"],  
                icons=["list", " ", "list-check"],  
                default_index= 1,  
                orientation="horizontal",
            )

            return chois

        chois = chois_menu()
        text = load_and_extract_one_pdf(topic)
        

        if chois == "Summary":
            with st.spinner("Wait ..."):
                st.write(Summary(text))


        elif chois == "Mini quiz":
            
            quiz = make_quiz()

            with st.spinner("Wait ..."):
                questions = quiz.get_questions(text)["questions"]

                quiz.display_questions(questions)



        elif chois == "Ask ✨":
            
            question = st.text_input(
            "Ask qustion about this topic",
            placeholder= ("Ask "))

            if question:
                
                with st.spinner("Just a sec .."):
                    
                    response = ask(topic, question)
                    
                    st.write("## Answer")
                    st.write(response)


    elif selected == "Circutis":
        topic = "Ch27.pdf"
        
        col1.write("## option menu:")
        st.divider()

        def chois_menu():

            chois = option_menu(
                menu_title=None,  
                options=["Summary", "Ask ✨", "Mini quiz"],  
                icons=["list", " ", "list-check"],  
                default_index= 1,  
                orientation="horizontal",
            )

            return chois

        chois = chois_menu()
        text = load_and_extract_one_pdf(topic)
        

        if chois == "Summary":
            with st.spinner("Wait ..."):
                st.write(Summary(text))


        elif chois == "Mini quiz":
            
            quiz = make_quiz()

            with st.spinner("Wait ..."):
                questions = quiz.get_questions(text)["questions"]

                quiz.display_questions(questions)



        elif chois == "Ask ✨":
            
            question = st.text_input(
            "Ask qustion about this topic",
            placeholder= ("Ask "))

            if question:
                
                with st.spinner("Just a sec .."):
                    
                    response = ask(topic, question)
                    
                    st.write("## Answer")
                    st.write(response)


    elif selected == "Magnetic Fields":
        topic = "Ch28.pdf"
        
        col1.write("## option menu:")
        st.divider()

        def chois_menu():

            chois = option_menu(
                menu_title=None,  
                options=["Summary", "Ask ✨", "Mini quiz"],  
                icons=["list", " ", "list-check"],  
                default_index= 1,  
                orientation="horizontal",
            )

            return chois

        chois = chois_menu()
        text = load_and_extract_one_pdf(topic)
        

        if chois == "Summary":
            with st.spinner("Wait ..."):
                st.write(Summary(text))


        elif chois == "Mini quiz":
            
            quiz = make_quiz()

            with st.spinner("Wait ..."):
                questions = quiz.get_questions(text)["questions"]

                quiz.display_questions(questions)



        elif chois == "Ask ✨":
            
            question = st.text_input(
            "Ask qustion about this topic",
            placeholder= ("Ask "))

            if question:
                
                with st.spinner("Just a sec .."):
                    
                    response = ask(topic, question)
                    
                    st.write("## Answer")
                    st.write(response)


    elif selected == "Magnetic Fields due Currents":
        topic = "Ch29.pdf"
        
        col1.write("## option menu:")
        st.divider()

        def chois_menu():

            chois = option_menu(
                menu_title=None,  
                options=["Summary", "Ask ✨", "Mini quiz"],  
                icons=["list", " ", "list-check"],  
                default_index= 1,  
                orientation="horizontal",
            )

            return chois

        chois = chois_menu()
        text = load_and_extract_one_pdf(topic)
        

        if chois == "Summary":
            with st.spinner("Wait ..."):
                st.write(Summary(text))


        elif chois == "Mini quiz":
            
            quiz = make_quiz()

            with st.spinner("Wait ..."):
                questions = quiz.get_questions(text)["questions"]

                quiz.display_questions(questions)



        elif chois == "Ask ✨":
            
            question = st.text_input(
            "Ask qustion about this topic",
            placeholder= ("Ask "))

            if question:
                
                with st.spinner("Just a sec .."):
                    
                    response = ask(topic, question)
                    
                    st.write("## Answer")
                    st.write(response)


    elif selected == "Induction & Induutance":
        topic = "Ch30.pdf"
        
        col1.write("## option menu:")
        st.divider()

        def chois_menu():

            chois = option_menu(
                menu_title=None,  
                options=["Summary", "Ask ✨", "Mini quiz"],  
                icons=["list", " ", "list-check"],  
                default_index= 1,  
                orientation="horizontal",
            )

            return chois

        chois = chois_menu()
        text = load_and_extract_one_pdf(topic)
        

        if chois == "Summary":
            with st.spinner("Wait ..."):
                st.write(Summary(text))


        elif chois == "Mini quiz":
            
            quiz = make_quiz()

            with st.spinner("Wait ..."):
                questions = quiz.get_questions(text)["questions"]

                quiz.display_questions(questions)



        elif chois == "Ask ✨":
            
            question = st.text_input(
            "Ask qustion about this topic",
            placeholder= ("Ask "))

            if question:
                
                with st.spinner("Just a sec .."):
                    
                    response = ask(topic, question)
                    
                    st.write("## Answer")
                    st.write(response)


    elif selected == "Electromagnatic Oscillations":
        topic = "Ch31.pdf"
        
        col1.write("## option menu:")
        st.divider()

        def chois_menu():

            chois = option_menu(
                menu_title=None,  
                options=["Summary", "Ask ✨", "Mini quiz"],  
                icons=["list", " ", "list-check"],  
                default_index= 1,  
                orientation="horizontal",
            )

            return chois

        chois = chois_menu()
        text = load_and_extract_one_pdf(topic)
        

        if chois == "Summary":
            with st.spinner("Wait ..."):
                st.write(Summary(text))


        elif chois == "Mini quiz":
            
            quiz = make_quiz()

            with st.spinner("Wait ..."):
                questions = quiz.get_questions(text)["questions"]

                quiz.display_questions(questions)



        elif chois == "Ask ✨":
            
            question = st.text_input(
            "Ask qustion about this topic",
            placeholder= ("Ask "))

            if question:
                
                with st.spinner("Just a sec .."):
                    
                    response = ask(topic, question)
                    
                    st.write("## Answer")
                    st.write(response)



    elif selected == "Contacts":
        
        st.divider()
        col2.write(" ## *X* : Lal7_91")
        st.divider()



if __name__ == "__main__":
     main()
