import json
import random
import string
import hashlib
import os
from pathlib import Path
from datetime import datetime


DATABASE_FILE = "bank_data.json"


# ─────────────────────────────────────────────
#  Helpers
# ─────────────────────────────────────────────

def _hash_pin(pin: str) -> str:
    """Return SHA-256 hash of pin string."""
    return hashlib.sha256(pin.encode()).hexdigest()


def _load_data() -> list[dict]:
    try:
        if Path(DATABASE_FILE).exists():
            with open(DATABASE_FILE, "r") as f:
                return json.load(f)
    except Exception:
        pass
    return []


def _save_data(data: list[dict]) -> None:
    with open(DATABASE_FILE, "w") as f:
        json.dump(data, f, indent=2)


def _generate_account_number() -> str:
    """Generate a unique alphanumeric account ID."""
    alpha = random.choices(string.ascii_uppercase, k=3)
    digits = random.choices(string.digits, k=6)
    chars = alpha + digits
    random.shuffle(chars)
    return "".join(chars)


def _find_user(data: list[dict], account_no: str, pin: str) -> dict | None:
    hashed = _hash_pin(pin)
    matches = [u for u in data if u["account_no"] == account_no and u["pin"] == hashed]
    return matches[0] if matches else None


def _log_transaction(user: dict, txn_type: str, amount: float) -> None:
    entry = {
        "type": txn_type,
        "amount": amount,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "balance_after": user["balance"],
    }
    user.setdefault("transactions", []).append(entry)


# ─────────────────────────────────────────────
#  Core Bank Operations (pure functions)
# ─────────────────────────────────────────────

def create_account(name: str, age: int, email: str, pin: str, initial_deposit: float = 0) -> tuple[bool, str, dict | None]:
    if age < 18:
        return False, "Applicant must be at least 18 years old.", None
    if len(pin) != 4 or not pin.isdigit():
        return False, "PIN must be exactly 4 digits.", None
    if initial_deposit < 0:
        return False, "Initial deposit cannot be negative.", None

    data = _load_data()

    # Check duplicate email
    if any(u["email"].lower() == email.lower() for u in data):
        return False, "An account with this email already exists.", None

    account_no = _generate_account_number()
    # Ensure uniqueness
    while any(u["account_no"] == account_no for u in data):
        account_no = _generate_account_number()

    user = {
        "name": name.strip(),
        "age": age,
        "email": email.strip().lower(),
        "pin": _hash_pin(pin),
        "account_no": account_no,
        "balance": initial_deposit,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "transactions": [],
    }

    if initial_deposit > 0:
        _log_transaction(user, "Initial Deposit", initial_deposit)

    data.append(user)
    _save_data(data)
    return True, "Account created successfully!", user


def deposit(account_no: str, pin: str, amount: float) -> tuple[bool, str, dict | None]:
    if amount <= 0:
        return False, "Deposit amount must be greater than 0.", None
    if amount > 500_000:
        return False, "Single deposit limit is Rs. 500,000.", None

    data = _load_data()
    user = _find_user(data, account_no, pin)
    if not user:
        return False, "Invalid account number or PIN.", None

    user["balance"] += amount
    _log_transaction(user, "Deposit", amount)
    _save_data(data)
    return True, f"Rs. {amount:,.2f} deposited successfully.", user


def withdraw(account_no: str, pin: str, amount: float) -> tuple[bool, str, dict | None]:
    if amount <= 0:
        return False, "Withdrawal amount must be greater than 0.", None

    data = _load_data()
    user = _find_user(data, account_no, pin)
    if not user:
        return False, "Invalid account number or PIN.", None
    if user["balance"] < amount:
        return False, f"Insufficient balance. Available: Rs. {user['balance']:,.2f}", None

    user["balance"] -= amount
    _log_transaction(user, "Withdrawal", amount)
    _save_data(data)
    return True, f"Rs. {amount:,.2f} withdrawn successfully.", user


def get_account(account_no: str, pin: str) -> tuple[bool, str, dict | None]:
    data = _load_data()
    user = _find_user(data, account_no, pin)
    if not user:
        return False, "Invalid account number or PIN.", None
    return True, "Account found.", user


def update_account(account_no: str, pin: str, new_name: str | None, new_email: str | None, new_pin: str | None) -> tuple[bool, str]:
    data = _load_data()
    user = _find_user(data, account_no, pin)
    if not user:
        return False, "Invalid account number or PIN."

    if new_name:
        user["name"] = new_name.strip()
    if new_email:
        # Check email conflict
        conflict = [u for u in data if u["email"].lower() == new_email.lower() and u["account_no"] != account_no]
        if conflict:
            return False, "That email is already used by another account."
        user["email"] = new_email.strip().lower()
    if new_pin:
        if len(new_pin) != 4 or not new_pin.isdigit():
            return False, "New PIN must be exactly 4 digits."
        user["pin"] = _hash_pin(new_pin)

    _save_data(data)
    return True, "Account updated successfully."


def delete_account(account_no: str, pin: str) -> tuple[bool, str]:
    data = _load_data()
    user = _find_user(data, account_no, pin)
    if not user:
        return False, "Invalid account number or PIN."

    data.remove(user)
    _save_data(data)
    return True, "Account deleted successfully."


def transfer(sender_acc: str, pin: str, receiver_acc: str, amount: float) -> tuple[bool, str]:
    if amount <= 0:
        return False, "Transfer amount must be greater than 0."

    data = _load_data()
    sender = _find_user(data, sender_acc, pin)
    if not sender:
        return False, "Invalid sender account number or PIN."

    receiver = next((u for u in data if u["account_no"] == receiver_acc), None)
    if not receiver:
        return False, "Receiver account not found."
    if sender["account_no"] == receiver["account_no"]:
        return False, "Cannot transfer to your own account."
    if sender["balance"] < amount:
        return False, f"Insufficient balance. Available: Rs. {sender['balance']:,.2f}"

    sender["balance"] -= amount
    receiver["balance"] += amount
    _log_transaction(sender, f"Transfer Out → {receiver_acc}", amount)
    _log_transaction(receiver, f"Transfer In ← {sender_acc}", amount)
    _save_data(data)
    return True, f"Rs. {amount:,.2f} transferred to {receiver['name']} successfully."