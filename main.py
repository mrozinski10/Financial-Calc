import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(
    page_title="Savings Annuity Calculator")

st.title("Savings Annuity Calculator")

st.header("Solving for future value:")
colInput1, colInput2 = st.beta_columns(2)

with colInput1:
    st.subheader("Payment/Deposit")
    pmt1 = st.number_input("Enter the payment amount: ", min_value=0.0, format='%f')

    st.subheader("Number of annual payments")
    k1 = st.number_input("Enter the number of payments/deposits per year: ", min_value=0.0, format='%f')

with colInput2:
    st.subheader("Interest rate")
    r1 = st.number_input("Enter the annual percentage rate (as a decimal): ", min_value=0.0, format='%f')

    st.subheader("Time")
    t1 = st.number_input("Enter the years: ", min_value=0.0, format='%f')

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

st.text("")
st.text("")

st.header("Solving for payment/deposit amount:")
colInput3, colInput4 = st.beta_columns(2)

with colInput3:
    st.subheader("Future Value")
    fv2 = st.number_input("Enter the future value amount: ", min_value=0.0, format='%f')

    st.subheader("Number of annual payments")
    k2 = st.number_input("Enter the number of payments per year:", min_value=0.0, format='%f')

with colInput4:
    st.subheader("Interest rate")
    r2 = st.number_input("Enter the percentage rate (as a decimal): ", min_value=0.0, format='%f')

    st.subheader("Time")
    t2 = st.number_input("Enter the number of years: ", min_value=0.0, format='%f')

st.header("Payment/Deposit Amount")
if k2 != 0 and t2!=0:
    pmt2 = fv2*(r2/k2)/(((1+r2/k2)**(k2*t2))-1)
    pmtr2 = round(pmt2,2)
    pmtf2 = "{:,}".format(pmtr2)
    st.subheader("The Payment/Deposit amount required is $" + str(pmtf2))

st.text("")
st.text("")
st.text("")
st.text("")

st.title("Payout Annuity/Loans Calculator")

st.header("Solving for present value/loan amount:")

colInput5, colInput6 = st.beta_columns(2)

with colInput5:
    st.subheader("Payment/Deposit")
    pmt3 = st.number_input("Enter withdrawal/payment amount: ", min_value=0.0, format='%f')

    st.subheader("Annual withdrawals/payments")
    k3 = st.number_input("Enter the number of withdrawals/payments per year: ", min_value=0.0, format='%f')

with colInput6:
    st.subheader("Interest rate")
    r3 = st.number_input("Enter the annual interest rate (as a decimal): ", min_value=0.0, format='%f')

    st.subheader("Time")
    t3 = st.number_input("Enter amount of years: ", min_value=0.0, format='%f')

st.header("Future Value")
if k3 != 0:
    pv1 = pmt3*(1-((1+r3/k3)**(-k3*t3)))/(r3/k3)
    pvr1 = round(pv1,2)
    pvf1 = "{:,}".format(pvr1)
    st.subheader("The present value of the account/loan is $" + str(pvf1))

    y_value2 = list()
    x_value2 = np.arange(t3*k3 + 1)
    for t in x_value2:
        pv1 = pv1+pv1*(r3/k3)-pmt3
        y_value2.append(pv1)
    y_value2 = tuple(y_value2)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=x_value2,
            y=y_value2,
            name="Account Value"
        )
    )
    fig.update_layout(title='Account Value Over Time',
                      xaxis_title='Number of Payments/Withdrawals',
                      yaxis_title='Amount($)')

    st.plotly_chart(fig, use_container_width=True)

st.text("")
st.text("")

st.header("Solving for withdrawal/payment amount:")

colInput7, colInput8 = st.beta_columns(2)

with colInput7:
    st.subheader("Initial value")
    pv2 = st.number_input("Enter the initial account/loan value : ", min_value=0.0, format='%f')

    st.subheader("Annual withdrawals/payments")
    k4 = st.number_input("Enter number of withdrawals/payments per year: ", min_value=0.0, format='%f')

with colInput8:
    st.subheader("Interest rate")
    r4 = st.number_input("Enter annual interest rate (as a decimal): ", min_value=0.0, format='%f')

    st.subheader("Time")
    t4 = st.number_input("Enter the amount of years: ", min_value=0.0, format='%f')

st.header("Future Value")
if k4 != 0 and t4 != 0:
    pmt4 = pv2*(r4/k4)/(1-((1+r4/k4)**(-k4*t4)))
    pmtr4 = round(pmt4,2)
    pmtf4 = "{:,}".format(pmtr4)
    st.subheader("The withdrawal/payment amount is $" + str(pmtf4))

    y_value3 = list()
    x_value3 = np.arange(t4*k4 + 1)
    for t in x_value3:
        pv2 = pv2+pv2*(r4/k4)-pmt4
        y_value3.append(pv2)
    y_value3 = tuple(y_value3)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=x_value3,
            y=y_value3,
            name="Account Value"
        )
    )
    fig.update_layout(title='Account Value Over Time',
                      xaxis_title='Number of Payments/Withdrawals',
                      yaxis_title='Amount($)')

    st.plotly_chart(fig, use_container_width=True)