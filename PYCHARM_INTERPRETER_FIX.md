# Fixing the PyCharm "No Interpreter" Issue

After creating a virtual environment, PyCharm sometimes still shows `<No interpreter>`. This happens because PyCharm's project config is pointing to a Python version that was never registered.

Follow these steps to fix it manually.

---

## Step 1 — Close PyCharm completely

Do this before editing any files. If PyCharm is open, it will overwrite your changes when it closes.

---

## Step 2 — Edit the project interpreter reference

Open this file in Notepad:

```
C:\Users\cesar\PycharmProjects\Coin-Collector\.idea\misc.xml
```

Replace the entire contents with this:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="Black">
    <option name="sdkName" value="Python 3.12 (Coin-Collector)" />
  </component>
  <component name="ProjectRootManager" version="2" project-jdk-name="Python 3.12 (Coin-Collector)" project-jdk-type="Python SDK" />
</project>
```

Save and close.

---

## Step 3 — Register the venv in PyCharm's global SDK list

Open this file in Notepad:

```
C:\Users\cesar\AppData\Roaming\JetBrains\PyCharm2026.1\options\jdk.table.xml
```

> If your PyCharm version is different (e.g. 2025.1), adjust the folder name accordingly.

Find the two closing lines at the very bottom of the file:

```xml
  </component>
</application>
```

Insert the block below **above** those two closing lines, then save:

```xml
    <jdk version="2">
      <name value="Python 3.12 (Coin-Collector)" />
      <type value="Python SDK" />
      <version value="Python 3.12.3" />
      <homePath value="$USER_HOME$/PycharmProjects/Coin-Collector/.venv/Scripts/python.exe" />
      <roots>
        <classPath>
          <root type="composite">
            <root url="file://C:/Program Files/Python312/DLLs" type="simple" />
            <root url="file://C:/Program Files/Python312/Lib" type="simple" />
            <root url="file://C:/Program Files/Python312" type="simple" />
            <root url="file://$USER_HOME$/PycharmProjects/Coin-Collector/.venv" type="simple" />
            <root url="file://$USER_HOME$/PycharmProjects/Coin-Collector/.venv/Lib/site-packages" type="simple" />
            <root url="file://$APPLICATION_HOME_DIR$/plugins/python-ce/helpers/typeshed/stdlib" type="simple" />
          </root>
        </classPath>
        <sourcePath>
          <root type="composite" />
        </sourcePath>
      </roots>
      <additional ASSOCIATED_PROJECT_PATH="$USER_HOME$/PycharmProjects/Coin-Collector" SDK_UUID="a1b2c3d4-e5f6-7890-abcd-ef1234567890">
        <setting name="FLAVOR_ID" value="VirtualEnvSdkFlavor" />
        <setting name="FLAVOR_DATA" value="{}" />
      </additional>
    </jdk>
```

---

## Step 4 — Open PyCharm

Open PyCharm and the project. The status bar at the bottom should now show **Python 3.12 (Coin-Collector)**. If it does, you are done.

---

## Step 5 — Install dependencies

Open the Terminal tab inside PyCharm and run:

```powershell
pip install pygame
pip install pgzero pytest
```

Verify they landed in the right place:

```powershell
pip show pygame pgzero pytest
```

All three should show a `Location` path containing `Coin-Collector\.venv`.
