# 🤖 GitHub README Auto-Update Setup

This repository uses GitHub Actions workflows to automatically update content in the README.

## Workflows Included

### 1. 📰 Medium Articles Auto-Fetch
**File:** `.github/workflows/update-articles.yml`

Automatically fetches your latest Medium articles from [@allwcons](https://medium.com/@allwcons) and updates the README every day at **12:00 UTC**.

**How it works:**
- Uses the `fetch_medium_articles.py` script to parse your Medium RSS feed
- Fetches the 5 latest articles with titles, links, and dates
- Updates the `### 📝 Latest Articles` section in README.md
- Commits and pushes changes automatically (if there are new articles)

**Manual trigger:** You can also trigger it manually from GitHub Actions tab
```
Actions → "Update Medium Articles" → Run workflow
```

**Configuration:**
- Edit `scripts/fetch_medium_articles.py` to change the number of articles or RSS feed
- Edit `.github/workflows/update-articles.yml` to change the schedule (cron time)

---

### 2. 🐍 Contribution Snake Animation
**File:** `.github/workflows/snake.yml`

Generates an animated SVG of your GitHub contributions.

**How it works:**
- Runs daily and generates a contribution snake animation
- Stores the SVG in the `output` branch
- README displays it via `<picture>` element with dark/light mode support

**First-time setup:**
1. Go to **Actions** tab on your GitHub repository
2. Click **"Generate Contribution Snake"**
3. Click **"Run workflow"** to generate the initial SVG
4. The snake SVG will be available for the README

---

## 🔧 Dependencies

### For Development (Local Testing)
```bash
pip install feedparser
```

### For GitHub Actions (Automatic)
All dependencies are installed automatically in the workflows.

---

## 📝 What Gets Updated

### Latest Articles Section
```markdown
### 📝 Latest Articles

- [Article Title](link) — *Date*
- [Another Article](link) — *Date*
...
```

The script automatically:
- ✅ Fetches from Medium RSS feed
- ✅ Extracts title, link, and publish date
- ✅ Formats in Markdown
- ✅ Updates only the articles section (preserves rest of README)
- ✅ Commits with message: `docs: update medium articles [auto]`

---

## 🚀 Getting Started

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Add GitHub Actions auto-update workflows"
   git push origin main
   ```

2. **Verify Workflows:**
   - Go to your repo → **Actions** tab
   - You should see both workflows listed:
     - ✅ Update Medium Articles
     - ✅ Generate Contribution Snake

3. **Trigger Manually (Optional):**
   - Click any workflow
   - Click **"Run workflow"**
   - Results update automatically

---

## 🔄 Scheduled Runs

| Workflow | Schedule | Time (UTC) |
|----------|----------|-----------|
| Update Medium Articles | Daily | 12:00 |
| Generate Contribution Snake | Daily | 00:00 |

---

## 📊 Example README Sections

### After Articles Auto-Update
The "Latest Articles" section automatically becomes:
```markdown
### 📝 Latest Articles

- [The Senior Carried the Chain: A Story of Two Kalis](https://medium.com/@allwcons/...) — *Jan 13, 2026*
- [How to Send "I Love You" to Your Crush Using the Internet](https://medium.com/@allwcons/...) — *Dec 25, 2025*
- [The Universe Might Be Lazy and That's a Feature, Not a Bug](https://medium.com/@allwcons/...) — *Oct 07, 2025*
...
```

### Contribution Snake
Appears as an animated SVG with dark/light mode support.

---

## ⚙️ Advanced Configuration

### Change Article Count
Edit `scripts/fetch_medium_articles.py`:
```python
NUM_ARTICLES = 10  # Change from 5 to 10
```

### Change Schedule Time
Edit `.github/workflows/update-articles.yml`:
```yaml
schedule:
  - cron: "0 14 * * *"  # Change 12 UTC to 14 UTC (2 PM)
```

**Cron Syntax:**
- `"0 12 * * *"` = Every day at 12:00 UTC
- `"0 9 * * 1"` = Every Monday at 9:00 UTC
- `"*/30 * * * *"` = Every 30 minutes

---

## 🐛 Troubleshooting

### Articles not updating?
1. Check **Actions** tab for any failed runs
2. Verify Medium RSS feed is accessible: https://medium.com/feed/@allwcons
3. Try manually triggering the workflow
4. Check git permissions (ensure workflow has write access)

### Contribution snake not showing?
1. Trigger "Generate Contribution Snake" manually first
2. Wait a few minutes for SVG generation
3. Check the `output` branch in your repo

### Images not loading?
The README uses cached images. GitHub might take 5-10 minutes to refresh cached images.
- Add `?t=` with timestamp to force refresh (but automatic workflows handle this)

---

## 📚 Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Medium RSS Feeds](https://help.medium.com/hc/en-us/articles/214874118-Using-RSS-feeds-of-publications-profiles-and-topics)
- [Feedparser Library](https://feedparser.readthedocs.io/)
- [Cron Job Scheduler](https://crontab.guru/)

---

## 📄 License

These workflows and scripts are provided as-is for use with your GitHub profile README.
