from flask import Blueprint, render_template

bp = Blueprint('payment', __name__, url_prefix='/payment')

@bp.route('/donate', methods=['GET', 'POST'])
def donate():
    """
    線上添香油錢。
    輸入：表單資料 (amount, message)
    處理邏輯：呼叫 Donation.create()。
    輸出：GET 渲染 donate.html，POST 重導向並發送感謝訊息
    """
    pass
