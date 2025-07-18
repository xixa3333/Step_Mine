
# 🧨 踩地雷遊戲 (Minesweeper Game)

這是一款使用 **Python Tkinter GUI** 製作的經典踩地雷遊戲，支援三種難度、旗子功能、自動展開空白區域與計時功能，並已成功打包為 `.exe` 可執行檔，提供 Windows 用戶輕鬆體驗。

<img width="400" height="500" alt="image" src="https://github.com/user-attachments/assets/d85dfe98-a163-4772-ac46-cae39407d871" />

---

## 🎮 遊戲玩法

- 使用滑鼠左鍵點擊方格探索地圖
- 使用右鍵插旗標記地雷
- 若點到地雷則遊戲結束
- 成功揭開所有非地雷格子即為勝利

---

## 🧩 功能特色

- ✅ 三種遊戲難度（簡單、普通、困難）
- ✅ 圖形介面、直觀操作（Tkinter + PIL）
- ✅ 自動避開首次點擊地雷
- ✅ 支援插旗與取消插旗
- ✅ 空白區域自動展開
- ✅ 計時功能顯示遊戲時間
- ✅ 顯示剩餘旗子數量
- ✅ 已打包為 `.exe` 可直接執行

---

## 📦 執行方式（Windows）

### 下載執行檔 `.exe`：
> 👉 [點我下載踩地雷遊戲 EXE（Windows）](https://github.com/xixa3333/Step_Mine/releases)

下載後直接雙擊執行，無需安裝 Python 或其他環境。

---

## 🧑‍💻 開發者環境安裝（原始碼運行）

若你希望從原始碼執行此專案，可按照以下步驟操作：

### ✅ 安裝必要套件

```bash
pip install pillow
````

### ✅ 執行遊戲

```bash
python main.py
```

> 注意：請將 `image` 資料夾與 `main.py` 放在同一目錄下。

---

## 🧰 打包為 EXE 的方法（開發者用）

本專案使用 `PyInstaller` 打包：

```bash
pyinstaller -F -w -i icon.ico main.py --add-data "image;image"
```

* `-F`：打包為單一檔案
* `-w`：隱藏命令提示字元視窗
* `--add-data`：包含圖檔資料夾（`image`）

若圖檔在資料夾中，請確保 `resource_path()` 函式正確指向打包後的路徑。

---

## 🙌 貢獻方式

歡迎 Fork 本專案，提交 PR 增加新功能或優化程式碼。如果你有任何建議或問題，也歡迎提出 [Issues](https://github.com/你的帳號/你的倉庫/issues)。

---

感謝使用！祝您踩雷順利 😄
