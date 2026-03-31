# Maggie's Task Master v2.0 SDD

## 1. 變更說明
- **需求 1 (List Filter)**: 在 `TaskManager` 加入 `status_filter` 邏輯，CLI 層透過 `click.Choice` 限制輸入。
- **需求 2 (Priority)**: 任務物件新增 `priority` 欄位。理由：數字雖好排序，但文字 (High/Medium/Low) 對使用者更直觀。
- **需求 3 (Interactive Delete)**: 使用 `click.confirm` 實現 y/n 互動，確保安全性。
- **需求 4 (Edit)**: 支援修改標題與優先級。理由：優先級與標題一樣重要，原地修改能維持 ID 連貫性。

## 2. 模組架構
```mermaid
graph TD
    CLI[v2/main.py] --> TM[v2/task_manager.py]
    TM --> ST[v2/storage.py]
    ST --> DB[(tasks_v2.json)]