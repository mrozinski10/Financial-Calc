import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(
    page_title="Savings Annuity Calculator")

st.title("Savings Annuity Calculator")

st.header("Solving for future value:")
colInput1, colInput2 = st.beta_columns(2)

with colInput1:
    st.subheader("Payment")
    pmt1 = st.number_input("Enter the payment amount: ", min_value=0.0, format='%f')

    st.subheader("Number of annual payments")
    k1 = st.number_input("Enter the number of payments per year: ", min_value=0.0, format='%f')

with colInput2:
    st.subheader("Interest rate")
    r1 = st.number_input("Enter the annual percentage rate (as a decimal): ", min_value=0.0, format='%f')

    st.subheader("Time")
    t1 = st.number_input("Enter the number of number of years: ", min_value=0.0, format='%f')

st.header("Future Value")
if k1 != 0:
    fv1 = pmt1*(((1+r1/k1)**(k1*t1))-1)/(r1/k1)
    fvr1 = round(fv1,2)
    fvf1 = "{:,}".format(fvr1)
    st.subheader("The future value of the account is $" + str(fvf1))

    x_value = np.arange(t1+1)
    y_value = list()
    for t in x_value:
        y_value.append(pmt1*(((1+r1/k1)**(k1*t))-1)/(r1/k1))
    y_value = tuple(y_value)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=x_value,
            y=y_value,
            name="Account Value"
        )
    )
    fig.update_layout(title='Account Value Over Time',
                      xaxis_title='Year',
                      yaxis_title='Amount($)')

    st.plotly_chart(fig, use_container_width=True)