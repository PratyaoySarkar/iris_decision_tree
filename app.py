import streamlit as st
import pickle as pkl
model = pkl.load(open('dt_model.pkl','rb'))
st.title("Irirs Classififcation using Decision Tree")
sl = st.number_input('Sepal Length')
sw = st.number_input('Sepal Width')
pl = st.number_input('Petal Length')
pw = st.number_input('Petal width')
def prediction(sl,sw,pl,pw):
    value = model.predict([[sl,sw,pl,pw]])
    if value[0] == 0:
        return 'Iris-setosa'
    elif value[0] == 1:
        return 'Iris-versiculor'
    else:
        return 'Iris-virginica'
if st.button('predict'):
    output = prediction(sl,sw,pl,pw)
    st.write(f'Predicted class: {output}')
