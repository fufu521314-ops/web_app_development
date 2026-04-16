from flask import Blueprint, render_template

bp = Blueprint('history', __name__, url_prefix='/history')

@bp.route('/', methods=['GET'])
def index():
    """
    歷史紀錄列表。
    輸入：無
    處理邏輯：驗證登入狀態，呼叫 Record.get_by_user_id()。
    輸出：渲染 history.html
    """
    pass

@bp.route('/<int:id>', methods=['GET'])
def detail(id):
    """
    歷史紀錄詳情。
    輸入：紀錄 ID
    處理邏輯：確認資料屬於該登入使用者，呼叫 Record.get_by_id()。
    輸出：渲染 result.html 作為歷程顯示
    """
    pass
