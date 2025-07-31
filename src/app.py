import datetime

import humanize
import streamlit as st

from Currency_exchange import convert_currency, get_exchange_rate
from currencylist import clist

st.markdown("# :moneybag:  Exchange Currency")
st.markdown("### Here you can exchange your currency into another countries currency!\n  ### Beside you can have the amount of your base currency into anther ! :money_mouth_face:")
st.write("")

base_currency = st.selectbox("From currency (Base)", clist)
target_currency = st.selectbox("To currency (Target)", clist)
amount = st.number_input("Enter amount: ", min_value= 0.0 , value=100.00 ,max_value=1000000.00)
exchange = st.button("Exchange")




if exchange :
    if amount > 0 and base_currency and target_currency:
        exchange_rate,time_last_updated = get_exchange_rate(base_currency=base_currency, target_currency=target_currency)
        time_diff = datetime.datetime.now() - datetime.datetime.fromtimestamp(time_last_updated)
        # Use humanize to format the time difference
        time_ago = humanize.naturaltime(time_diff)


        if exchange_rate:
            converted_amount = convert_currency(amount=amount, exchange_rate=exchange_rate)
            st.success(f":white_check_mark: Exchange Rate : {exchange_rate:.2f} (Last updated: {time_ago})")

            col1, col2, col3 = st.columns(3)
            col1.metric(label="Base Currency", value=f"{amount:.2f} {base_currency}")
            col2.markdown("<h1 style='text-align: center; margin: 0; color: green;'>&#8594;</h1>", unsafe_allow_html=True)
            col3.metric(label="Target Currency", value=f"{converted_amount:.2f} {target_currency}")

        else:
            st.error("Eror fetching excahnge rate.")

st.markdown("---")
st.markdown("### ℹ️ About This Tool")
st.markdown("""
This currency converter uses real-time exchange rates provided by the ExchangeRate-API.
- The conversion updates automatically as you input the amount or change the currency.
- Enjoy seamless currency conversion without the need to press a button!
""")
