import streamlit as st
from BankGUI import (
    create_account, deposit, withdraw,
    get_account, update_account, delete_account, transfer
)

# ─────────────────────────────────────────────
#  Page config
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Best Bank",
    page_icon="🏦",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
#  Global CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* ── Background ── */
.stApp {
    background: #0a0f1e;
    color: #e8eaf6;
}

/* ── Hero banner ── */
.hero {
    background: linear-gradient(135deg, #1a237e 0%, #0d47a1 50%, #01579b 100%);
    border-radius: 16px;
    padding: 36px 32px 28px;
    margin-bottom: 28px;
    text-align: center;
    border: 1px solid #1e3a5f;
}
.hero h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.2rem;
    font-weight: 700;
    color: #ffffff;
    margin: 0 0 6px;
    letter-spacing: -0.5px;
}
.hero p {
    color: #90caf9;
    font-size: 1rem;
    margin: 0;
    font-weight: 400;
}

/* ── Cards ── */
.card {
    background: #111827;
    border: 1px solid #1e3a5f;
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 16px;
}

/* ── Balance pill ── */
.balance-pill {
    background: linear-gradient(135deg, #0d47a1, #1565c0);
    border-radius: 12px;
    padding: 20px 24px;
    text-align: center;
    margin: 12px 0;
}
.balance-pill .label {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #90caf9;
    margin-bottom: 4px;
}
.balance-pill .amount {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.2rem;
    font-weight: 700;
    color: #ffffff;
}

/* ── Transaction rows ── */
.txn-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0;
    border-bottom: 1px solid #1e3a5f;
    font-size: 0.88rem;
}
.txn-row:last-child { border-bottom: none; }
.txn-type { color: #90caf9; }
.txn-credit { color: #4caf50; font-weight: 600; }
.txn-debit  { color: #ef5350; font-weight: 600; }
.txn-time   { color: #546e7a; font-size: 0.78rem; }

/* ── Streamlit widgets overrides ── */
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input,
[data-testid="stSelectbox"] select {
    background: #1a2235 !important;
    border: 1px solid #2a4a7f !important;
    color: #e8eaf6 !important;
    border-radius: 8px !important;
}
.stButton > button {
    background: linear-gradient(135deg, #1565c0, #0d47a1) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    padding: 0.55rem 1.4rem !important;
    transition: opacity 0.2s;
}
.stButton > button:hover { opacity: 0.88; }
.stTabs [data-baseweb="tab-list"] {
    background: #111827;
    border-radius: 10px;
    gap: 4px;
    padding: 4px;
}
.stTabs [data-baseweb="tab"] {
    background: transparent;
    color: #90caf9;
    border-radius: 8px;
    font-size: 0.85rem;
    font-weight: 500;
}
.stTabs [aria-selected="true"] {
    background: #1565c0 !important;
    color: #fff !important;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  Hero
# ─────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>🏦 BestPay Bank</h1>
    <p>Secure · Simple · Modern Banking</p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  Tabs
# ─────────────────────────────────────────────
tabs = st.tabs([
    "➕ Open Account",
    "💰 Deposit",
    "💸 Withdraw",
    "🔁 Transfer",
    "📋 My Account",
    "✏️ Update",
    "🗑️ Close Account",
])

# ════════════════════════════════════════════
#  TAB 1 — Create Account
# ════════════════════════════════════════════
with tabs[0]:
    st.subheader("Open a New Account")
    with st.form("create_form"):
        col1, col2 = st.columns(2)
        with col1:
            name  = st.text_input("Full Name")
            email = st.text_input("Email Address")
            pin   = st.text_input("4-Digit PIN", type="password", max_chars=4)
        with col2:
            age             = st.number_input("Age", min_value=1, max_value=120, step=1, value=18)
            initial_deposit = st.number_input("Initial Deposit (Rs.)", min_value=0.0, step=100.0)
            pin_confirm     = st.text_input("Confirm PIN", type="password", max_chars=4)

        submitted = st.form_submit_button("Open Account", use_container_width=True)
        if submitted:
            if not name or not email:
                st.error("Name and email are required.")
            elif pin != pin_confirm:
                st.error("PINs do not match.")
            else:
                ok, msg, user = create_account(name, int(age), email, pin, initial_deposit)
                if ok:
                    st.success(msg)
                    st.markdown(f"""
                    <div class="card">
                        <b>Account Number:</b> <code style="font-size:1.1rem;color:#4fc3f7">{user['account_no']}</code><br>
                        <small style="color:#90caf9">Save this — you'll need it to log in.</small>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error(msg)

# ════════════════════════════════════════════
#  TAB 2 — Deposit
# ════════════════════════════════════════════
with tabs[1]:
    st.subheader("Deposit Money")
    with st.form("deposit_form"):
        acc = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password", max_chars=4)
        amt = st.number_input("Amount (Rs.)", min_value=1.0, step=100.0)
        if st.form_submit_button("Deposit", use_container_width=True):
            ok, msg, user = deposit(acc.strip(), pin, amt)
            if ok:
                st.success(msg)
                st.markdown(f"""
                <div class="balance-pill">
                    <div class="label">New Balance</div>
                    <div class="amount">Rs. {user['balance']:,.2f}</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error(msg)

# ════════════════════════════════════════════
#  TAB 3 — Withdraw
# ════════════════════════════════════════════
with tabs[2]:
    st.subheader("Withdraw Money")
    with st.form("withdraw_form"):
        acc = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password", max_chars=4)
        amt = st.number_input("Amount (Rs.)", min_value=1.0, step=100.0)
        if st.form_submit_button("Withdraw", use_container_width=True):
            ok, msg, user = withdraw(acc.strip(), pin, amt)
            if ok:
                st.success(msg)
                st.markdown(f"""
                <div class="balance-pill">
                    <div class="label">Remaining Balance</div>
                    <div class="amount">Rs. {user['balance']:,.2f}</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error(msg)

# ════════════════════════════════════════════
#  TAB 4 — Transfer
# ════════════════════════════════════════════
with tabs[3]:
    st.subheader("Transfer Funds")
    with st.form("transfer_form"):
        acc      = st.text_input("Your Account Number")
        pin      = st.text_input("Your PIN", type="password", max_chars=4)
        recv_acc = st.text_input("Recipient Account Number")
        amt      = st.number_input("Amount (Rs.)", min_value=1.0, step=100.0)
        if st.form_submit_button("Transfer", use_container_width=True):
            ok, msg = transfer(acc.strip(), pin, recv_acc.strip(), amt)
            (st.success if ok else st.error)(msg)

# ════════════════════════════════════════════
#  TAB 5 — Account Details
# ════════════════════════════════════════════
with tabs[4]:
    st.subheader("Account Details")
    with st.form("details_form"):
        acc = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password", max_chars=4)
        if st.form_submit_button("View Details", use_container_width=True):
            ok, msg, user = get_account(acc.strip(), pin)
            if ok:
                st.markdown(f"""
                <div class="balance-pill">
                    <div class="label">Available Balance</div>
                    <div class="amount">Rs. {user['balance']:,.2f}</div>
                </div>
                """, unsafe_allow_html=True)

                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"**👤 Name:** {user['name']}")
                    st.markdown(f"**📧 Email:** {user['email']}")
                with col2:
                    st.markdown(f"**🎂 Age:** {user['age']}")
                    st.markdown(f"**📅 Joined:** {user.get('created_at', 'N/A')}")

                # Transaction history
                txns = user.get("transactions", [])
                if txns:
                    st.markdown("#### 📄 Transaction History")
                    rows = ""
                    for t in reversed(txns[-20:]):
                        is_credit = "Deposit" in t["type"] or "Transfer In" in t["type"] or "Initial" in t["type"]
                        sign  = "+" if is_credit else "−"
                        cls   = "txn-credit" if is_credit else "txn-debit"
                        rows += f"""
                        <div class="txn-row">
                            <span class="txn-type">{t['type']}</span>
                            <span class="{cls}">{sign} Rs. {t['amount']:,.2f}</span>
                            <span class="txn-time">{t['timestamp']}</span>
                        </div>
                        """
                    st.markdown(f'<div class="card">{rows}</div>', unsafe_allow_html=True)
                else:
                    st.info("No transactions yet.")
            else:
                st.error(msg)

# ════════════════════════════════════════════
#  TAB 6 — Update Details
# ════════════════════════════════════════════
with tabs[5]:
    st.subheader("Update Account Details")
    st.caption("Leave a field empty to keep the existing value.")
    with st.form("update_form"):
        acc       = st.text_input("Account Number")
        pin       = st.text_input("Current PIN", type="password", max_chars=4)
        new_name  = st.text_input("New Name (optional)")
        new_email = st.text_input("New Email (optional)")
        col1, col2 = st.columns(2)
        with col1:
            new_pin = st.text_input("New PIN (optional)", type="password", max_chars=4)
        with col2:
            new_pin_confirm = st.text_input("Confirm New PIN", type="password", max_chars=4)

        if st.form_submit_button("Update Account", use_container_width=True):
            if new_pin and new_pin != new_pin_confirm:
                st.error("New PINs do not match.")
            else:
                ok, msg = update_account(
                    acc.strip(), pin,
                    new_name  or None,
                    new_email or None,
                    new_pin   or None,
                )
                (st.success if ok else st.error)(msg)

# ════════════════════════════════════════════
#  TAB 7 — Delete Account
# ════════════════════════════════════════════
with tabs[6]:
    st.subheader("Close Account")
    st.warning("⚠️ This action is permanent and cannot be undone.")
    with st.form("delete_form"):
        acc     = st.text_input("Account Number")
        pin     = st.text_input("PIN", type="password", max_chars=4)
        confirm = st.checkbox("I understand this will permanently delete my account and all data.")
        if st.form_submit_button("Close Account", use_container_width=True):
            if not confirm:
                st.error("Please check the confirmation box to proceed.")
            else:
                ok, msg = delete_account(acc.strip(), pin)
                (st.success if ok else st.error)(msg)

# ─────────────────────────────────────────────
#  Footer
# ─────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;margin-top:40px;color:#37474f;font-size:0.8rem;">
    NovaPay Bank · Secure Banking System · Built with Streamlit
</div>
""", unsafe_allow_html=True)