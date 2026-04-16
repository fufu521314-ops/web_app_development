from flask import Blueprint, render_template

bp = Blueprint('fortune', __name__, url_prefix='/fortune')

@bp.route('/draw', methods=['GET', 'POST'])
def draw_lots():
    """
    抽籤頁面與執行。
    輸入：無 (GET) / 可能有擲筊參數 (POST)
    處理邏輯：隨機抽出一支籤，若有登入則呼叫 Record.create()。
    輸出：GET 渲染 draw_lots.html，POST 重導向至 /fortune/result/<lot_id>
    """
    pass

@bp.route('/result/<int:id>', methods=['GET'])
def result(id):
    """
    籤詩結果。
    輸入：籤詩 ID (或紀錄 ID)
    處理邏輯：呼叫 Lot.get_by_id() 獲取籤詩資料。
    輸出：渲染 result.html
    """
    pass
