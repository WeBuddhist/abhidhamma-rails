# Set up the vault on your computer

This guide walks you through getting the shared `abhidhamma-rails` vault onto your computer and open in Obsidian. You only do this once per computer. After setup, you just open Obsidian like a normal app and the vault keeps itself in sync with the team automatically every 10 minutes.

## A few words you'll see

- **Vault** — the folder that Obsidian uses to hold your notes.
- **Git** — the tool that syncs the vault between you and your teammates.
- **Terminal** (Mac) / **PowerShell** or **Git Bash** (Windows) — a window where you type commands instead of clicking buttons. You only need it during setup.
- **Clone** — making a copy of the GitHub repo on your own computer.
- **Sync** — what happens automatically: your changes go up to GitHub, and your teammates' changes come down to you.

## 1. Install Obsidian

Download Obsidian from [obsidian.md](https://obsidian.md) and install it. It's free and works on Mac, Windows, and Linux.

## 2. Get access to the GitHub repo

Ask the project lead to add your GitHub account as a collaborator on the `abhidhamma-rails` repo. You won't be able to clone it until they do.

> If you are setting up a *new* vault from scratch for a different text, see Section 9 of `4-SYSTEM/Guidelines/0-VAULT-Structure.md` for the vault-creation checklist. The rest of this guide assumes you're joining an existing vault.

## 3. Install Git and connect your GitHub account

You only do this once per computer. Git is the tool Obsidian uses to sync the vault. After you connect your GitHub account, you won't have to log in again.

**Mac**

1. Open Terminal. (Press `Cmd + Space`, type "Terminal", and press Return.)
2. Type `git --version` and press Return. If Git isn't installed, your Mac will ask if you want to install the Xcode Command Line Tools — click **Install** and wait for it to finish.
3. Tell Git who you are. This name and email will appear next to every change you save:
   ```
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```
4. Connect your GitHub account. The easiest way is to install [GitHub CLI](https://cli.github.com/) by running:
   ```
   brew install gh
   ```
   If Terminal says `command not found: brew`, you don't have Homebrew yet. Homebrew is a free tool that installs other tools on a Mac. Install it by pasting this into Terminal and pressing Return:
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   It will ask for your Mac password and may take a few minutes. When it finishes, you may see a "Next steps" message at the end — copy and run the two `echo` and `eval` lines it shows you (this lets Terminal find `brew`). Then run `brew install gh` again.

   Once GitHub CLI is installed, run:
   ```
   gh auth login
   ```
   Choose **GitHub.com → HTTPS → Login with a web browser** and follow the steps it shows you. After you do this once, GitHub won't ask for your password again.

**Windows**

1. Install [Git for Windows](https://git-scm.com/download/win). Keep the default settings during installation.
2. Open Git Bash (or PowerShell) and tell Git who you are:
   ```
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```
3. Install [GitHub CLI](https://cli.github.com/), then run `gh auth login` to connect your GitHub account. Choose **GitHub.com → HTTPS → Login with a web browser** and follow the steps it shows you. After you do this once, GitHub won't ask for your password again.

## 4. Make a copy of the repo (clone it) on your computer

This step downloads a copy of the GitHub repo onto your own computer. The technical word for this is *cloning*.

**First, decide where the vault should live.** Use Finder (Mac) or File Explorer (Windows) to create a folder for it — for example, a folder called `WeBuddhist` inside your Documents folder.

**Now tell the Terminal where that folder is.** The "where" is called the *path*. Here are the easiest ways to copy it.

*Mac*

- Open Terminal, type `cd ` (the letters c-d followed by one space), then **drag the folder from Finder onto the Terminal window**. Terminal will paste the path for you. Press Return.
- Or, in Finder, hold the **Option** key and right-click the folder. Choose **Copy "[folder name]" as Pathname** from the menu. Then in Terminal, type `cd ` and paste with `Cmd + V`.

*Windows*

- In File Explorer, click into the address bar at the top of the window — the path will appear. Copy it.
- Or, hold **Shift** and right-click the folder. Choose **Copy as path** from the menu.
- In PowerShell or Git Bash, type `cd ` and paste the path. (You can also drag the folder onto the PowerShell window to paste its path.)

**Copy the repo's link from GitHub.** On the repo's page on GitHub, click the green **Code** button and copy the HTTPS link.

**Download the repo into that folder.** Back in Terminal (or PowerShell / Git Bash), type `git clone ` and paste the link:

```
git clone https://github.com/WeBuddhist/abhidhamma-rails.git
```

Press Return. This creates a new folder inside the one you chose, with the vault's contents inside.

## 5. Open the folder as a vault in Obsidian

1. Open Obsidian.
2. In the menu at the top, choose **File**, then **Open Vault**.
3. In the window that appears, click **Open** next to **Open folder as vault**.
4. Choose the folder that you just downloaded.

Or, if you already have another vault open in Obsidian:

1. Click the name of the open vault in the bottom-left corner of the Obsidian window.
2. In the menu that appears, choose **Manage Vaults**.
3. In the window that appears, click **Open** next to **Open folder as vault**.
4. Choose the folder that you just downloaded.

## 6. Trust the author and close the plugin window

The first time you open the vault, Obsidian will show a warning about community plugins. This is because the Git plugin came with the template.

1. Click **Trust author & enable plugins**.
2. Obsidian will then open the Community plugins window in front of your vault. The Obsidian Git plugin is already installed and turned on, so you don't need to do anything here — just **close the window** to see your vault behind it.

That's it. The vault will now save your changes and pull in your teammates' changes automatically every 10 minutes.

## Next steps

Once the vault is open, read:

- `README.md` at the vault root — what this vault is for.
- `4-SYSTEM/Guidelines/0-VAULT-Structure.md` — how the vault is organised.
- `4-SYSTEM/How-to guides/Sync and troubleshoot.md` — how sync works day-to-day and what to do when something goes wrong.
