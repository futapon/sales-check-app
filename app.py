import streamlit as st
import re

st.title("📱 売上チェックアプリ（スマホ対応）")

# 数値をカンマ区切りで入力 → 合計を出す関数
def get_sum(label):
    raw = st.text_input(label, "")
    try:
        # カンマやスペースで区切る:正規表記 r"[,\s]+"
        values = re.split(r"[,\s]+", raw.strip())
        return sum(float(v) for v in values if v)
    except:
        return 0.0

# 入力欄
total_customers = get_sum("1. 総客数（例: 400,300）")
cash_sales = get_sum("2. 現金売上")
credit_sales = get_sum("3. クレジットの総和")
electronic_payments = get_sum("4. 電子支払い")
code_payments = get_sum("5. コード支払い")
house_tickets = get_sum("6. ハウスマネー・優待券の和")
gift_coupons = get_sum("7. 金券の和")
net_sales = get_sum("8. 総売り上げ（税抜き）")
tax = get_sum("9. 消費税")
sales_deduction = 0  # 固定
gross_sales = get_sum("11. 総売り上げ（税込み）")

# 計算ボタン
if st.button("✅ チェック実行"):
    total_sum = (
        cash_sales
        + credit_sales
        + electronic_payments
        + code_payments
        + house_tickets
        + gift_coupons
    )

    result_check = total_sum - tax
    difference = result_check - gross_sales

    st.markdown("### 🧾 計算結果")
    st.write(f"合計チェック額（税抜き＋各種売上 − 税）: {result_check:,}円")
    st.write(f"総売上（税込み）: {gross_sales:,}円")
    st.write(f"差額: {difference:,}円")

    if abs(difference) < 0.01:
        st.success("✅ 完全一致！問題ありません。")
    else:
        st.error("⚠ 差額あり！入力ミスまたは未計上の可能性があります。")
    

#全入力の再表示（１～１１）整数で表示
st.markdown("###📋 入力値の確認")
st.write(f"1.総客数:{int(total_customers):,}")
st.write(f"2.現金売上:{int(cash_sales):,}")
st.write(f"3.クレジットの総和:{int(credit_sales):,}")
st.write(f"4.電子支払い:{int(electronic_payments):,}")
st.write(f"5.コード支払い:{int(code_payments):,}")
st.write(f"6.ハウスマネー・優待券:{int(house_tickets):,}")
st.write(f"7.金券:{int(gift_coupons):,}")
st.write(f"8.総売り上げ:{int(net_sales):,}")
st.write(f"9.消費税:{int(tax):,}")
st.write(f"10.売上控除:{sales_deduction}")
st.write(f"11.総売上(税込み):{int(gross_sales):,}")
