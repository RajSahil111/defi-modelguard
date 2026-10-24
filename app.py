import streamlit as st

st.set_page_config(
    page_title="DeFi ModelGuard",
    page_icon="🛡️",
    layout="centered"
)

st.title("DeFi ModelGuard")
st.subheader("Financial Logic Verification for DeFi")

st.write(
    "Test basic DeFi collateral rules and compare financial results "
    "with your expected requirements."
)

st.warning(
    "Educational prototype only. This is not a complete smart-contract audit."
)

st.header("1. Collateral Ratio Checker")

collateral = st.number_input(
    "Collateral value (USD)",
    min_value=0.0,
    value=1500.0,
    step=100.0
)

debt = st.number_input(
    "Debt amount (USD)",
    min_value=0.0,
    value=750.0,
    step=50.0
)

minimum_ratio = st.number_input(
    "Required collateral ratio (%)",
    min_value=100.0,
    value=150.0,
    step=10.0
)

if st.button("Verify Financial Model"):
    if debt <= 0:
        st.error("Debt must be greater than zero.")
    else:
        actual_ratio = collateral / debt * 100
        maximum_safe_debt = collateral / (minimum_ratio / 100)

        st.metric(
            "Maximum debt at required collateral ratio",
            f"${maximum_safe_debt:,.2f}"
        )

        st.metric(
            "Actual collateral ratio",
            f"{actual_ratio:.2f}%"
        )

        if actual_ratio >= minimum_ratio:
            st.success("PASS: The collateral ratio meets the requirement.")
        else:
            st.error("FAIL: The collateral ratio is below the requirement.")

st.header("2. Solidity Code Input")

solidity_code = st.text_area(
    "Paste Solidity code here",
    placeholder="pragma solidity ...",
    height=180
)

if st.button("Check Solidity Input"):
    if "pragma solidity" in solidity_code:
        st.info(
            "A Solidity version declaration was detected. "
            "This is a text check only, not a security audit."
        )
    elif solidity_code.strip():
        st.warning("No Solidity version declaration was detected.")
    else:
        st.info("Paste Solidity code first.")
