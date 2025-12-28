# soWidget

Weather widget for windows os using tkinter.

It gets the data from [soHUB](https://github.com/rave1/soHUB)

### Method 1: Startup Folder (Easiest & Recommended)
This works on Windows 10 and 11 (including 2025 builds).

1. **Open the Startup folder quickly**  
   Press `Win + R` → type exactly this and press Enter:  
   ```
   shell:startup
   ```  
   → This opens your personal Startup folder (for the current user only).

   (Alternative full path if needed:  
   `C:\Users\YourUsername\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`  
   — replace `YourUsername` with your actual Windows username.)

2. **Create a shortcut that uses uv to run your script**  
   - Right-click inside the Startup folder → **New** → **Shortcut**
   - In the "Type the location of the item" field, paste one of these (pick the one that works for you):

     **Option A – Using `uv run` (temporary venv, very clean)**  
     ```
     uv run --with requests "F:\projekty\soWidget\temp_widget.py"
     ```  
     (Adjust the path to your script if different.)

     **Option B – If you created a persistent venv with uv**  
     ```
     "F:\projekty\soWidget\.venv\Scripts\pythonw.exe" "F:\projekty\soWidget\temp_widget.py"
     ```  
     (This uses the venv's `pythonw.exe` directly — no console window.)

     **Option C – If you prefer uv run every time**  
     ```
     uv run pythonw "F:\projekty\soWidget\temp_widget.py"
     ```

   - Click **Next** → give it a name like "Temperature Widget" → **Finish**

3. **Optional: Edit the shortcut for better behavior**  
   - Right-click the new shortcut → **Properties**
   - In the **Target** field: make sure it matches one of the options above
   - **Run**: set to **Minimized** (helps if any tiny flash happens)
   - Click OK

4. **Test it**  
   - Double-click the shortcut → your widget should appear (no console if using `pythonw`)
   - Restart your computer → it should launch automatically after login

### Method 2: Task Scheduler (More control, runs even if not logged in — but usually overkill for a widget)
If you want it to start before login or with higher privileges:

1. Search for **Task Scheduler** in the Start menu and open it.
2. Right-click **Task Scheduler Library** → **Create Basic Task**
3. Name: "Temperature Widget"
4. Trigger: **When I log on** (or **At startup** if you want it earlier)
5. Action: **Start a program**
   - Program/script: `uv` (or full path like `C:\Users\YourName\.local\bin\uv.exe` if needed)
   - Add arguments:  
     `run --with requests "F:\projekty\soWidget\temp_widget.py"`  
     or for pythonw:  
     `run pythonw "F:\projekty\soWidget\temp_widget.py"`
   - Start in (optional): `F:\projekty\soWidget`
6. Finish → then right-click your new task → **Properties** → check **Run with highest privileges** if needed, and **Hidden** under General if you want no flash.
7. Test: right-click the task → **Run**

### Tips & Troubleshooting
- **Nothing happens after restart?**  
  → Double-check the path in the shortcut/task is correct (copy-paste from File Explorer).  
  → Test by logging out & back in (faster than full reboot).

- **Console flashes briefly?**  
  → Make sure you're using `pythonw` (not `python`) in the command.

- **uv not found?**  
  → Run `where uv` in cmd to see its path, then use the full path in the shortcut:  
  `"C:\full\path\to\uv.exe" run ...`

- **For all users** (rarely needed): use `shell:common startup` instead of `shell:startup`.

This should get your widget launching on every Windows start. Let me know if you get any error message when double-clicking the shortcut — we can debug it quickly!
