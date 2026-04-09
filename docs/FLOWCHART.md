# 線上算命系統 - 流程圖文件 (Flowchart)

本文件描述了「線上算命系統」的使用者操作流程以及系統內部的資料處理流程。

## 1. 使用者流程圖 (User Flow)

下圖展示了使用者從進入網站到完成抽籤、查看紀錄及捐贈的操作路徑。

```mermaid
flowchart TD
    Start([使用者開啟網頁]) --> Home[首頁 / 歡迎頁]
    Home -->|查看功能| DrawLots[線上抽籤/占卜頁]
    Home -->|欲儲存紀錄| Login{是否已登入?}
    
    Login -- 否 --> Auth[登入 / 註冊頁]
    Auth --> Login
    Login -- 是 --> Dashboard[個人首頁 / 歷史紀錄]

    DrawLots --> Action[點擊抽籤 / 搖動手機]
    Action --> Animation[抽籤動畫 / 擲筊互動]
    Animation --> Result[顯示籤詩結果與解說]

    Result --> Save{是否登入?}
    Save -- 是 --> AutoSave[系統自動儲存結果]
    Save -- 否 --> Notice[提示登入以儲存紀錄]

    Dashboard --> History[查看過去算命紀錄]
    
    Home --> Donate[添香油錢頁面]
    Donate --> Pay[填寫金額與模擬支付]
    Pay --> Thanks[跳出感謝訊息]
```

---

## 2. 系統序列圖 (Sequence Diagram)

以「使用者進行線上抽籤」為例，展示前端、後端路由、資料模型與資料庫之間的互動。

```mermaid
sequenceDiagram
    actor User as 使用者
    participant Browser as 瀏覽器 (JS/CSS)
    participant Flask as Flask Route (fortune.py)
    participant Model as Record Model
    participant DB as SQLite

    User->>Browser: 點擊「開始抽籤」
    Browser->>Browser: 播放抽籤中動畫 (main.js)
    Browser->>Flask: POST /fortune/draw (發送抽籤請求)
    
    Note over Flask: 後端隨機計算籤號與結果
    
    Flask->>Model: 查詢籤詩內容 (ID: 42)
    Model->>DB: SELECT * FROM lots WHERE id=42
    DB-->>Model: 回傳籤詩資料
    
    alt 使用者已登入
        Flask->>Model: 儲存本次抽籤結果
        Model->>DB: INSERT INTO user_records (...)
        DB-->>Model: 儲存成功
    end

    Flask-->>Browser: 回傳渲染後的 Result 頁面 (Jinja2)
    Browser-->>User: 顯示最終籤詩內容與指引
```

---

## 3. 功能清單對照表

以下為系統規劃的各項功能對應的 URL 路徑與 HTTP 方法：

| 功能名稱 | URL 路徑 | HTTP 方法 | 說明 |
| :--- | :--- | :--- | :--- |
| **首頁** | `/` | GET | 系統入口與功能導覽 |
| **註冊頁面** | `/auth/register` | GET / POST | 帳號創立 |
| **登入頁面** | `/auth/login` | GET / POST | 身分驗證 |
| **登出** | `/auth/logout` | POST | 清除 Session |
| **線上抽籤** | `/fortune/draw` | GET / POST | 執行抽籤演算法 |
| **查看紀錄** | `/history` | GET | 列出該使用者的所有算命歷史 |
| **紀錄詳情** | `/history/<id>` | GET | 查看特定一筆算命的詳細內容 |
| **添香油錢** | `/payment/donate` | GET / POST | 模擬捐贈功能 |

---

## 4. 流程說明

1.  **抽籤邏輯**：為了確保公平性與未來的可擴充性，抽籤的核心亂數邏輯是在 Flask 後端處理。前端主要負責提供視覺上的回饋（如 CSS 動畫）。
2.  **身分驗證**：只有登入的使用者能將結果持久化儲存在 `user_records` 資料表中。非登入使用者僅能單次查看結果，重新整理頁面後資訊將遺失。
3.  **重導向機制**：在登入或註冊成功後，系統會自動將使用者導回原本所在的頁面，確保操作體驗不中斷。
