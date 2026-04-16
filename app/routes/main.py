from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """
    首頁。
    輸入：無
    處理邏輯：判斷是否登入。
    輸出：渲染 index.html
    """
    pass
