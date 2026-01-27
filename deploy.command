#!/bin/bash
cd "$(dirname "$0")"

echo "========================================"
echo "    TAP & TABLE JEOPARDY - DEPLOYER     "
echo "========================================"
echo ""
echo "This will upload your latest changes to GitHub."
echo "Render will automatically see them and update the live site."
echo ""
read -p "Enter a message for this update (e.g. 'Fixed typo'): " commit_msg

if [ -z "$commit_msg" ]; then
    commit_msg="Update game content"
fi

echo ""
echo "Step 1: Saving files..."
git add .

echo "Step 2: Committing changes..."
git commit -m "$commit_msg"

echo "Step 3: Uploading to GitHub..."
git push

echo ""
echo "========================================"
if [ $? -eq 0 ]; then
    echo "SUCCESS! Changes uploaded."
    echo "Render is now building your new version."
    echo "Check status here: https://dashboard.render.com"
else
    echo "ERROR: Something went wrong."
fi
echo "========================================"
echo ""
read -p "Press Enter to close..."
