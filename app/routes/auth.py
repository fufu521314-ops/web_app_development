from flask import Blueprint, render_template

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    註冊處理。
    輸入：表單資料 (username, email, password, confirm_password)
    處理邏輯：驗證輸入，確認電子郵件未重複後，建立 User。
    輸出：GET 渲染 login.html，POST 重導向至登入或首頁
    """
    pass

@bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    登入處理。
    輸入：表單資料 (email, password)
    處理邏輯：驗證帳密，設定 session['user_id']。
    輸出：GET 渲染 login.html，POST 重導向至首頁
    """
    pass

@bp.route('/logout', methods=['POST'])
def logout():
    """
    登出處理。
    處理邏輯：清除 session 中的 user_id。
    輸出：重導向至首頁
    """
    pass
