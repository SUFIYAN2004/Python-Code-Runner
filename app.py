import streamlit as st
import io
import contextlib

st.title("Python Code Runner")
code = st.text_area("Enter the python code here: ")

if st.button("Run code"):
    output_buffer = io.StringIO()
    try:
        with contextlib.redirect_stdout(output_buffer):
            exec(code, {})
            output = output_buffer.getvalue()
            st.success("Code executed Successfully!")
            st.code(output, language="python")
    except Exception as e:
        st.error(f"Erorr {e}") #https://github.com/SUFIYAN2004/Python-Code-Runner-Run-Python-Code-in-the-Browser-with-Streamlit-exec-.git