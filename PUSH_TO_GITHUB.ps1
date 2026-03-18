# KPI Report Automation - Push to GitHub Script
# This script automates pushing your project to GitHub

$ErrorActionPreference = "Stop"

Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host "  KPI Report Automation - GitHub Push Automation" -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host ""

# Step 1: Configure Git
Write-Host "Step 1️⃣  Configuring Git..." -ForegroundColor Green
git config --global user.name "mugilancrajan"
git config --global user.email "mchinnapparajan@gmail.com"
Write-Host "✅ Git configured with:" -ForegroundColor Green
Write-Host "   Name: mugilancrajan"
Write-Host "   Email: mchinnapparajan@gmail.com"
Write-Host ""

# Step 2: Check if repo exists
Write-Host "Step 2️⃣  Checking repository status..." -ForegroundColor Green
if (Test-Path ".git") {
    Write-Host "✅ Git repository found" -ForegroundColor Green
} else {
    Write-Host "⚠️  Initializing git repository..." -ForegroundColor Yellow
    git init
}
Write-Host ""

# Step 3: Add files
Write-Host "Step 3️⃣  Adding all files to git..." -ForegroundColor Green
git add .
$fileCount = (git ls-files).Count
Write-Host "✅ Added $fileCount files" -ForegroundColor Green
Write-Host ""

# Step 4: Create commit
Write-Host "Step 4️⃣  Creating initial commit..." -ForegroundColor Green
git commit -m "Initial commit: Complete KPI Report Automation project

- Data generation pipeline with 2,500 synthetic leads
- Data cleaning and weekly KPI aggregation
- Professional HTML report with embedded charts
- Streamlit interactive dashboard
- GitHub Actions workflow for weekly automation
- Comprehensive documentation and guides"
Write-Host "✅ Commit created successfully" -ForegroundColor Green
Write-Host ""

# Step 5: Ensure main branch
Write-Host "Step 5️⃣  Setting up main branch..." -ForegroundColor Green
git branch -M main
Write-Host "✅ Main branch ready" -ForegroundColor Green
Write-Host ""

# Step 6: Add remote
Write-Host "Step 6️⃣  Connecting to GitHub..." -ForegroundColor Green
$username = "mugilancrajan"
$repo = "kpi-report-automation"
$remoteUrl = "https://github.com/$username/$repo.git"

# Check if remote already exists
try {
    $existingRemote = git remote get-url origin 2>$null
    if ($existingRemote) {
        Write-Host "⚠️  Remote already exists, updating..." -ForegroundColor Yellow
        git remote remove origin
    }
} catch {
    # Remote doesn't exist, continue
}

git remote add origin $remoteUrl
Write-Host "✅ GitHub remote added:" -ForegroundColor Green
Write-Host "   $remoteUrl"
Write-Host ""

# Step 7: Push to GitHub
Write-Host "Step 7️⃣  Pushing to GitHub..." -ForegroundColor Green
Write-Host "   This may prompt for authentication..." -ForegroundColor Yellow
Write-Host ""

try {
    git push -u origin main
    Write-Host ""
    Write-Host "✅ SUCCESS! Your project has been pushed to GitHub!" -ForegroundColor Green
    Write-Host ""
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
    Write-Host "📍 Your project is now at:" -ForegroundColor Green
    Write-Host "   https://github.com/$username/$repo" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "📋 Next steps:" -ForegroundColor Green
    Write-Host "   1. Go to your GitHub repo page" -ForegroundColor White
    Write-Host "   2. Click 'About' (top right)" -ForegroundColor White
    Write-Host "   3. Add topics: python, data-analytics, streamlit, automation" -ForegroundColor White
    Write-Host "   4. Share the link with recruiters/employers!" -ForegroundColor White
    Write-Host ""
    Write-Host "🎉 Your portfolio project is live!" -ForegroundColor Green
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
} catch {
    Write-Host ""
    Write-Host "⚠️  Authentication Issue" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "The script needs a Personal Access Token to push to GitHub." -ForegroundColor White
    Write-Host ""
    Write-Host "To fix this:" -ForegroundColor Yellow
    Write-Host "1. Go to: https://github.com/settings/tokens" -ForegroundColor White
    Write-Host "2. Click 'Generate new token'" -ForegroundColor White
    Write-Host "3. Select: repo, read:user, write:repo_hook" -ForegroundColor White
    Write-Host "4. Copy the token" -ForegroundColor White
    Write-Host "5. When prompted, paste it as your password" -ForegroundColor White
    Write-Host ""
    Write-Host "Then try the push again:" -ForegroundColor Yellow
    Write-Host "   git push -u origin main" -ForegroundColor Cyan
}
