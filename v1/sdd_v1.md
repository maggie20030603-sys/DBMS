# 專案概覽
- 程式名稱：Maggie's Task Master
- 版本：v1.0
- 一句話描述：一個專為學生設計的 CLI 任務管理工具，支援基本 CRUD 功能與 JSON 儲存。
- 目標使用者：偏好簡潔介面的開發者。

# 2. CLI 介面規格
| 指令 | 參數 | 說明 | 範例 |
|---|---|---|---|
| `add` | `--title TEXT` | 新增一個待辦任務 | `python v1/main.py add --title "買咖啡"` |
| `list` | (無) | 顯示所有任務清單 | `python v1/main.py list` |
| `done` | `--id INT` | 將指定 ID 任務標記為完成 | `python v1/main.py done --id 1` |

# 3. 資料模型 (Data Model)
- **id** (int): 任務唯一識別碼。
- **title** (str): 任務標題描述。
- **status** (str): 任務狀態 (todo / done)。
- **created_at** (str): ISO 8601 格式的建立時間。

# 4. 模組架構 (Module Design)
```mermaid
graph TD
    A[main.py] --> B[task_manager.py]
    B --> C[storage.py]
    C --> D[(tasks.json)]