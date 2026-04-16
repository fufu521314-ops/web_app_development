# 路由設計文件 (API Design)

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| --- | --- | --- | --- | --- |
| 首頁 | GET | `/` | `templates/index.html` | 系統入口與功能導覽 |
| 註冊頁面 | GET | `/auth/register` | `templates/login.html` | 顯示註冊表單（可與登入同頁） |
| 執行註冊 | POST | `/auth/register` | — | 接收註冊表單，存入 DB，重導向至登入或首頁 |
| 登入頁面 | GET | `/auth/login` | `templates/login.html` | 顯示登入表單 |
| 執行登入 | POST | `/auth/login` | — | 驗證帳密，將 user_id 寫入 session |
| 登出 | POST | `/auth/logout` | — | 清除 session，重導向至首頁 |
| 抽籤頁面 | GET | `/fortune/draw` | `templates/draw_lots.html` | 顯示抽籤與擲筊互動頁面 |
| 執行抽籤 | POST | `/fortune/draw` | — | 隨機產生籤號，若已登入則存成紀錄，重導向至結果頁 |
| 籤詩結果 | GET | `/fortune/result/<id>` | `templates/result.html` | 顯示抽籤結果與解籤說明 |
| 歷史紀錄 | GET | `/history/` | `templates/history.html` | 列出該使用者的所有算命歷史紀錄 |
| 紀錄詳情 | GET | `/history/<id>` | `templates/result.html` | 查看特定一筆算命紀錄詳情（共用結果頁模板） |
| 捐獻頁面 | GET | `/payment/donate` | `templates/donate.html` | 填寫添香油錢表單頁面 |
| 執行捐獻 | POST | `/payment/donate` | — | 存入 Donation 模型，跳出感謝訊息並重導向 |

## 2. 每個路由的詳細說明

### 首頁模組 (`main.py`)
- **GET `/`**
  - **輸入**：無
  - **處理邏輯**：判斷是否登入。
  - **輸出**：渲染 `index.html`。
  - **錯誤處理**：無。

### 認證模組 (`auth.py`)
- **GET `/auth/register`**
  - **輸出**：渲染 `login.html` (表單開關切換為註冊態)。
- **POST `/auth/register`**
  - **輸入**：表單欄位 (`username`, `email`, `password`, `confirm_password`)。
  - **處理邏輯**：驗證輸入，確認電子郵件未重複後，將密碼雜湊並呼叫 `User.create()`。
  - **輸出**：重導向至 `/auth/login` 或自動登入回到首頁。
- **GET `/auth/login`**
  - **輸出**：渲染 `login.html`。
- **POST `/auth/login`**
  - **輸入**：表單欄位 (`email`, `password`)。
  - **處理邏輯**：呼叫 `User.get_by_email()`，驗證密碼，若正確則設定 `session['user_id']`。
  - **輸出**：重導向至首頁 (`/`)。
- **POST `/auth/logout`**
  - **處理邏輯**：清除 `session` 中的 `user_id`。
  - **輸出**：重導向至首頁。

### 算命模組 (`fortune.py`)
- **GET `/fortune/draw`**
  - **輸出**：渲染 `draw_lots.html`，供使用者進行互動操作。
- **POST `/fortune/draw`**
  - **處理邏輯**：隨機抽出一支籤。若 `session` 內有登入資訊，則呼叫 `Record.create()` 寫入歷程。
  - **輸出**：重導向至 `/fortune/result/<lot_id>`（若是已紀錄，則可以帶上紀錄 id）。
- **GET `/fortune/result/<id>`**
  - **輸入**：URL 參數 `id`（籤詩 ID 或紀錄 ID）。
  - **處理邏輯**：呼叫 `Lot.get_by_id()` 獲取資料。
  - **輸出**：渲染 `result.html`。

### 歷史紀錄模組 (`history.py`)
- **GET `/history/`**
  - **處理邏輯**：確認有 `session['user_id']`，呼叫 `Record.get_by_user_id()` 獲取清單。
  - **輸出**：渲染 `history.html`。
- **GET `/history/<id>`**
  - **輸入**：URL 參數 `id` (紀錄 ID)。
  - **處理邏輯**：呼叫 `Record.get_by_id()`，確認資料夾屬於目前登入使用者。
  - **輸出**：渲染 `result.html` 或特定的頁面顯示該次結果。

### 捐款模組 (`payment.py`)
- **GET `/payment/donate`**
  - **輸出**：渲染 `donate.html`。
- **POST `/payment/donate`**
  - **輸入**：表單欄位 (`amount`, `message`)。
  - **處理邏輯**：呼叫 `Donation.create()` 將資料存入資料庫（帶入 `user_id` 如果有登入）。
  - **輸出**：重導向至首頁並帶放 `感謝您的支持` 的 flash 訊息。

## 3. Jinja2 模板清單

所有的 HTML 檔案皆放於 `app/templates/`。
- `base.html`：包含 HTML `<head>`，共用的 Navbar、Footer 與提示訊息 (flash messages)。
- `index.html`：繼承 `base.html`，首頁外觀及功能入口。
- `login.html`：繼承 `base.html`，包含登入與註冊之表單介面。
- `draw_lots.html`：繼承 `base.html`，含抽籤與擲筊的視覺互動與特效。
- `result.html`：繼承 `base.html`，顯示抽中的籤詩排版以及解說。可用於單次抽籤結果或是歷史紀錄的詳細閱覽。
- `history.html`：繼承 `base.html`，用表格或卡片列表呈現使用者的過往算命總覽。
- `donate.html`：繼承 `base.html`，提供選擇或填寫捐款金額的結帳介面。
