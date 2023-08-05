#modules
import streamlit as st
import pandas as pd
from PIL import Image
from churnlytical_function import *
import sqlite3 as sq

#images
logo = Image.open('1.png')
#load= Image.open('2.png')
def add_bg():
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("https://tse3.mm.bing.net/th?id=OIP.rDF_M3IHxBtGhF0wKVihkAHaGJ&pid=Api&P=0");
                background-attachment: fixed;
                background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html=True
        )    
#add_bg()


#space containers
web_name=st.empty()
heading=st.empty()

side_logo=st.sidebar.empty()
side=st.sidebar.empty()
side_details=st.sidebar.empty()

content1=st.empty()
content2=st.empty()
content3=st.empty()
content4=st.empty()
content5=st.empty()
content6=st.empty()
content7=st.empty()
content8=st.empty()
content9=st.empty()
content10=st.empty()
content11=st.empty()

#refreshing space containers
def refresh(): 
    content1.write("")
    content2.write("")
    content3.write("")
    content4.write("")
    content5.write("")
    content6.write("")
    content7.write("")
    content8.write("")
    content9.write("")
    content10.write("")
    content11.write("")

#database functions
conn = sq.connect('data.db')
c = conn.cursor()

def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS usertable(username TEXT,password TEXT,company_name TEXT,company_address TEXT,fullname TEXT,email TEXT,phone_num1 TEXT,phone_num2 TEXT)')

def add_userdata(username,password,comp_name,comp_add,fullname,email,ph_no1,ph_no2):
	c.execute('INSERT INTO usertable(username,password,company_name,company_address,fullname,email,phone_num1,phone_num2) VALUES (?,?,?,?,?,?,?,?)',
    (username,password,comp_name,comp_add,fullname,email,ph_no1,ph_no2))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM usertable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data

def view_all_users():
	c.execute('SELECT * FROM usertable')
	data = c.fetchall()
	return data

def update_user_details(c_n,c_a,f,e,p1,p2):
    c.execute('UPDATE usertable SET company_name= ? , company_address= ? , fullname= ? , email= ? , phone_num1= ? ,phone_num2= ?  WHERE username = ? ',
    (c_n,c_a,f,e,p1,p2,st.session_state['username']))   
    conn.commit()

def del_table():
    c.execute('DROP TABLE usertable')

def check_profile():
    c.execute('SELECT * FROM usertable WHERE username =?',(st.session_state['username']))
    data=c.fetchone()
    return data

#functions

#1-login-signup
def signup():
        refresh()
        global_var()
        content1.subheader("Create New Account")
        new_user = content2.text_input("Username",placeholder='(enter email-id) <email>@<gmail>.com')
        new_password = content3.text_input("Password",type='password', placeholder="(6-15 characters, alpha-numeric characters)")
        sign=content5.button("Signup")

        if new_password:
            if isValid_Password(new_password)==1 or isValid_Username(new_user)==1:
                content4.error("Password should be of length 6-15 characters. Password can have only alphabets and numbers.")
                if sign:
                    content6.error("Signup failed. Kindly check the username and password entered.")
            elif sign:
                create_usertable()
                add_userdata(new_user,make_hashes(new_password),new_comp_name,new_comp_add,new_fullname,new_email,new_ph_1,new_ph_2)
                content5.success("You have successfully created an valid account")
                content6.info("Go to 'Login' option in the 'Login Menu' to login")  

        #experimentation
        if content7.checkbox("User Profiles"):
                    user_result = view_all_users()
                    clean_db = pd.DataFrame(user_result,columns =["Username","Password","company_name","company_address","fullname","email","phone_num1","phone_num2"] )
                    content8.dataframe(clean_db)
        if content9.checkbox('del',disabled=True):
            del_table()
        content7.write("")
        content9.write("")

#2-login-main
def login():
        refresh()
        heading.subheader("Login Section")
        username = content1.text_input("User Name")
        password = content2.text_input("Password",type='password')
        login_logout=content3.text("Login")

        if content4.checkbox("submit") and username and password:
            create_usertable()
            hashed_pswd = make_hashes(password)
            st.session_state['username']=username
            st.session_state['pass']=password

            result = login_user(username,check_hashes(password,hashed_pswd))
            if result:
                st.session_state['logged_in']=True

            #logout_button
            if (result and st.session_state['logged_in']==True) :
                content7.success("Logged In as {}".format(username))
                login_logout.text("Logout")
                content5.caption("To logout,  ***password field input*** should be **empty** ")
                if content4.button("logout"):
                    intro()
                    logout()
                nav2()   

            elif st.session_state['log_out']==False :
                content5.warning("Incorrect username or password.")

            if st.session_state['log_out']==True and st.session_state['logged_in']==False:
                content6.success("Logged Out Successfully.")
        else:
            content10.caption("To submit, enter username and password.")

#3-nav-home
def intro():
    refresh()
    heading.subheader("Introduction")
    content1.caption("Welcome to CHURNLYTICAL...")
    content3.info("As we know that service companies of telecommunication service businesses suffer from customer churn (a loss of valuable customers to competitors). This causes a huge loss to these companies.")
    content5.success(" ***We here at \"Churnlytical\", reduce these losses incurred by the telecom companies.*** ")
    content6.markdown(" We help companies better understand, **increase the number of customers using their telecom service** and **reduce the number of customers leaving** their telecom network. Thereby increasing their profit.")
    content8.warning(" ***If your company is also suffering from this problem of customer churn, go ahead and sign-up to analyze the behaviour of your customers.*** Thereby, increasing your company's profits. ")
    content9.caption("To 'sign-up', select option 'SignUp' under the 'Login Menu' drop-down list. ")

#4-nav-2
def nav2():
    task = side.selectbox("Task Menu",["LOGOUT","Profile","Churn Analysis-Online (1 customer)","Churn Analysis-Batch (many customers)"])
    if task=="LOGOUT":
        heading.subheader("Logout page")
        content7.info("For navigation use the drop-down list 'Task Menu'. ")
    elif task == "Profile":
        refresh()
        heading.subheader("Profile")
        profile()
    elif task=="Churn Analysis-Online (1 customer)":
        refresh()
        heading.subheader("Analysis: Online (1 customer)")
        nav_online()
    elif task == "Churn Analysis-Batch (many customers)":
        refresh()
        heading.subheader("Analysis: Batch (many customers)")
        nav_batch()

#5-profile
def profile():
    #content1.caption('Before submitting crosscheck all fields as they cannot be changed later.')
    #content2.caption('Incase, you need to change any details send a mail to the support.')
    content1.info('Once the form is submitted, values previously entered will not be visible to the user upon refreshing.')
    content2.success('Before submitting, crosscheck all fields. The user can edit their details by doing the following steps: refresh -> login -> ENTER \'ALL\' DETAILS AGAIN WITH THE CHANGED DETAIL -> submit .')
    

    #checking if profile alrealy filled
    if st.session_state['fullname']!="":
        st.session_state['profile_submit']==True

    if  st.session_state['profile_submit']==True:
        content3.text_input("Username:",value=st.session_state['username'],disabled=True)
        content4.text_input("Fullname:",value=st.session_state['fullname'],disabled=True)
        content5.text_input("Company Name:",value=st.session_state['company_name'],disabled=True)
        content6.text_area("Company Address:",value=st.session_state['company_add'],disabled=True)
        content7.text_input("E-mail:",value=st.session_state['e-mail'],disabled=True)
        content8.text_input("Phone no. 1:",value=st.session_state['phone no. 1'],disabled=True)
        content9.text_input("Phone No. 2:",value=st.session_state['phone no. 2'],disabled=True)
    else:
        content3.text_input("Username:",value=st.session_state['username'],disabled=True)
        val1=content4.text_input("Fullname:",placeholder="<firstname> <middlename> <lastname>")
        st.session_state['fullname']=val1
        val2=content5.text_input("Company Name:",placeholder="<company name>")
        st.session_state['company_name']=val2
        val3=content6.text_area("Company Address:",placeholder="<company address>, <city> - <pin code>")
        st.session_state['company_add']=val3
        val4=content7.text_input("E-mail:",placeholder="<email>@<gmail>.com  (you can use a different e-mail than username)")
        st.session_state['e-mail']=val4
        val5=content8.text_input("Phone no. 1:",placeholder="XXXXXXXXXX {10 digits}")
        st.session_state['phone no. 1']=val5
        val6=content9.text_input("Phone No. 2:",placeholder="XXXXXXXXXX {10 digits}")
        st.session_state['phone no. 2']=val6

        #if content10.button('submit') and isValid_input(val1,val2,val3,val4,val5,val6)==0:
        if content10.button('submit') and (val1 and val2 and val3 and val4 and val5 and val6) :
            check=isValid_input(val1,val2,val3,val4,val5,val6)
            if check==0:
                st.session_state['profile_submit']=True
                content11.success('Submitted details successfully.')
                update_user_details(val2,val3,val1,val4,val5,val6)
                content10.write("")

            elif check==1:
                content11.warning('Kindly enter "correct format of full name" to submit.(Should have space " ") ')
            elif check==2:
                content11.warning('Kindly enter "correct format of company address" to submit.(Should have symbols  "," and "-") ')
            elif check==3:
                content11.warning('Kindly enter "correct email address" to submit.(Should have expressions "@" and ".com") ')
            elif check==4:
                content11.warning('Kindly enter "correct no. of digits for \'phone no.1\' and for \'phone no.2\' to submit.(Should have "10 digits" for both) ')
            elif check==5:
                content11.warning('Kindly enter "only digits for \'phone no.1\' " to submit. ')
            elif check==6:
                content11.warning('Kindly enter "only digits for \'phone no.2\' " to submit. ')

        else:
            content11.warning('Kindly enter all details to submit.')
            
            

#6-online churn analysis
def nav_online():
    content3.write(" ")
    st.title('Telecom Churn Prediction App')
    st.write('---')

    name = st.text_input('Enter your name:')
    st.subheader(f'Hi {name},')
    st.markdown(f'''The Telecom Churn Prediction App is used to detect whether a Customer will Churn or not Churn based on his behavior and features. 

            Here, the user has to select the relevant options below to generate results. The generated results are predicted by the 

            trained model with confidence levels, these predictions are made after training the model with the attributes and 

            characteristics of Churners & Non-Churners.''')
    data = pd.read_csv("tel_churn.csv")
    #predict_online()        

    
    gender = st.radio('Select your Gender:', ('Male', 'Female'))

    senior_citizen = st.radio('Are you a Senior Citizen?', ('No', 'Yes'))

    partner = st.radio('Do you have a partner?', ('Yes', 'No'))

    dependents = st.radio('Do you have any dependents?', ('Yes', 'No'))
    phone_service = st.radio('Do you use phone services?', ('Yes', 'No'))
    multiple_lines = st.radio('Do you use multiple lines?', ('Yes', 'No'))
    internet_service = st.radio('What mode do you use to access internet services?', ( 'DSL', 'Fiber optic','No'))
    online_security = st.radio('Do you use online security?', ('Yes', 'No'))
    online_backup = st.radio('Do you use online backup?', ('Yes', 'No'))
    device_protection = st.radio('Do you use device protection?', ('Yes', 'No'))
    tech_support = st.radio('Do you use tech support?', ('Yes', 'No'))
    streaming_tv = st.radio('Do you use streaming services on TV?', ('Yes', 'No'))
    streaming_movies = st.radio('Do you steam movies?', ('Yes', 'No'))
    paperless_billing = st.radio('Do you use paperless billing?', ('Yes', 'No'))
    contract = st.selectbox("What type of Contract Term are you subscribed?",['Month-to-month', 'One year', 'Two year'])
    st.success(f"Contract Type - {contract}")
    monthly_charges = st.slider('Monthly Charges (USD)', min(data['MonthlyCharges']), max(data["MonthlyCharges"]))
    total_charges = st.slider('Total Charges (USD)', min(data['TotalCharges']), max(data["TotalCharges"]))
    payment_method = st.selectbox("What type of payment method do you use :",['Electronic check', 'Mailed check', 'Bank transfer (automatic)','Credit card (automatic)'])
    tenure_group = st.selectbox("How many months have you been using the services?", ['1 - 12', '13 - 24', '25 - 36', '37 - 48', '61 - 72', '49 - 60'], help = 'Tenure')
    input = [[gender, senior_citizen, partner, dependents, phone_service, multiple_lines, internet_service, online_security,

                online_backup, device_protection, tech_support, streaming_tv, streaming_movies, contract, paperless_billing, 

                payment_method, monthly_charges, total_charges,tenure_group]]

    cols = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService','MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',

                'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',

                'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges',

                'TotalCharges','tenure_group']
# creating a dataframe for inputs

    predictor = pd.DataFrame(input, columns=cols)

    if(st.button('Predict')):

        preprocess_predictor(predictor)

#5-batch churn analysis
def nav_batch():
    
    risk=[]

    file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])

    if file_upload is not None:

        df = pd.read_csv(file_upload)
        df.drop("Churn",inplace=True,axis=1)       

        if(st.button('Predict')):

            for i in range(1,len(df)-1):

                predictor=df.iloc[i:i+1,1:]

                sb=preprocess_predictor_batch(predictor)

                if(sb==1):

                    risk.append(df['customerID'][i])

            st.write('''### Number of Potentially Churning Customers''')

            st.write('''There are **{} customers** at risk of closing their accounts.'''.format(len(risk)))            

            dict={'cid':risk}

            csv = pd.DataFrame(dict).to_csv()

            b64 = base64.b64encode(csv.encode()).decode()

            st.write('''''')
            st.write('''''')
            st.write('''### **Download Customer Id's at Risk⬇**''')

            href = f'<a href="data:file/csv;base64,{b64}" download="CHURN_CUSTOMERID.csv">CSV File(Download)</a>'

            st.write(href, unsafe_allow_html=True)
            st.write(risk)


#main
init()
web_name.title("CHURNLYTICAL")
side_logo.image(logo,width=350)
side_details.caption("CONTACT:-  Email: churnlytical@gmail.com; Support-email: support.churnlytical@gmail.com; Phone no.: 1233459876")
menu=["Home","Login","SignUp"]
choice = side.selectbox("Login Menu",menu)
if choice =="Home":
    intro()
elif choice == "Login":
    login()
elif choice == "SignUp":
    signup()
        