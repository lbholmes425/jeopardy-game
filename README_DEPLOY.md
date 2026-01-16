# Deploying Tap & Table Jeopardy to the Cloud

Your application is a **Python Web App** (dynamic), not a static website. This means it cannot be hosted on Netlify (which is for valid HTML/JS only).

**The Best Free Solution: Render.com**

I have prepared your code for Render. Follow these steps:

## Step 1: Push to GitHub
1.  Create a new repository on [GitHub.com](https://github.com/new).
2.  Open your terminal in this folder and run:
    ```bash
    git init
    git add .
    git commit -m "Ready for deployment"
    git branch -M main
    git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
    git push -u origin main
    ```

## Step 2: Deploy on Render
1.  Go to [dashboard.render.com](https://dashboard.render.com/).
2.  Click **New +** -> **Blueprint**.
3.  Connect your GitHub repository.
4.  Render will automatically detect the `render.yaml` file I created.
5.  Click **Apply**.

## That's it!
Render will build your app and give you a public URL (e.g., `https://tap-and-table.onrender.com`).
The QR Code in the app will **automatically update** to this new URL.
