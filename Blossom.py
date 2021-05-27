

import pickle
import streamlit as st

st.title('Blossom Loan Prediction Assistant')

st.markdown('This application is meant to assist banks to classify how much loan a user can take based on certain factors ')
st.markdown('Please Enter the below details to know the results')

 
# loading the trained model
pickle_in = open('blossom.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome,
 CoapplicantIncome, Loan_Amount_Term, Credit_History, Property_Area):   
 
    # Pre-processing user input    
    if Gender == 'Male':
        Gender = 0
    else:
        Gender=1

    if Married == 'Yes':
        Married=0
    else:
        Married=1

    if Education == 'Graduate':
        Education=0
    else:
        Education=1

    if Dependents==1:
        Dependents=0
    elif Dependents==2:
        Dependents=1
    else:
        Dependents=2


    if Self_Employed == "Yes":
        Self_Employed = 1
    else:
        Self_Employed = 0

    if Property_Area=='Rural':
        Property_Area=0
    elif Property_Area=='Semiurban':
        Property_Area=1
    else:
        Property_Area=2

    # Making predictions 
    prediction = classifier.predict([[Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome,
 CoapplicantIncome, Loan_Amount_Term, Credit_History, Property_Area]])

    
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;"> Blossom Academy Loan Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 


    st.write('')
    st.write('')
      
    # following lines create boxes in which user can enter data required to make prediction 
    Gender = st.selectbox("Gender",('Male','Female'))
    Married = st.selectbox("Are You Married",( 'Yes','No'))
    Dependents = st.selectbox("How Many Dependents",('1', '2','3+'))
    Education = st.selectbox("What is your level of education",( 'Graduate','Non Graduate'))
    Self_Employed = st.selectbox("Are yoou Self Employed",('Yes','No'))
    ApplicantIncome=st.number_input("Applicant's Income (In GHC)")
    CoapplicantIncome=st.number_input("Co-Applicant's Income (In GHC)")
    Loan_Amount_Term=st.number_input("Loan Amount Term (In Days)")
    Credit_History=st.selectbox("Do You Have Credit History(1=Yes, 0=No)", ('1','0'))
    Property_Area=st.selectbox('Where is your proprties located?', ('Rural', 'Urban', 'Semi Urban'))
    




    # when 'Predict' is clicked, make the prediction and store it 
    
    if st.button("Predict Amount", key='predict'):
        try:
            Model = classifier  #get_model()
            prediction = Model.predict([[Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome,
 CoapplicantIncome, Loan_Amount_Term, Credit_History, Property_Area]])
            output = round(prediction[0],2)
            if output==0:
                st.warning("Sorry, we cannot get you a loan Now !!")
            else:
                st.success("Congratulations, You can get a loan of {} GHC 🙌".format(output))
        except:
            st.warning("Opps!! Something went wrong\nTry again")
            
if __name__=='__main__': 
    main()